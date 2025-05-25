from pydantic import BaseModel
from datetime import date

class Dodatki(BaseModel):
    """
    Klasa Dodatki
        Atrybuty:
            -tytul: str
            -termin: date
            -koszt: int
            -liczba_miejsc: int
    """

    tytul: str
    termin: date
    koszt: int
    liczba_miejsc: int
