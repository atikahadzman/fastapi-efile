from sqlalchemy import Column, Integer, String
from app.db.database import Base
from sqlalchemy import Column, Date
from datetime import date


class File(Base):
    __tablename__ = "file"

    fileNo = Column(String(30), primary_key=True, nullable=False)
    fileName = Column(String(100), unique=False, nullable=False)
    fileDateIn = Column(
        Date,
        default=date.today,
        nullable=False
    )
    categoryID = Column(String(30), unique=False, nullable=False)
    cabinetid = Column(Integer, unique=False, index=True)
    levelid = Column(Integer, unique=False, index=True)
    subid = Column(Integer, unique=False, index=True)
    fileStatus = Column(String(30), unique=False, nullable=False)
    fileStat = Column(String(30), unique=False, nullable=False)
