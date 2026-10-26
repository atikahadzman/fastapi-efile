from sqlalchemy.orm import Session
from app.models.category import Category
from app.models.cabinet import Cabinet
from app.models.sub_category import SubCategory
from app.schemas.cabinet import CabinetCreate, CabinetUpdate

def fetch_all_cabinet(db: Session):
    return db.query(Cabinet).all()


def fetch_cabinet_by_id(db: Session, cabinetid: int):
    return (
        db.query(Cabinet)
        .filter(Cabinet.cabinetid == cabinetid)
        .first()
    )


def create_cabinet(
        db: Session, 
        cabinet_data: CabinetCreate
    ):
    data = cabinet_data.model_dump()

    cabinet = cabinet(
        cabinetNo = data["cabinetNo"],
        cabinetDesc = data["cabinetDesc"],
        categoryID = data["categoryID"],
        subid = data["subid"],
    )

    db.add(cabinet)
    db.commit()
    db.refresh(cabinet)
    return cabinet


def update_cabinet(
    db: Session,
    cabinetid: int,
    data: CabinetUpdate
):
    cabinet = fetch_cabinet_by_id(db, cabinetid)

    if cabinet is None:
        raise ValueError("The cabinet does not exist")

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

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(cabinet, field, value)

    db.commit()
    db.refresh(cabinet)

    return cabinet



def delete_cabinet(db: Session, cabinetid: int):
    cabinet = fetch_cabinet_by_id(db, cabinetid)

    if cabinet is None:
        raise ValueError("The cabinet does not exist")

    db.delete(cabinet)
    db.commit()

    return cabinet