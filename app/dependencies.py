from sqlalchemy.orm import Session
from app.db.database import SessionLocal

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import get_db

from app.models.admin import Admin
from app.models.staff import Staff

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = payload.get("sub")
        role = payload.get("role")

        if not user_id or role not in ["admin", "staff"]:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    # Retrieve admin
    if role == "admin":
        user = db.query(Admin).filter(
            Admin.adminId == int(user_id)
        ).first()

    # Retrieve staff
    else:
        user = db.query(Staff).filter(
            Staff.staffId == int(user_id)
        ).first()

    if user is None:
        raise credentials_exception

    return {
        "user": user,
        "role": role
    }

def require_role(*allowed_roles):

    def role_checker(
        current_user=Depends(get_current_user)
    ):

        if current_user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission"
            )

        return current_user

    return role_checker
