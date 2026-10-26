from sqlalchemy.orm import Session
from app.models.category import Category
from app.models.cabinet import Cabinet
from app.models.sub_category import SubCategory
from app.models.level import Level
from app.schemas.level import LevelCreate, LevelUpdate

def fetch_all_level(db: Session):
    return db.query(Level).all()


def fetch_level_by_id(db: Session, levelid: int):
    return (
        db.query(Level)
        .filter(Level.levelid == levelid)
        .first()
    )


def create_level(
        db: Session, 
        level_data: LevelCreate
    ):
    data = level_data.model_dump()

    level = level(
        levelNo = data["levelNo"],
        levelDesc = data["levelDesc"],
        categoryID = data["categoryID"],
        cabinetid = data["cabinetid"],
        subid = data["subid"],
    )

    db.add(level)
    db.commit()
    db.refresh(level)
    return level


def update_level(
    db: Session,
    levelid: int,
    data: LevelUpdate
):
    level = fetch_level_by_id(db, levelid)

    if level is None:
        raise ValueError("The level does not exist")

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
        setattr(level, field, value)

    db.commit()
    db.refresh(level)

    return level


def delete_level(db: Session, levelid: int):
    level = fetch_level_by_id(db, levelid)

    if level is None:
        raise ValueError("The level does not exist")

    db.delete(level)
    db.commit()

    return level