from .ClassDodatki import Dodatki
from pydantic import BaseModel, Field
from datetime import date
from typing import List

class Wariant(BaseModel):
    """
    Klasa Wariant
        Atrybuty:
            -termin: datetime
            -koszt: int
            -ilosc_miejsc: int
            -lista_dodatkow: lista obiektów, domyślnie lista
            -opis: str
    """
    termin: date
    koszt: int
    ilosc_miejsc: int
    lista_dodatkow: List[Dodatki] = Field(default_factory=[])
    opis: str