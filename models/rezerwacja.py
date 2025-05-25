"""from .ClassDodatki import Dodatki
from .ClassKlient import Klient
from .ClassWariant import Wariant
from pydantic import BaseModel, Field
from typing import List
from datetime import date

class Rezerwacja(BaseModel):

    klient: Klient
    dodatki: List[Dodatki]
    wariant: Wariant
    data_zakupu: date = Field(default_factory=date.today())

    def __str__(self):
        return (f"{self.klient}\nDodatki: {self.dodatki}\nWariant: {self.wariant}\nData: {self.data_zakupu}")
"""