from sqlalchemy import Column, Integer, String
from app.db.database import Base
from datetime import datetime


class Transaction(Base):
    __tablename__ = "transaction"

    transID = Column(Integer, primary_key=True, nullable=False)
    staffId = Column(String(12), unique=False, nullable=False)
    categoryID = Column(String(30), unique=False, nullable=False)
    cabinetid = Column(Integer, unique=False, index=True)
    levelid = Column(Integer, unique=False, index=True)
    fileNo = Column(String(30), unique=False, nullable=False)
    fileDateIn = Column(datetime.now(), unique=False, nullable=False)
    fileDateTaken = Column(datetime.now(), unique=False, nullable=False)
    fileDateReturn = Column(datetime.now(), unique=False, nullable=False)
    fileTransStatus = Column(String(30), unique=False, nullable=False)
    subid = Column(Integer, unique=False, index=True)
