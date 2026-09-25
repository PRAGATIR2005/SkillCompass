from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import JWTError, jwt

from backend.jwt_config import SECRET_KEY, ALGORITHM


# ============================================================
# HTTP BEARER AUTHENTICATION
# ============================================================

security = HTTPBearer()


# ============================================================
# GET CURRENT USER FROM JWT
# ============================================================

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")
        email = payload.get("email")
        stage = payload.get("stage")

        # ----------------------------------------------------
        # Validate required JWT information
        # ----------------------------------------------------

        if (
            user_id is None
            or email is None
            or stage is None
        ):

            raise HTTPException(
                status_code=401,
                detail="Invalid authentication token"
            )

        # ----------------------------------------------------
        # Return authenticated user information
        # ----------------------------------------------------

        return {
            "id": int(user_id),
            "email": email,
            "stage": stage
        }

    except (JWTError, ValueError):

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired authentication token"
        )