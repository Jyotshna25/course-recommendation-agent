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