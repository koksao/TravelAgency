from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    date_of_birth: date
    id_series: str
    id_number: str

    class Config:
        from_attributes = True


class UserGet(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    date_of_birth: date
    id_series: str
    id_number: str

    class Config:
        from_attributes = True