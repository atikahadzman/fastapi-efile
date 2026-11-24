from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    id: int
    username: str
    name: str
    unit: str
    role: str


class CurrentUserResponse(BaseModel):
    id: int
    username: str
    role: str
