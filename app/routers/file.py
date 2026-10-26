import logging
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.schemas.file import FileCreate, FileUpdate, FileResponse
from app.services import file_service
from app.dependencies import get_db

router = APIRouter(prefix="/file", tags=["file"])

# get all file
@router.get("", response_model=list[FileResponse])
def get_all_file(db: Session = Depends(get_db)):
    return file_service.fetch_all_file(db)


# get file by fileNo
@router.get("/{fileNo:path}")
def get_file_by_id(
    fileNo: str,
    db: Session = Depends(get_db)
):
    # print("Received fileNo:", repr(fileNo))
    file_record = file_service.fetch_file_by_id(db, fileNo)

    if file_record is None:
        raise HTTPException(
            status_code=404,
            detail="File record not found"
        )

    return file_record


# save file records
@router.post("/", response_model=FileCreate)
def create_file(file: FileCreate, db: Session = Depends(get_db)):
    return create_file(db, file)


# update file
@router.put("/{fileNo}", response_model=FileResponse)
def update_file(
    fileNo: str,
    file_data: FileUpdate,
    db: Session = Depends(get_db)
):
    try:
        file = file.update_file(
            db, fileNo, file_data
        )

        if file is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="File record not found"
            )

        return file

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="File update failed due to a duplicate or invalid database value"
        )


# delete file 
@router.delete("/{fileNo}")
def delete_file(
    fileNo: str,
    db: Session = Depends(get_db)
):
    file = file.delete_file(db, fileNo)

    if file is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File record not found"
        )

    return {
        "message": "File deleted successfully",
        "file number": fileNo
    }
