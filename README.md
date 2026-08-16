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

## set up and installation
### 1. Clone the repository
```bash
git clone https://github.com/Jyotshna25/course-recommendation-agent.git
cd course-recommendation-agent
```
### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure the Groq API Key

Create a `.env` file in the project folder and add:

```text
GROQ_API_KEY=your_groq_api_key_here
```
### 5. Run the CLI Agent

```bash
python main.py
```
### 6. Run the Streamlit App

```bash
streamlit run app.py
```

The application will open at:

`http://localhost:8501`


## How It Works

The agent takes the student's background, current skills, and career goal and uses Groq AI to generate a personalized learning path from the available course catalogue.

### Workflow

Student Profile  
↓  
Background + Skills + Career Goal  
↓  
Course Catalogue  
↓  
Groq AI  
↓  
Personalized Course Recommendations



## Sample Input

Name: Jyotshna

Background: CSE-AIML student with basic programming knowledge

Current Skills: Python, SQL

Career Goal: Machine Learning and Artificial Intelligence

## Sample Output

PERSONALIZED LEARNING PATH

1. Machine Learning Fundamentals
   Reason: Builds the foundation required for machine learning and AI.

2. Deep Learning with Neural Networks
   Reason: Builds knowledge of neural networks and advanced AI techniques.

3. Natural Language Processing
   Reason: Develops skills for working with text and human language.

4. Generative AI and LLMs
   Reason: Builds on ML and NLP knowledge to understand modern generative AI.


   ## Sample Input

Name: Jyotshna

Background: CSE-AIML student with basic programming knowledge

Current Skills: Python, SQL

Career Goal: Machine Learning and Artificial Intelligence

## Sample Output

PERSONALIZED LEARNING PATH

1. Machine Learning Fundamentals
   Reason: Builds the foundation required for machine learning and AI.

2. Deep Learning with Neural Networks
   Reason: Builds knowledge of neural networks and advanced AI techniques.

3. Natural Language Processing
   Reason: Develops skills for working with text and human language.

4. Generative AI and LLMs
   Reason: Builds on ML and NLP knowledge to understand modern generative AI.


   ## Tradeoffs and Future Improvements

### Current Tradeoffs

- The course catalogue is stored locally in JSON instead of a database.
- Recommendation quality depends on the courses available in the catalogue.
- Student progress is not currently tracked over time.
- The system uses an LLM-based recommendation approach, so responses may vary.

### Future Improvements

- Add a database for courses and student profiles.
- Track completed courses and learning progress.
- Add course difficulty and prerequisite relationships.
- Add course ratings and student feedback.
- Add authentication and persistent student profiles.
- Deploy the Streamlit application online.
- Add evaluation metrics to measure recommendation quality.

## Agent-Specific Deliverables

This project implements an AI-powered Course Recommendation Agent.

### Course Catalogue

The course catalogue is provided in `courses.json` and contains courses, skills, levels, descriptions, and prerequisites.

### Sample Student Profiles

Four sample student profiles are provided in `profiles.json` to demonstrate personalized recommendations for different backgrounds and career goals.

### Recommended Learning Paths

Sample recommendations are provided in `recommendation.json`.

### Recommendation Rationale

For each recommended course, the agent provides a reason explaining why the course was selected and how it supports the student's learning or career goal.

Replace `your_groq_api_key_here` with your own Groq API key.

**Do not commit the `.env` file to GitHub.**