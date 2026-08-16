import streamlit as st
import json
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load course catalogue
with open("courses.json", "r", encoding="utf-8") as f:
    courses = json.load(f)


def generate_recommendation(name, background, skills, goal):

    course_catalogue = json.dumps(courses, indent=2)

    prompt = f"""
You are an intelligent Course Recommendation Agent.

Your task is to create a personalized and ordered learning path.

STUDENT PROFILE:
Name: {name}
Background: {background}
Current Skills: {skills}
Career Goal: {goal}

COURSE CATALOGUE:
{course_catalogue}

Instructions:
1. Recommend only courses that exist in the catalogue.
2. Consider the student's existing skills.
3. Respect course prerequisites.
4. Arrange courses in the correct learning order.
5. Explain why every recommended course was selected.
6. Avoid recommending courses the student already knows.
7. Keep the learning path practical and personalized.

Return the answer in this format:

PERSONALIZED LEARNING PATH

1. Course Name
Why: Explanation

2. Course Name
Why: Explanation

3. Course Name
Why: Explanation

FINAL GOAL:
Explain how this learning path helps the student achieve their career goal.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert academic and career learning-path advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content



# Streamlit UI


st.set_page_config(
    page_title="Course Recommendation Agent",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Course Recommendation Agent")

st.markdown(
    """
    ### 🚀 Build Your Personalized Learning Path

    Get AI-powered course recommendations based on your **background,
    current skills, and career goals**.
    
    Your learning journey is analyzed using **Groq AI** to create a
    structured and personalized course roadmap.
    """
)

st.divider()

# Student information
st.subheader("👨‍🎓 Student Profile")

name = st.text_input(
    "Student Name",
    placeholder="Enter your name"
)

background = st.text_area(
    "Background",
    placeholder="Example: CSE-AIML student with basic programming knowledge"
)

skills = st.text_input(
    "Current Skills",
    placeholder="Example: Python, SQL, HTML"
)

goal = st.text_input(
    "Career / Learning Goal",
    placeholder="Example: Machine Learning and Artificial Intelligence"
)

st.divider()

if st.button("🚀 Generate Learning Path", use_container_width=True):

    if not name or not background or not skills or not goal:
        st.warning("Please fill in all the student profile fields.")

    else:
        with st.spinner("🤖 AI Agent is creating your personalized learning path..."):

            try:
                recommendation = generate_recommendation(
                    name,
                    background,
                    skills,
                    goal
                )

                st.success("Learning path generated successfully!")

                st.subheader("🎯 Personalized Learning Path")

                st.markdown(recommendation)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.divider()

st.caption(
    "Course Recommendation Agent • Personalized learning using Groq AI"
)