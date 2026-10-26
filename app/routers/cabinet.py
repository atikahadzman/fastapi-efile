import logging
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.schemas.cabinet import CabinetCreate, CabinetUpdate, CabinetResponse
from app.services import cabinet_service
from app.dependencies import get_db

router = APIRouter(prefix="/cabinet", tags=["cabinet"])

# get all cabinet
@router.get("", response_model=list[CabinetResponse])
def get_all_cabinet(db: Session = Depends(get_db)):
    return cabinet_service.fetch_all_cabinet(db)


# get cabinet by cabinetid
@router.get("/{cabinetid}", response_model=CabinetResponse)
def get_cabinet_by_id(
    cabinetid: str,
    db: Session = Depends(get_db)
):
    cabinet_record = cabinet_service.fetch_cabinet_by_id(db, cabinetid)

    if cabinet_record is None:
        raise HTTPException(
            status_code=404,
            detail="Cabinet record not found"
        )

    return cabinet_record


# save cabinet records
@router.post("/", response_model=CabinetCreate)
def create_cabinet(cabinet: CabinetCreate, db: Session = Depends(get_db)):
    return create_cabinet(db, cabinet)


# update cabinet
@router.put("/{cabinetid}", response_model=CabinetResponse)
def update_cabinet(
    cabinetid: int,
    cabinet_data: CabinetUpdate,
    db: Session = Depends(get_db)
):
    try:
        cabinet = cabinet.update_cabinet(
            db, cabinetid, cabinet_data
        )

        if cabinet is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cabinet record not found"
            )

        return cabinet

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cabinet update failed due to a duplicate or invalid database value"
        )


# delete cabinet 
@router.delete("/{cabinetid}")
def delete_cabinet(
    cabinetid: int,
    db: Session = Depends(get_db)
):
    cabinet = cabinet.delete_cabinet(db, cabinetid)

    if cabinet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cabinet record not found"
        )

    return {
        "message": "Cabinet deleted successfully",
        "cabinet id": cabinetid
    }
