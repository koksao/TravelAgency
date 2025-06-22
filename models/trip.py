from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base
from schemas.trip import TripCreate


class Trip(Base):
    __tablename__ = "trip"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    country = Column(String)
    description = Column(String)

    variants = relationship("Variant", back_populates="trip", cascade="all, delete-orphan",
    passive_deletes=True)
    addons = relationship("Addon", back_populates="trip", cascade="all, delete-orphan",
    passive_deletes=True)

    @classmethod
    def from_create_schema(cls, schema: 'TripCreate') -> 'Trip':
        return cls(
            title=schema.title,
            country=schema.country,
            description=schema.description
        )