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
- Identify suitable pathways based on assessment results.
- Maintain user assessment information and history.

## Technologies Used

- Python
- Streamlit
- FastAPI
- Scikit-learn
- Pandas and NumPy
- SQLAlchemy and SQLite
- Ollama (Llama 3.2 3B)
- Matplotlib
- Git and GitHub

## Machine Learning

The project uses four separate Gradient Boosting Classifier models, one for each assessment stage.

Current experimental model performance:

| Stage | Accuracy |
|---|---:|
| Stage 1 | 96.82% |
| Stage 2 | 97.27% |
| Stage 3 | 90.00% |
| Stage 4 | 93.18% |

The models are trained and evaluated using synthetic datasets.

**Note:** These results represent experimental classification performance on held-out synthetic test data, not real-world career prediction accuracy.

## AI-Powered Career Guidance

SkillCompass integrates Ollama with the Llama 3.2 3B model to generate personalized career guidance.

The LLM uses the predicted pathway and assessment feature scores to provide:

- Reasons to explore the recommended pathway.
- Potential strengths indicated by assessment responses.
- Areas for further development.
- Practical next steps.

The ML model determines the recommended pathway, while the LLM provides supplementary guidance.

## Main Features

- User registration and login.
- Stage-specific assessments.
- Machine-learning-based recommendations.
- AI-generated personalized career guidance.
- Assessment history.
- Model evaluation and feature importance visualization.

## Project Structure

```text
SkillCompass/
├── app/
├── backend/
├── database/
├── models/
│   ├── stage1/
│   ├── stage2/
│   ├── stage3/
│   └── stage4/
├── training/
├── requirements.txt
├── .gitignore
└── README.md
```

## Running the Project

### Start Backend

```bash
python -m uvicorn backend.main:app --reload
```

Backend: http://127.0.0.1:8000

API Documentation: http://127.0.0.1:8000/docs

### Start Frontend

```bash
python -m streamlit run app/app.py
```

Frontend: http://localhost:8501

### AI Guidance Setup

Install Ollama and download the required model:

```bash
ollama pull llama3.2:3b
```

Ensure Ollama is running before using AI-generated guidance.

## SDG Alignment

**SDG 4 – Quality Education**

SkillCompass aims to support personalized educational exploration and career guidance through artificial intelligence and machine learning.

## Future Enhancements

- Integration of real-world assessment data.
- Personalized learning-resource recommendations.
- Expanded career and course database.
- Cloud deployment.
- Improved recommendation explainability.

## Academic Project

**Project Title:** AI-Based Skill Assessment and Career Guidance System for Students

**Project Name:** SkillCompass

**Domains:** Artificial Intelligence, Machine Learning, Data Science and Web Technologies.