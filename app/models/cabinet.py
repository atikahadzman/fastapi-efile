from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Cabinet(Base):
    __tablename__ = "cabinet"

    cabinetid = Column(Integer, primary_key=True, index=True)
    cabinetNo = Column(String(30), unique=True, nullable=False)
    cabinetDesc = Column(String(50), unique=False, nullable=False)
    categoryID = Column(String(30), unique=False, nullable=False)
    subid = Column(Integer, unique=False, index=True)
