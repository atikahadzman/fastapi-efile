from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


def fetch_all_category(db: Session):
    return db.query(Category).all()


def fetch_category_by_id(db: Session, categoryID: int):
    return (
        db.query(Category)
        .filter(Category.categoryID == categoryID)
        .first()
    )


def create_category(db: Session, category_data: CategoryCreate):
    data = category_data.model_dump()

    category = category(
        categoryID=data["categoryID"],
        categoryName=data["categoryName"],
    )

    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_category(
    db: Session,
    categoryID: int,
    category_data: CategoryUpdate
):
    category = fetch_category_by_id(db, categoryID)

    if category is None:
        raise ValueError("The category does not exist")

    update_data = category_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(category, field, value)

    db.commit()
    db.refresh(category)

    return category


def delete_category(db: Session, categoryID: int):
    category = fetch_category_by_id(db, categoryID)

    if category is None:
        raise ValueError("The category does not exist")

    db.delete(category)
    db.commit()

    return category