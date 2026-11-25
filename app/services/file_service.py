import math
from sqlalchemy.orm import Session
from app.models.cabinet import Cabinet
from app.models.category import Category
from app.models.file import File
from app.models.level import Level
from app.models.sub_category import SubCategory
from app.schemas.file import FileCreate, FileUpdate

def fetch_all_file(
        db: Session,
        page: int = 1,
        page_size: int = 10
    ):
        page = max(page, 1)
        page_size = max(page_size, 1)
        offset = (page - 1) * page_size
        total_records = db.query(File).count()

        files = (
            db.query(
                File,
                Category.categoryName.label("categoryName"),
                SubCategory.subName.label("subName"),
                Cabinet.cabinetNo.label("cabinetNo"),
                Level.levelNo.label("levelNo"),
                Level.levelDesc.label("levelDesc")
            )
            .outerjoin(
                Category,
                File.categoryID == Category.categoryID
            )
            .outerjoin(
                SubCategory,
                File.subid == SubCategory.subid
            )
            .outerjoin(
                Cabinet,
                File.cabinetid == Cabinet.cabinetid
            )
            .outerjoin(
                Level,
                File.levelid == Level.levelid
            )
            .order_by(File.fileDateIn)
            .offset(offset)
            .limit(page_size)
            .all()
        )

        result = [
            {
                "fileNo": f.fileNo,
                "fileName": f.fileName,
                "fileDateIn": f.fileDateIn,
                "categoryID": f.categoryID,
                "categoryName": categoryName,
                "cabinetid": f.cabinetid,
                "cabinetNo": cabinetNo,
                "levelid": f.levelid,
                "levelNo": levelNo,
                "levelDesc": levelDesc,
                "subid": f.subid,
                "subName": subName,
                "fileStatus": f.fileStatus,
                "fileStat": f.fileStat
            }
            for f, categoryName, cabinetNo, levelNo, levelDesc, subName in files
        ]

        total_pages = math.ceil(total_records / page_size)
        
        return {
            "data": result,
            "pagination": {
                "current_page": page,
                "page_size": page_size,
                "total_records": total_records,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_previous": page > 1
            }
        }


def fetch_file_by_id(db: Session, fileNo: str):
    return (
        db.query(File)
        .filter(File.fileNo == fileNo)
        .first()
    )


def create_file(
        db: Session, 
        file_data: FileCreate
    ):
    data = file_data.model_dump()

    file = file(
        fileNo = data["fileNo"],
        fileName = data["fileName"],
        fileDateIn = data["fileDateIn"],
        categoryID = data["categoryID"],
        cabinetid = data["cabinetid"],
        levelid = data["levelid"],
        subid = data["subid"],
        fileStatus = data["fileStatus"],
        fileStat = data["fileStat"],
    )

    db.add(file)
    db.commit()
    db.refresh(file)
    return file


def update_file(
    db: Session,
    fileNo: int,
    data: FileUpdate
):
    file = fetch_file_by_id(db, fileNo)

    if file is None:
        raise ValueError("The file does not exist")

    category = db.query(Category).filter(
        Category.categoryID == data.categoryID
    ).first()

    if category is None:
        raise ValueError("The category does not exist")

    sub_category = db.query(SubCategory).filter(
        SubCategory.subid == data.subid
    ).first()

    if sub_category is None:
        raise ValueError("The sub category does not exist")
		
    cabinet = db.query(Cabinet).filter(
        cabinet.cabinetid == data.cabinetid
    ).first()

    if cabinet is None:
        raise ValueError("The cabinet does not exist")

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(file, field, value)

    db.commit()
    db.refresh(file)

    return file


def delete_file(db: Session, fileNo: str):
    file = fetch_file_by_id(db, fileNo)

    if file is None:
        raise ValueError("The file does not exist")

    db.delete(file)
    db.commit()

    return file
