from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Trip(Base):
    __tablename__ = "trip"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    country = Column(String)
    description = Column(String)

    variants = relationship("Variant", back_populates="trip")
    addons = relationship("Addon", back_populates="trip")