from datetime import date
from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship

from database import Base
from schemas.order import OrderCreate


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey("user.id"))
    variant_id = Column(Integer, ForeignKey("variant.id"))
    transport_id = Column(Integer, ForeignKey("transport.id"))
    order_date = Column(Date, default=date.today)
    cost = Column(Numeric )

    user = relationship("User",back_populates="orders")
    variant = relationship("Variant", back_populates="orders")
    transport = relationship("Transport", back_populates="orders")
    addons = relationship("OrderAddon", back_populates="order")

    @classmethod
    def from_create_schema(cls, schema: 'OrderCreate') -> 'Order':
        return cls(
            transport_type=schema.transport_type,
            payment_type = schema.payment_type,
            place_of_departure=schema.place_of_departure,
            destination=schema.destination,
            date_of_departure=schema.date_of_departure,
            date_of_return=schema.date_of_return,
            cost=schema.cost,
            variant_id=schema.variant_id
        )