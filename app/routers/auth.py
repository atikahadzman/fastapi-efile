from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.auth import authenticate_user
from app.dependencies import get_current_user
from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    token = authenticate_user(
        db,
        credentials.username,
        credentials.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/")
def profile(
    current_user=Depends(get_current_user)
):

    user = current_user["user"]

    return {
        "id": user.id,
        "username": user.username,
        "role": current_user["role"]
    }