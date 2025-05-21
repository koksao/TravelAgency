from pydantic import BaseModel, EmailStr

class Klient(BaseModel):
    imie: str
    nazwisko: str
    email: EmailStr

    def __str__(self):
        return f"Klient {self.imie} {self.nazwisko} {self.email}"