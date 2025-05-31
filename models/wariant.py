from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base


class Wariant(Base):
    __tablename__ = "warianty"

    id = Column(Integer, primary_key=True, autoincrement=True)
    termin = Column(Date, nullable=False)
    koszt = Column(Integer, nullable=False)
    ilosc_miejsc = Column(Integer, nullable=False)
    opis = Column(String(255), nullable=True)

    # ARRAY typu Integer – lista ID dodatków
    lista_dodatkow = Column(ARRAY(Integer), nullable=True) # wstepnie IDDodatku by bylo


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