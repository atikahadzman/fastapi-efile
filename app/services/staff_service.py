from sqlalchemy.orm import Session
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate
from app.core.security import hash_password


def fetch_all_staff(db: Session):
    return db.query(Staff).all()


def fetch_staff_by_id(db: Session, staffId: int):
    return (
        db.query(Staff)
        .filter(Staff.staffId == staffId)
        .first()
    )


def create_staff(db: Session, staff_data: StaffCreate):
    data = staff_data.model_dump()
    hashed_password = hash_password(data.pop("staffPassword"))

    staff = Staff(
        staffName=data["staffName"],
        staffUsername=data["staffUsername"],
        staffContactNo=data["staffContactNo"],
        staffUnit=data["staffUnit"],
        staffPassword=hashed_password
    )

    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff


def update_staff(
    db: Session,
    staffId: int,
    staff_data: StaffUpdate
):
    staff = fetch_staff_by_id(db, staffId)

    if staff is None:
        raise ValueError("The staff does not exist")

    update_data = staff_data.model_dump(exclude_unset=True)

    if update_data.get("staffPassword"):
        update_data["staffPassword"] = hash_password(
            update_data["staffPassword"]
        )

    for field, value in update_data.items():
        setattr(staff, field, value)

    db.commit()
    db.refresh(staff)

    return staff


def delete_staff(db: Session, staffId: int):
    staff = fetch_staff_by_id(db, staffId)

    if staff is None:
        raise ValueError("The staff does not exist")

    db.delete(staff)
    db.commit()

    return staff