import logging
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.schemas.sub_category import SubCategoryCreate, SubCategoryUpdate, SubCategoryResponse
from app.services import sub_category_service
from app.dependencies import get_db

router = APIRouter(prefix="/sub-category", tags=["sub-category"])

# get all category
@router.get("", response_model=list[SubCategoryResponse])
def get_all_sub_category(db: Session = Depends(get_db)):
    return sub_category_service.fetch_all_sub_category(db)


# get category by subid
@router.get("/{subid}", response_model=SubCategoryResponse)
def get_sub_category_by_id(
    subid: str,
    db: Session = Depends(get_db)
):
    sub_category_record = sub_category_service.fetch_sub_category_by_id(db, subid)

    if sub_category_record is None:
        raise HTTPException(
            status_code=404,
            detail="sub category record not found"
        )

    return sub_category_record


# save category records
@router.post("/", response_model=SubCategoryCreate)
def create_sub_category(sub_category: SubCategoryCreate, db: Session = Depends(get_db)):
    return create_sub_category(db, sub_category)


# update category
@router.put("/{subid}", response_model=SubCategoryResponse)
def update_category(
    subid: int,
    sub_category_data: SubCategoryUpdate,
    db: Session = Depends(get_db)
):
    try:
        sub_category = sub_category_service.update_sub_category(
            db, subid, sub_category_data
        )

        if sub_category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="category record not found"
            )

        return sub_category

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Sub category update failed due to a duplicate or invalid database value"
        )


# delete category 
@router.delete("/{subid}")
def delete_sub_category(
    subid: int,
    db: Session = Depends(get_db)
):
    sub_category = sub_category_service.delete_sub_category(db, subid)

    if sub_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sub category record not found"
        )

    return {
        "message": "Sub category deleted successfully",
        "subid": subid
    }
