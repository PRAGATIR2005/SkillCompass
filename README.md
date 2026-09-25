# SkillCompass

## AI-Based Skill Assessment and Career Guidance System for Students

SkillCompass is an AI-based skill assessment and career guidance system designed to help students and professionals make informed educational and career decisions based on their skills, interests, abilities, and preferences.

## Project Overview

The system uses machine learning to provide stage-specific recommendations for different educational and professional decision points.

### Four Stages

| Stage | User Group | Purpose |
|---|---|---|
| Stage 1 | Post-10th | Stream Selection |
| Stage 2 | Post-12th / PUC | Higher Education Field Selection |
| Stage 3 | Working Professionals | Career Switch Guidance |
| Stage 4 | Postgraduates | Next Career Step |

## Objectives

- Assess users based on skills, interests, abilities, and preferences.
- Provide personalized educational and career recommendations.
- Use machine learning for stage-specific classification.
- Identify skill gaps between the user's profile and target paths.
- Maintain secure user authentication and assessment history.

## Technologies Used

- Python
- Streamlit
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- SQLAlchemy
- SQLite
- JWT Authentication
- bcrypt
- Git & GitHub

## Machine Learning

The project uses a Gradient Boosting Classifier for stage-specific prediction.

Current experimental model accuracies:

| Stage | Accuracy |
|---|---:|
| Stage 1 | 96.82% |
| Stage 2 | 97.70% |
| Stage 3 | 89.60% |
| Stage 4 | 93.20% |

The current models are trained using synthetic datasets for academic prototype development.

## Main Features

- User registration and login
- Password hashing
- JWT-based authentication
- Stage-specific assessments
- Machine-learning-based recommendations
- Skill-gap analysis
- Assessment history
- Stage-based access control
- Model evaluation and feature importance

## Project Structure

SkillCompass/
├── app/
├── backend/
├── database/
├── models/
├── training/
├── requirements.txt
├── .gitignore
└── README.md

## Running the Project

### Start Backend

uvicorn backend.main:app --reload

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

### Start Frontend

streamlit run app/app.py

Frontend:

http://localhost:8501

## SDG Alignment

The project is aligned with:

SDG 4 – Quality Education

SkillCompass aims to support personalized educational and career guidance through technology and machine learning.

## Future Enhancements

- Real-world survey data integration
- Learning-resource recommendations based on skill gaps
- Personalized learning paths
- Expanded career and course database
- Cloud deployment
- Improved recommendation explainability

## Academic Project

Project Title: AI-Based Skill Assessment and Career Guidance System for Students

Project Name: SkillCompass

Domains: Artificial Intelligence, Machine Learning, Big Data, Cloud Computing and Web Technologies