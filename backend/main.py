from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import engine
from database.models import Base

from backend.routes.auth import router as auth_router
from backend.routes.assessments import router as assessment_router


# ============================================================
# CREATE DATABASE TABLES
# ============================================================

Base.metadata.create_all(
    bind=engine
)


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="SkillCompass API",
    description=(
        "Backend API for the SkillCompass "
        "AI-based skill assessment system"
    ),
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:8501",
        "http://127.0.0.1:8501"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ============================================================
# ROUTES
# ============================================================

app.include_router(
    auth_router
)

app.include_router(
    assessment_router
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    return {
        "message": "SkillCompass Backend is running",
        "status": "success"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }