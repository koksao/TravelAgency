from sqlalchemy import Column, Integer, String, Date
from database import Base  # zakładam, że masz plik database.py z deklaracją Base

class Dodatek(Base):
    __tablename__ = "dodatki"

    id = Column(Integer, primary_key=True, index=True)
    tytul = Column(String, nullable=False)
    termin = Column(Date, nullable=False)
    koszt = Column(Integer, nullable=False)
    liczba_miejsc = Column(Integer, nullable=False)
    opis = Column(String, nullable=True)
