from pydantic import BaseModel, ConfigDict

class LevelCreate(BaseModel):
    levelid: int
    levelNo: int
    levelDesc: str
    categoryID: str
    cabinetid: int
    subid: int


class LevelUpdate(BaseModel):
    levelNo: int | None = None
    levelDesc: str | None = None
    categoryID: str | None = None
    cabinetid: int | None = None
    subid: int | None = None
    

class LevelResponse(BaseModel):
    levelid: int
    levelNo: int
    levelDesc: str
    categoryID: str
    cabinetid: int
    subid: int

    model_config = ConfigDict(from_attributes=True)