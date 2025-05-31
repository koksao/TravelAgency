from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base
from datetime import date

class Rezerwacja(Base):
    __tablename__ = "rezerwacje"

    id = Column(Integer, primary_key=True, autoincrement=True)

    klient_id = Column(Integer, ForeignKey("klienci.id"), nullable=False)
    wariant_id = Column(Integer, ForeignKey("warianty.id"), nullable=False)

    dodatki_ids = Column(ARRAY(Integer), nullable=True)  # tez iddodatku

    data_zakupu = Column(Date, default=date.today, nullable=False)


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