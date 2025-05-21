from pydantic import BaseModel
from datetime import datetime

class Dodatki(BaseModel):
    tytul: str
    termin: datetime
    koszt: int
    liczba_miejsc: int