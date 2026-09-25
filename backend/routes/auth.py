from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User, LoginHistory

from backend.schemas import UserRegister, UserLogin
from backend.auth import hash_password, verify_password
from backend.jwt_config import create_access_token
from backend.dependencies import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ============================================================
# ALLOWED STAGES
# ============================================================

ALLOWED_STAGES = {
    "Stage 1": "Post-10th / School Stream Selection",
    "Stage 2": "Post-12th / Higher Education Selection",
    "Stage 3": "Working Professional / Career Switch",
    "Stage 4": "Postgraduate / Next Career Step"
}


# ============================================================
# REGISTER
# ============================================================

@router.post("/register")
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Check whether email already exists
    # --------------------------------------------------------

    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="An account with this email already exists. Please login instead."
        )

    # --------------------------------------------------------
    # Validate stage
    # --------------------------------------------------------

    if user_data.stage not in ALLOWED_STAGES:
        raise HTTPException(
            status_code=400,
            detail="Invalid stage selected."
        )

    # --------------------------------------------------------
    # Validate age
    # --------------------------------------------------------

    if user_data.age < 10 or user_data.age > 100:
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid age."
        )

    # --------------------------------------------------------
    # Create user
    # --------------------------------------------------------

    new_user = User(
        name=user_data.name,
        age=user_data.age,
        date_of_birth=user_data.date_of_birth,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        stage=user_data.stage
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # --------------------------------------------------------
    # Response
    # --------------------------------------------------------

    return {
        "message": "Registration successful.",
        "user_id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "stage": new_user.stage,
        "stage_name": ALLOWED_STAGES[new_user.stage],
        "is_new_user": True
    }


# ============================================================
# LOGIN
# ============================================================

@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Find user
    # --------------------------------------------------------

    user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    # --------------------------------------------------------
    # Verify password
    # --------------------------------------------------------

    if not verify_password(
        user_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    # --------------------------------------------------------
    # Check previous logins
    # --------------------------------------------------------

    previous_logins = (
        db.query(LoginHistory)
        .filter(LoginHistory.user_id == user.id)
        .count()
    )

    is_first_login = previous_logins == 0

    # --------------------------------------------------------
    # Save login history
    # --------------------------------------------------------

    login_record = LoginHistory(
        user_id=user.id
    )

    db.add(login_record)
    db.commit()

    # --------------------------------------------------------
    # Create JWT
    # --------------------------------------------------------

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "stage": user.stage
        }
    )

    # --------------------------------------------------------
    # Response
    # --------------------------------------------------------

    return {
        "message": "Login successful.",
        "access_token": access_token,
        "token_type": "bearer",

        "user": {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "date_of_birth": user.date_of_birth,
            "email": user.email,
            "stage": user.stage,
            "stage_name": ALLOWED_STAGES.get(
                user.stage,
                user.stage
            )
        },

        "is_first_login": is_first_login,
        "total_logins": previous_logins + 1
    }


# ============================================================
# CURRENT USER
# ============================================================

@router.get("/me")
def get_me(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == current_user["id"])
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return {
        "id": user.id,
        "name": user.name,
        "age": user.age,
        "date_of_birth": user.date_of_birth,
        "email": user.email,
        "stage": user.stage,
        "stage_name": ALLOWED_STAGES.get(
            user.stage,
            user.stage
        )
    }


# ============================================================
# LOGIN HISTORY
# ============================================================

@router.get("/login-history")
def login_history(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    records = (
        db.query(LoginHistory)
        .filter(
            LoginHistory.user_id == current_user["id"]
        )
        .order_by(
            LoginHistory.login_time.desc()
        )
        .all()
    )

    return {
        "user_id": current_user["id"],
        "total_logins": len(records),
        "login_history": [
            {
                "id": record.id,
                "login_time": record.login_time
            }
            for record in records
        ]
    }