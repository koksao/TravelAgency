from sqlalchemy import Column, Integer, Enum as SqlEnum
from database import Base
from .enum_transport import TypTransportu

class Transport(Base):
    __tablename__ = "transporty"

    id = Column(Integer, primary_key=True, index=True)
    typ = Column(SqlEnum(TypTransportu), nullable=False)
    koszt = Column(Integer, nullable=False)
