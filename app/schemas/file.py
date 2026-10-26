from pydantic import BaseModel, ConfigDict
from datetime import date

class FileCreate(BaseModel):
    fileNo: str
    fileName: str
    fileDateIn: date
    categoryID: str
    cabinetid: int
    levelid: int
    subid: int
    fileStatus: str
    fileStat: str


class FileUpdate(BaseModel):
    fileName: str | None = None
    fileDateIn: date | None = None
    categoryID: str | None = None
    cabinetid: int | None = None
    levelid: int | None = None
    subid: int | None = None
    fileStatus: str | None = None
    fileStat: str | None = None
    

class FileResponse(BaseModel):
    fileNo: str
    fileName: str
    fileDateIn: date
    categoryID: str
    cabinetid: int
    levelid: int
    subid: int
    fileStatus: str
    fileStat: str

    model_config = ConfigDict(from_attributes=True)