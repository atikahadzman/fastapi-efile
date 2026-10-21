from sqlalchemy import Column, Integer, String
from app.db.database import Base


class SubCategory(Base):
    __tablename__ = "sub_category"

    subid = Column(Integer, primary_key=True, index=True)
    subName = Column(String(100), unique=True, nullable=False)
    categoryID = Column(String(30), unique=False, nullable=False)
