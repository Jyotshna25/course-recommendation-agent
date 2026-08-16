import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)




def load_courses():
    with open("courses.json", "r", encoding="utf-8") as file:
        return json.load(file)



# CHECK PREREQUISITES


def check_prerequisites(course, known_skills, completed_courses):
    """
    Returns True if the student satisfies the prerequisites.
    """

    prerequisites = course.get("prerequisites", [])

    for prerequisite in prerequisites:

        # Check if prerequisite course was completed
        if prerequisite in completed_courses:
            continue

        # Check if prerequisite skill is already known
        if prerequisite in known_skills:
            continue

        return False

    return True




def find_matching_courses(profile, courses):
    """
    Find courses relevant to the student's goals while:
    - avoiding courses for skills the student already knows
    - respecting prerequisites
    - prioritising courses that directly support the student's goals
    """

    known_skills = {
        skill.lower().strip()
        for skill in profile.get("known_skills", [])
    }

    goals = {
        goal.lower().strip()
        for goal in profile.get("goals", [])
    }

    completed_courses = {
        course.lower().strip()
        for course in profile.get("completed_courses", [])
    }

    # Map course IDs to courses
    course_map = {
        course["id"]: course
        for course in courses
    }

    def prerequisite_is_satisfied(prerequisite_id):
        """
        A prerequisite is satisfied if:
        1. The student completed that course, OR
        2. The student already knows one of the skills taught by it.
        """

        if prerequisite_id in completed_courses:
            return True

        prerequisite_course = course_map.get(prerequisite_id)

        if not prerequisite_course:
            return False

        prerequisite_skills = {
            skill.lower()
            for skill in prerequisite_course.get("skills", [])
        }

        return bool(prerequisite_skills.intersection(known_skills))

    def prerequisites_met(course):
        for prerequisite in course.get("prerequisites", []):
            if not prerequisite_is_satisfied(prerequisite):
                return False

        return True

    recommendations = []

    for course in courses:

        course_id = course["id"].lower()

        # Skip already completed courses
        if course_id in completed_courses:
            continue

        # Skip courses whose prerequisites are not satisfied
        if not prerequisites_met(course):
            continue

        course_skills = {
            skill.lower()
            for skill in course.get("skills", [])
        }

        course_text = (
            course["name"].lower()
            + " "
            + " ".join(course.get("skills", [])).lower()
            + " "
            + course.get("description", "").lower()
        )

        # Don't recommend courses whose main skills are already known
        new_skills = course_skills - known_skills

        if not new_skills:
            continue

        score = 0

        # Strong priority for direct goal matches
        for goal in goals:

            if goal in course["name"].lower():
                score += 10

            if goal in course_text:
                score += 6

            for skill in course_skills:
                if goal in skill or skill in goal:
                    score += 8

        # Give some priority to courses that add new skills
        score += len(new_skills) * 2

        if score > 0:
            recommendations.append((score, course))

    # Highest relevance first
    recommendations.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [course for score, course in recommendations]




def generate_recommendation(profile, recommended_courses):

    courses_text = json.dumps(
        recommended_courses,
        indent=2
    )

    prompt = f"""
You are an expert educational career advisor.

Create a personalised learning path for this student.

STUDENT PROFILE:
{json.dumps(profile, indent=2)}

AVAILABLE RECOMMENDED COURSES:
{courses_text}

Your job:

1. Recommend the courses in the best learning order.
2. Explain why every course was selected.
3. Explain how each course helps the student's goal.
4. Respect prerequisites.
5. Do NOT recommend courses that mainly teach skills the student
   already knows.
6. Prioritize courses that directly contribute to the student's goals.
7. Prefer a logical progression from foundational courses to advanced courses.
8. Do not invent courses that are not present in the provided catalogue.

Return the answer in this format:

LEARNING PATH

1. Course Name
   Why: ...

2. Course Name
   Why: ...

3. Course Name
   Why: ...

FINAL GOAL:
Explain how this learning path helps the student reach their goal.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful educational career advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1200
    )

    return response.choices[0].message.content


# --------------------------------------------------
# DISPLAY STUDENT PROFILE
# --------------------------------------------------

def get_student_profile():

    print("\n" + "=" * 60)
    print("       COURSE RECOMMENDATION AGENT")
    print("=" * 60)

    name = input("\nStudent name: ")

    background = input(
        "Educational background (e.g. CSE student): "
    )

    goals_input = input(
        "Career goals (comma separated): "
    )

    skills_input = input(
        "Known skills (comma separated): "
    )

    completed_input = input(
        "Completed courses (comma separated, or press Enter): "
    )

    profile = {
        "name": name,
        "background": background,
        "goals": [
            goal.strip()
            for goal in goals_input.split(",")
            if goal.strip()
        ],
        "known_skills": [
            skill.strip()
            for skill in skills_input.split(",")
            if skill.strip()
        ],
        "completed_courses": [
            course.strip()
            for course in completed_input.split(",")
            if course.strip()
        ]
    }

    return profile


# --------------------------------------------------
# MAIN AGENT
# --------------------------------------------------

def main():

    courses = load_courses()

    profile = get_student_profile()

    print("\nAnalyzing your profile...")
    print("Matching courses and checking prerequisites...\n")

    recommended_courses = find_matching_courses(
        profile,
        courses
    )

    if not recommended_courses:

        print("No matching courses found.")
        print(
            "Try adding a broader career goal or skill."
        )
        return

    print(
        f"Found {len(recommended_courses)} "
        "potential courses."
    )

    print("\nGenerating personalised learning path...\n")

    recommendation = generate_recommendation(
        profile,
        recommended_courses
    )

    print("\n" + "=" * 60)
    print("PERSONALISED LEARNING PATH")
    print("=" * 60)

    print(recommendation)

    print("\n" + "=" * 60)
    print("END OF RECOMMENDATION")
    print("=" * 60)



# RUN


if __name__ == "__main__":
    main()