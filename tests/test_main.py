import os

# main.py requires a Groq API key when imported.
os.environ["GROQ_API_KEY"] = "test-key"

from main import check_prerequisites, find_matching_courses


def test_prerequisites_are_satisfied():
    course = {
        "prerequisites": ["Python"]
    }

    assert check_prerequisites(
        course,
        ["Python"],
        []
    ) is True


def test_prerequisites_are_not_satisfied():
    course = {
        "prerequisites": ["Python"]
    }

    assert check_prerequisites(
        course,
        [],
        []
    ) is False


def test_completed_course_is_not_recommended():
    profile = {
        "goals": ["Machine Learning"],
        "known_skills": [],
        "completed_courses": ["python-basics"]
    }

    courses = [
        {
            "id": "python-basics",
            "name": "Python Programming Fundamentals",
            "skills": ["python"],
            "prerequisites": [],
            "description": "Learn Python."
        },
        {
            "id": "machine-learning",
            "name": "Machine Learning Fundamentals",
            "skills": ["machine learning"],
            "prerequisites": [],
            "description": "Learn machine learning."
        }
    ]

    recommendations = find_matching_courses(profile, courses)

    ids = [course["id"] for course in recommendations]

    assert "python-basics" not in ids