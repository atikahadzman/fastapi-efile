from pydantic import BaseModel, ConfigDict

class CabinetCreate(BaseModel):
    cabinetid: int
    cabinetNo: str
    cabinetDesc: str
    categoryID: str
    subid: int


class CabinetUpdate(BaseModel):
    subName: str | None = None
    cabinetNo: str | None = None
    cabinetDesc: str | None = None
    categoryID: str | None = None
    subid: int | None = None
    

class CabinetResponse(BaseModel):
    cabinetid: int
    cabinetNo: str
    cabinetDesc: str
    categoryID: str
    subid: int

    model_config = ConfigDict(from_attributes=True)