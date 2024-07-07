from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    # id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "johndoe@gmail.com",
                "password": "12345",
                "is_staff": False,
                "is_active": True,
            }
        }

    class Settings(BaseModel):
        authjwt_secret_key: str = "bb33304041283a38101af340f90c56e6d45ac20d690bbe2307fae12176abd96b"

    class LoginModel(BaseModel):
        email: str
        password: str
