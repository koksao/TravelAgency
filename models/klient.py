from sqlalchemy import Column, Integer, String
from database import Base

class Klient(Base):
    __tablename__ = "klienci"  # możesz użyć "clients" jeśli wolisz angielski

    id = Column(Integer, primary_key=True, index=True)
    imie = Column(String, nullable=False)
    nazwisko = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

