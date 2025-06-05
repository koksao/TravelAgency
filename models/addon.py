from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, Date
from sqlalchemy.orm import relationship
from database import Base

class Addon(Base):
    __tablename__ = "addon"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    cost = Column(Numeric)
    availability = Column(Integer)
    date = Column(Date)

    trip_id = Column(Integer, ForeignKey("trip.id"))
    trip = relationship("Trip", back_populates="addons")
    orders = relationship("OrderAddon", back_populates="addon")