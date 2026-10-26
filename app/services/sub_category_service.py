from sqlalchemy.orm import Session
from app.models.sub_category import SubCategory
from app.models.category import Category
from app.schemas.sub_category import SubCategoryCreate, SubCategoryUpdate

def fetch_all_sub_category(db: Session):
    return db.query(SubCategory).all()


def fetch_sub_category_by_id(db: Session, subid: int):
    return (
        db.query(SubCategory)
        .filter(SubCategory.subid == subid)
        .first()
    )


def create_sub_category(
        db: Session, 
        sub_data: SubCategoryCreate
    ):
    data = sub_data.model_dump()

    sub_category = sub_category(
        subName=data["subName"],
        categoryID=data["categoryID"],
    )

    db.add(sub_category)
    db.commit()
    db.refresh(sub_category)
    return sub_category


def update_sub_category(
    db: Session,
    subid: int,
    sub_data: SubCategoryUpdate
):
    sub_category = fetch_sub_category_by_id(db, subid)

    if sub_category is None:
        raise ValueError("The sub category does not exist")

    category = db.query(Category).filter(
        Category.categoryID == sub_data.categoryID
    ).first()

    if category is None:
        raise ValueError("The category does not exist")

    update_data = sub_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(sub_category, field, value)

    db.commit()
    db.refresh(sub_category)

    return sub_category



def delete_sub_category(db: Session, subid: int):
    sub_category = fetch_sub_category_by_id(db, subid)

    if sub_category is None:
        raise ValueError("The sub category does not exist")

    db.delete(sub_category)
    db.commit()

    return sub_category