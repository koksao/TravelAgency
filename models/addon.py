from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, Date
from sqlalchemy.orm import relationship
from database import Base
from schemas.addon import AddonCreate


class Addon(Base):
    __tablename__ = "addon"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    cost = Column(Numeric)
    availability = Column(Integer)
    date = Column(Date)

    trip_id = Column(Integer, ForeignKey("trip.id", ondelete="CASCADE"))
    trip = relationship("Trip", back_populates="addons")
    orders = relationship("OrderAddon", back_populates="addon")

    @classmethod
    def from_create_schema(cls, schema: 'AddonCreate') -> 'Addon':
        return cls(
            description=schema.description,
            cost=schema.cost,
            availability=schema.availability,
            date=schema.date,
            trip_id=schema.trip_id
        )