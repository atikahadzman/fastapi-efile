from pydantic import BaseModel, ConfigDict
from datetime import date

class TransactionCreate(BaseModel):
    transID: int
    staffId: str
    categoryID: str
    cabinetid: int
    levelid: int
    fileNo: str
    fileDateTaken: date
    fileDateReturn: date
    fileTransStatus: date
    subid: int


class TransactionUpdate(BaseModel):
    staffId: str | None = None
    categoryID: str | None = None
    cabinetid: int | None = None
    levelid: int | None = None
    fileNo: str | None = None
    fileDateIn: date | None = None
    fileDateTaken: date | None = None
    fileDateReturn: date | None = None
    subid: int | None = None
    

class TransactionResponse(BaseModel):
    transID: int
    staffId: str
    categoryID: str
    cabinetid: int
    levelid: int
    fileNo: str
    fileDateIn: date | None = None
    fileDateTaken: date | None = None
    fileDateReturn: date | None = None
    subid: int

    model_config = ConfigDict(from_attributes=True)