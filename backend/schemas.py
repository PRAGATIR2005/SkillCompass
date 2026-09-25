from pydantic import BaseModel, EmailStr


# ============================================================
# USER REGISTRATION
# ============================================================

class UserRegister(BaseModel):

    name: str

    age: int

    date_of_birth: str

    email: EmailStr

    password: str

    stage: str


# ============================================================
# USER LOGIN
# ============================================================

class UserLogin(BaseModel):

    email: EmailStr

    password: str