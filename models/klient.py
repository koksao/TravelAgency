from sqlalchemy import Column, Integer, String, Date
from database import Base

class Klient(Base):
    __tablename__ = "klienci"

    id = Column(Integer, primary_key=True, index=True)
    imie = Column(String, nullable=False)
    nazwisko = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    data_dodania = Column(Date, nullable=True)
