from pydantic import BaseModel, EmailStr, validator

class KlientCreate(BaseModel):
    imie: str
    nazwisko: str
    email: EmailStr

class KlientOut(BaseModel):
    id = int