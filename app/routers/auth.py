import logging
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

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("db_logger")


@router.post("/login", response_model=TokenResponse)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        credentials.username,
        credentials.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    return {
        "access_token": user["access_token"],
        "token_type": "bearer",
        "id": user["id"],
        "username": user["username"],
        "name": user["name"],
        "unit": user["unit"],
        "role": user["role"]
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