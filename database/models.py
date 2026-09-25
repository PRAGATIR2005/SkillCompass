from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database.database import Base


# ============================================================
# USER
# ============================================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    date_of_birth = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    stage = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # --------------------------------------------------------
    # Relationships
    # --------------------------------------------------------

    assessments = relationship(
        "Assessment",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    login_history = relationship(
        "LoginHistory",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# ============================================================
# LOGIN HISTORY
# ============================================================

class LoginHistory(Base):

    __tablename__ = "login_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    login_time = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="login_history"
    )


# ============================================================
# ASSESSMENT
# ============================================================

class Assessment(Base):

    __tablename__ = "assessments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    stage = Column(
        String,
        nullable=False
    )

    recommendation = Column(
        String,
        nullable=True
    )

    completed_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # --------------------------------------------------------
    # Relationships
    # --------------------------------------------------------

    user = relationship(
        "User",
        back_populates="assessments"
    )

    responses = relationship(
        "AssessmentResponse",
        back_populates="assessment",
        cascade="all, delete-orphan"
    )

    feature_scores = relationship(
        "FeatureScore",
        back_populates="assessment",
        cascade="all, delete-orphan"
    )


# ============================================================
# ASSESSMENT RESPONSE
# ============================================================

class AssessmentResponse(Base):

    __tablename__ = "assessment_responses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False,
        index=True
    )

    question_id = Column(
        Integer,
        nullable=False
    )

    score = Column(
        Integer,
        nullable=False
    )

    assessment = relationship(
        "Assessment",
        back_populates="responses"
    )


# ============================================================
# FEATURE SCORE
# ============================================================

class FeatureScore(Base):

    __tablename__ = "feature_scores"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False,
        index=True
    )

    feature_name = Column(
        String,
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    assessment = relationship(
        "Assessment",
        back_populates="feature_scores"
    )