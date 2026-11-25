from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Union, List

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
    categoryID: Union[str, None] = None
    categoryName: Union[str, None] = None
    cabinetid: Union[int, None] = None
    cabinetNo: Union[str, None] = None
    levelid: Union[int, None] = None
    levelNo: Union[int, str]
    levelDesc: Union[str, int]
    subid: Union[int, None] = None
    subName: Union[str, None] = None
    fileStatus: Union[str, None] = None
    fileStat: Union[str, None] = None

    model_config = ConfigDict(from_attributes=True)

class PaginationResponse(BaseModel):
    current_page: int
    page_size: int
    total_records: int
    total_pages: int
    has_next: bool
    has_previous: bool

class FilePaginationResponse(BaseModel):
    data: List[FileResponse]
    pagination: PaginationResponse