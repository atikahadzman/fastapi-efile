from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Category(Base):
    __tablename__ = "category"

    categoryID = Column(String(30), primary_key=True, index=True)
    categoryName = Column(String(50), unique=True, nullable=False)
