from datetime import date
from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship

from database import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey("user.id"))
    variant_id = Column(Integer, ForeignKey("variant.id"))
    transport_id = Column(Integer, ForeignKey("transport.id"))
    order_date = Column(Date, default=date.today)
    cost = Column(Numeric)

    user = relationship("User",back_populates="orders")
    variant = relationship("Variant", back_populates="orders")
    transport = relationship("Transport", back_populates="orders")
    addons = relationship("OrderAddon", back_populates="order")