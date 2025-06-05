from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship

from database import Base

class Variant(Base):
    __tablename__ = "variant"

    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey("trip.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    cost = Column(Numeric)
    availability = Column(Integer)

    trip = relationship("Trip", back_populates="variants")
    orders = relationship("Order", back_populates="variant")
    transports = relationship("Transport", back_populates="variant")
