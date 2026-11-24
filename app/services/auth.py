import logging
from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.models.staff import Staff
from app.core.security import (
    verify_password,
    create_access_token
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("db_logger")

def authenticate_user(
    db: Session,
    username: str,
    password: str
):

    # check admin table
    admin = db.query(Admin).filter(
        Admin.adminUsername == username
    ).first()

    if admin:
        if verify_password(
            password,
            admin.adminPassword
        ):

            token = create_access_token({
                "sub": str(admin.adminId),
                "role": "admin"
            })
            
            return {
                "access_token": token,
                "id": admin.adminId,
                "username": username,
                "name": admin.adminName,
                "unit": admin.adminUnit,
                "role": 'Admin'
            }

        return None

    # check staff table
    staff = db.query(Staff).filter(
        Staff.staffUsername == username
    ).first()

    if staff:
        if verify_password(
            password,
            staff.hashed_password
        ):

            token = create_access_token({
                "sub": str(staff.staffId),
                "role": "staff"
            })

            return {
                "access_token": token,
                "id": staff.staffId,
                "username": username,
                "name": staff.staffName,
                "unit": staff.staffUnit,
                "role": 'Staff'
            }

    return None

