from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Staff(Base):
    __tablename__ = "staff"

    staffId = Column(Integer, primary_key=True, index=True)
    staffUsername = Column(String(255), unique=True, nullable=False)
    staffName = Column(String(100), unique=True, nullable=False)
    staffContactNo = Column(String(15), unique=True, nullable=False)
    staffUnit = Column(String(50), unique=False, nullable=False)
    staffPassword = Column(String(255), nullable=False)
