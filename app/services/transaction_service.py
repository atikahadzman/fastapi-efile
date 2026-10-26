from sqlalchemy.orm import Session
from app.models.cabinet import Cabinet
from app.models.category import Category
from app.models.file import File
from app.models.level import Level
from app.models.sub_category import SubCategory
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate

def fetch_all_transaction(db: Session):
    return db.query(Transaction).all()


def fetch_transaction_by_id(db: Session, transID: int):
    return (
        db.query(Transaction)
        .filter(Transaction.transID == transID)
        .first()
    )


def create_transaction(
        db: Session, 
        transaction_data: TransactionCreate
    ):
    data = transaction_data.model_dump()

    transaction = transaction(
        staffIC = data["staffIC"],
        categoryID = data["categoryID"],
        cabinetid = data["cabinetid"],
        levelid = data["levelid"],
        fileNo = data["fileNo"],
        fileDateTaken = data["fileDateTaken"],
        fileDateReturn = data["fileDateReturn"],
        fileTransStatus = data["fileTransStatus"],
        subid = data["subid"],
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


def update_transaction(
    db: Session,
    transID: int,
    data: TransactionUpdate
):
    transaction = fetch_transaction_by_id(db, transID)

    if transaction is None:
        raise ValueError("The transaction does not exist")

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
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)

    return transaction


def delete_transaction(db: Session, transID: int):
    transaction = fetch_transaction_by_id(db, transID)

    if transaction is None:
        raise ValueError("The transaction does not exist")

    db.delete(transaction)
    db.commit()

    return transaction