from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db

from database.models import (
    Assessment,
    AssessmentResponse,
    FeatureScore
)

from backend.dependencies import get_current_user


# ============================================================
# ROUTER
# ============================================================

router = APIRouter(
    prefix="/assessments",
    tags=["Assessments"]
)


# ============================================================
# SAVE ASSESSMENT
# ============================================================

@router.post("/")
def save_assessment(
    assessment_data: dict,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Current authenticated user
    # --------------------------------------------------------

    user_id = current_user["id"]

    # --------------------------------------------------------
    # Get assessment information
    # --------------------------------------------------------

    stage = assessment_data.get("stage")

    recommendation = assessment_data.get(
        "recommendation"
    )

    responses = assessment_data.get(
        "responses",
        {}
    )

    feature_scores = assessment_data.get(
        "feature_scores",
        {}
    )

    # --------------------------------------------------------
    # Validate stage
    # --------------------------------------------------------

    if not stage:

        raise HTTPException(
            status_code=400,
            detail="Assessment stage is required."
        )

    # --------------------------------------------------------
    # Stage access protection
    # --------------------------------------------------------

    if stage != current_user.get("stage"):

        raise HTTPException(
            status_code=403,
            detail=(
                "You are not authorized to submit "
                "an assessment for this stage."
            )
        )

    # --------------------------------------------------------
    # Validate recommendation
    # --------------------------------------------------------

    if not recommendation:

        raise HTTPException(
            status_code=400,
            detail="Assessment recommendation is required."
        )

    # --------------------------------------------------------
    # Validate responses
    # --------------------------------------------------------

    if not responses:

        raise HTTPException(
            status_code=400,
            detail="Assessment responses are required."
        )

    # --------------------------------------------------------
    # Validate feature scores
    # --------------------------------------------------------

    if not feature_scores:

        raise HTTPException(
            status_code=400,
            detail="Feature scores are required."
        )

    # ========================================================
    # CREATE ASSESSMENT
    # ========================================================

    assessment = Assessment(
        user_id=user_id,
        stage=stage,
        recommendation=recommendation
    )

    db.add(assessment)

    db.commit()

    db.refresh(assessment)

    # ========================================================
    # SAVE QUESTION RESPONSES
    # ========================================================

    for question_id, score in responses.items():

        response = AssessmentResponse(
            assessment_id=assessment.id,
            question_id=int(question_id),
            score=int(score)
        )

        db.add(response)

    # ========================================================
    # SAVE FEATURE SCORES
    # ========================================================

    for feature_name, score in feature_scores.items():

        feature_score = FeatureScore(
            assessment_id=assessment.id,
            feature_name=feature_name,
            score=float(score)
        )

        db.add(feature_score)

    # --------------------------------------------------------
    # Save everything
    # --------------------------------------------------------

    db.commit()

    # ========================================================
    # RESPONSE
    # ========================================================

    return {
        "message": "Assessment saved successfully.",
        "assessment_id": assessment.id,
        "user_id": user_id,
        "stage": stage,
        "recommendation": recommendation
    }


# ============================================================
# GET ASSESSMENT HISTORY
# ============================================================

@router.get("/history")
def get_assessment_history(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Current authenticated user
    # --------------------------------------------------------

    user_id = current_user["id"]

    # --------------------------------------------------------
    # Get only this user's assessments
    # --------------------------------------------------------

    assessments = (
        db.query(Assessment)
        .filter(
            Assessment.user_id == user_id
        )
        .order_by(
            Assessment.completed_at.desc()
        )
        .all()
    )

    # ========================================================
    # RETURN HISTORY
    # ========================================================

    return {
        "user_id": user_id,

        "total_assessments": len(
            assessments
        ),

        "assessments": [
            {
                "id": assessment.id,
                "stage": assessment.stage,
                "recommendation": assessment.recommendation,
                "completed_at": assessment.completed_at
            }

            for assessment in assessments
        ]
    }