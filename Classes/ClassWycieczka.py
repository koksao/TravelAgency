from .ClassWariant import Wariant
from pydantic import BaseModel
from typing import List

class Wycieczka(BaseModel):
    """
    Klasa Wycieczka
        Atrybuty:
            -tytul: str
            -organizator: str
            -lokalizacja: str
            -warianty: Lista Obiektów
    """

    tytul: str
    organizator: str
    lokalizacja: str
    warianty: List[Wariant]