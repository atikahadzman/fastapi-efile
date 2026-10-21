from pydantic import BaseModel, ConfigDict

class CategoryCreate(BaseModel):
    categoryID: str
    categoryName: str


class CategoryUpdate(BaseModel):
    categoryID: str | None = None
    categoryName: str | None = None
    

class CategoryResponse(BaseModel):
    categoryID: str
    categoryName: str

    model_config = ConfigDict(from_attributes=True)