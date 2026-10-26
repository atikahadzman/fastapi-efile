from pydantic import BaseModel, ConfigDict

class SubCategoryCreate(BaseModel):
    subid: int
    subName: str
    categoryID: str


class SubCategoryUpdate(BaseModel):
    subName: str | None = None
    categoryID: str | None = None
    

class SubCategoryResponse(BaseModel):
    subid: int
    subName: str
    categoryID: str

    model_config = ConfigDict(from_attributes=True)