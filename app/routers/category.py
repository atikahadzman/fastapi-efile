import logging
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services import category_service
from app.dependencies import get_db

router = APIRouter(prefix="/category", tags=["category"])

# get all category
@router.get("", response_model=list[CategoryResponse])
def get_all_category(db: Session = Depends(get_db)):
    return category_service.fetch_all_category(db)


# get category by categoryID
@router.get("/{categoryID}", response_model=CategoryResponse)
def get_category_by_id(
    categoryID: str,
    db: Session = Depends(get_db)
):
    category_record = category_service.fetch_category_by_id(db, categoryID)

    if category_record is None:
        raise HTTPException(
            status_code=404,
            detail="category record not found"
        )

    return category_record


# save category records
@router.post("/", response_model=CategoryCreate)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)


# update category
@router.put("/{categoryID}", response_model=CategoryResponse)
def update_category(
    categoryID: int,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db)
):
    try:
        category = category_service.update_category(
            db, categoryID, category_data
        )

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="category record not found"
            )

        return category

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="category update failed due to a duplicate or invalid database value"
        )


# delete category 
@router.delete("/{categoryID}")
def delete_category(
    categoryID: int,
    db: Session = Depends(get_db)
):
    category = category_service.delete_category(db, categoryID)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="category record not found"
        )

    return {
        "message": "category deleted successfully",
        "categoryID": categoryID
    }
