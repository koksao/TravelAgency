from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base

class Wycieczka(Base):
    __tablename__ = "wycieczki"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tytul = Column(String(255), nullable=False)
    organizator = Column(String(255), nullable=False)
    lokalizacja = Column(String(255), nullable=False)

    warianty = Column(ARRAY(Integer), nullable=True) # tu tez array z IDWariantow


"""from .ClassWariant import Wariant
from pydantic import BaseModel
from typing import List

class Wycieczka(BaseModel):

    tytul: str
    organizator: str
    lokalizacja: str
    warianty: List[Wariant]"""