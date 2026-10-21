import logging
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.schemas.staff import StaffCreate, StaffUpdate, StaffResponse
from app.services import staff_service
from app.dependencies import get_db

router = APIRouter(prefix="/staff", tags=["staff"])


# get all staff
@router.get("", response_model=list[StaffResponse])
def get_all_staffs(db: Session = Depends(get_db)):
    return staff_service.fetch_all_staff(db)


# get staff by staffId
@router.get("/{staffId}", response_model=StaffResponse)
def get_staff_by_id(
    staffId: int,
    db: Session = Depends(get_db)
):
    staff_record = staff_service.fetch_staff_by_id(db, staffId)

    if staff_record is None:
        raise HTTPException(
            status_code=404,
            detail="staff record not found"
        )

    return staff_record


# save staff records
@router.post("/", response_model=StaffCreate)
def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    return create_staff(db, staff)


# update staff
@router.put("/{staffId}", response_model=StaffResponse)
def update_staff(
    staffId: int,
    staff_data: StaffUpdate,
    db: Session = Depends(get_db)
):
    try:
        staff = staff_service.update_staff(
            db, staffId, staff_data
        )

        if staff is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="staff record not found"
            )

        return staff

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="staff update failed due to a duplicate or invalid database value"
        )


# delete staff 
@router.delete("/{staffId}")
def delete_staff(
    staffId: int,
    db: Session = Depends(get_db)
):
    staff = staff_service.delete_staff(db, staffId)

    if staff is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff record not found"
        )

    return {
        "message": "Staff deleted successfully",
        "staffId": staffId
    }
