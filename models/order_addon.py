
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class OrderAddon(Base):
    __tablename__ = "order_addon"

    order_id = Column(Integer,ForeignKey("order.id"), primary_key=True)
    addon_id = Column(Integer, ForeignKey("addon.id"), primary_key=True)
    quantity = Column(Integer)

    order = relationship("Order", back_populates="addons")
    addon = relationship("Addon", back_populates="orders")
