from .ClassDodatki import Dodatki
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class Wariant(BaseModel):
    termin: datetime
    koszt: int
    ilosc_miejsc: int
    lista_dodatkow: List[Dodatki] = Field(default_factory=[])
    opis: str