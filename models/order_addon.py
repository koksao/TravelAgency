
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class OrderAddon(Base):
    __tablename__ = "order_addon"

    order_id = Column(Integer,ForeignKey("order.id"), primary_key=True)
    addon_id = Column(Integer, ForeignKey("addon.id", ondelete="CASCADE"), primary_key=True)

    order = relationship("Order", back_populates="addons")
    addon = relationship("Addon", back_populates="orders")
