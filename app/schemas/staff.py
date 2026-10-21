from pydantic import BaseModel, ConfigDict

class StaffCreate(BaseModel):
    staffName: str
    staffUsername: str
    staffContactNo: str
    staffUnit: str
    staffPassword: str


class StaffUpdate(BaseModel):
    staffName: str | None = None
    staffUsername: str | None = None
    staffContactNo: str | None = None
    staffUnit: str | None = None
    staffPassword: str | None = None
    

class StaffResponse(BaseModel):
    staffId: int
    staffUsername: str
    staffName: str
    staffContactNo: str
    staffUnit: str

    model_config = ConfigDict(from_attributes=True)
