from pydantic import BaseModel, EmailStr

class Klient(BaseModel):
    """
    Klasa Klient
        Atrybuty:
            -imie str
            -nazwisko str
            -email
        Metody:
    """

    imie: str
    nazwisko: str
    email: EmailStr

    def __str__(self):
        return f"Klient: {self.imie} {self.nazwisko} {self.email}"