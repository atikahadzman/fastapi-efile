import logging
import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.database import get_db
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionResponse
from app.services import transaction_service
from app.dependencies import get_db

router = APIRouter(prefix="/transaction", tags=["transaction"])

# get all transaction
@router.get("", response_model=list[TransactionResponse])
def get_all_transaction(db: Session = Depends(get_db)):
    return transaction_service.fetch_all_transaction(db)


# get transaction by transID
@router.get("/{transID}")
def get_transaction_by_id(
    transID: int,
    db: Session = Depends(get_db)
):
    transaction_record = transaction_service.fetch_transaction_by_id(db, transID)

    if transaction_record is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction record not found"
        )

    return transaction_record


# save transaction records
@router.post("/", response_model=TransactionCreate)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, transaction)


# update transaction
@router.put("/{transID}", response_model=TransactionResponse)
def update_transaction(
    transID: str,
    trans_data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    try:
        transaction = transaction.update_transaction(
            db, transID, trans_data
        )

        if transaction is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction record not found"
            )

        return transaction

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Transaction update failed due to a duplicate or invalid database value"
        )


# delete transaction 
@router.delete("/{transID}")
def delete_transaction(
    transID: str,
    db: Session = Depends(get_db)
):
    transaction = transaction.delete_transaction(db, transID)

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction record not found"
        )

    return {
        "message": "Transaction deleted successfully",
        "transaction id": transID
    }

