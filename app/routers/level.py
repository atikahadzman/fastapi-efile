import logging
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.schemas.level import LevelCreate, LevelUpdate, LevelResponse
from app.services import level_service
from app.dependencies import get_db

router = APIRouter(prefix="/level", tags=["level"])

# get all level
@router.get("", response_model=list[LevelResponse])
def get_all_level(db: Session = Depends(get_db)):
    return level_service.fetch_all_level(db)


# get level by levelid
@router.get("/{levelid}", response_model=LevelResponse)
def get_level_by_id(
    levelid: str,
    db: Session = Depends(get_db)
):
    level_record = level_service.fetch_level_by_id(db, levelid)

    if level_record is None:
        raise HTTPException(
            status_code=404,
            detail="Level record not found"
        )

    return level_record


# save level records
@router.post("/", response_model=LevelCreate)
def create_level(level: LevelCreate, db: Session = Depends(get_db)):
    return create_level(db, level)


# update level
@router.put("/{levelid}", response_model=LevelResponse)
def update_level(
    levelid: int,
    level_data: LevelUpdate,
    db: Session = Depends(get_db)
):
    try:
        level = level.update_level(
            db, levelid, level_data
        )

        if level is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Level record not found"
            )

        return level

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Level update failed due to a duplicate or invalid database value"
        )


# delete level 
@router.delete("/{levelid}")
def delete_level(
    levelid: int,
    db: Session = Depends(get_db)
):
    level = level.delete_level(db, levelid)

    if level is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Level record not found"
        )

    return {
        "message": "Level deleted successfully",
        "level id": levelid
    }
