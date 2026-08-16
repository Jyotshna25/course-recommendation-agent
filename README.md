#  AI Course Recommendation Agent

An AI-powered Course Recommendation Agent that creates a personalized learning path for students based on their background, current skills, and career goals.

The application uses Groq AI to analyze the student's profile and recommend a logical sequence of courses from a predefined course catalogue.

##  Features

- Personalized course recommendations
- Uses student background, skills, and career goals
- Groq-powered AI reasoning
- Course catalogue stored in JSON
- CLI/backend version available
- Interactive Streamlit web interface
- Environment-based API key configuration
- Sample student profiles and generated recommendations

##  Project Structure

```text
course-recommendation-agent/
│
├── app.py                  # Streamlit user interface
├── main.py                 # CLI/backend recommendation agent
├── courses.json            # Course catalogue
├── profiles.json           # Sample student profiles
├── recommendation.json     # Sample generated recommendations
├── requirements.txt        # Python dependencies
├── .env                    # API key (not committed)
├── .gitignore              # Ignores secrets and virtual environment
└── README.md               # Project documentation

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jyotshna25/course-recommendation-agent.git
cd course-recommendation-agent


2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure the Groq API Key

Create a .env file in the project folder and add:

GROQ_API_KEY=your_groq_api_key_here

Replace your_groq_api_key_here with your own Groq API key.

Do not commit the .env file to GitHub.

5. Run the CLI Agent
python main.py
6. Run the Streamlit App
streamlit run app.py

The application will open at:

http://localhost:8501
How It Works

The agent takes the student's background, current skills, and career goal and uses Groq AI to generate a personalized learning path from the available course catalogue.

Workflow
Student Profile
      ↓
Background + Skills + Career Goal
      ↓
Course Catalogue
      ↓
Groq AI
      ↓
Personalized Learning Path
Sample Input
Name: Jyotshna


Background: CSE-AIML student with basic programming knowledge


Current Skills: Python, SQL


Career Goal: Machine Learning and Artificial Intelligence
Sample Output
PERSONALIZED LEARNING PATH


1. Data Structures and Algorithms
   Reason: Builds strong problem-solving and algorithmic foundations.


2. Machine Learning Fundamentals
   Reason: Introduces core machine learning concepts and algorithms.


3. Deep Learning with Neural Networks
   Reason: Builds knowledge of neural networks and deep learning.


4. Generative AI and LLMs
   Reason: Introduces modern generative AI and language models.
Technology Stack
Python
Groq API
Streamlit
JSON
python-dotenv
Design Decisions

The course catalogue is stored separately in courses.json, allowing courses to be added or modified without changing the recommendation logic.

The agent uses the student's background, current skills, and career goal together with the course catalogue to generate a logical learning sequence.

The project provides both a CLI/backend implementation and a Streamlit interface.

Tradeoffs and Future Improvements
Current Tradeoffs
The course catalogue is stored locally in JSON instead of a database.
Recommendation quality depends on the available course catalogue.
Student progress is not currently tracked over time.
The current implementation uses a single LLM-based recommendation process.
Future Improvements
Add a database for courses and student profiles.
Track completed courses and learning progress.
Add course prerequisites and difficulty levels.
Add course ratings and user feedback.
Add authentication and persistent profiles.
Deploy the Streamlit application online.
Add evaluation metrics for recommendation quality.
Agent-Specific Deliverable

This project implements an AI-powered Course Recommendation Agent.

The agent analyzes a student's:

Background
Existing skills
Career goal

and generates a personalized sequence of courses from the course catalogue.

The project demonstrates:

Student profile collection
Course catalogue retrieval
LLM-based reasoning
Personalized recommendation generation
Learning-path generation
CLI and Streamlit interfaces