from sqlalchemy.orm import Session
from app.models.cabinet import Cabinet
from app.models.category import Category
from app.models.file import File
from app.models.level import Level
from app.models.sub_category import SubCategory
from app.schemas.file import FileCreate, FileUpdate

def fetch_all_file(db: Session):
    return db.query(File).all()


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
