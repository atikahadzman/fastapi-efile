from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Level(Base):
    __tablename__ = "level"

    levelid = Column(Integer, primary_key=True, index=True)
    levelNo = Column(Integer, unique=True, index=True)
    levelDesc = Column(String(50), unique=False, nullable=False)
    categoryID = Column(String(30), unique=False, nullable=False)
    cabinetid = Column(Integer, unique=False, index=True)
    subid = Column(Integer, unique=False, index=True)
