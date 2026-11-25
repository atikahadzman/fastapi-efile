from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Union

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
    categoryName: str
    cabinetid: int
    cabinetNo: str
    levelid: int
    levelNo: Union[int, str]
    levelDesc: Union[str, int]
    subid: int
    subName: str
    fileStatus: str
    fileStat: str

    model_config = ConfigDict(from_attributes=True)