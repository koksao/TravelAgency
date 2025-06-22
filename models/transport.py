from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, Date, Enum as SqlEnum
from sqlalchemy.orm import relationship

from database import Base
from models.transport_type import TransportType

class Transport(Base):
    __tablename__ = "transport"

    id = Column(Integer, primary_key=True)
    transport_type = Column(SqlEnum(TransportType))
    place_of_departure = Column(String)
    destination = Column(String)
    date_of_departure = Column(Date)
    date_of_return = Column(Date)
    cost = Column(Numeric)

    variant_id = Column(Integer, ForeignKey("variant.id"))
    variant = relationship("Variant", back_populates="transports")
    orders = relationship("Order", back_populates="transport")

    @classmethod
    def from_create_schema(cls, schema: 'TransportCreate') -> 'Transport':
        return cls(
            transport_type=schema.transport_type,
            place_of_departure=schema.place_of_departure,
            destination=schema.destination,
            date_of_departure=schema.date_of_departure,
            date_of_return=schema.date_of_return,
            cost=schema.cost,
            variant_id=schema.variant_id
        )
