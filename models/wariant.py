"""from .ClassDodatki import Dodatki
from pydantic import BaseModel, Field
from datetime import date
from typing import List

class Wariant(BaseModel):
    termin: date
    koszt: int
    ilosc_miejsc: int
    lista_dodatkow: List[Dodatki] = Field(default_factory=[])
    opis: str"""