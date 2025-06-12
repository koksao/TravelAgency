from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base
from schemas.user import UserCreate


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    date_of_birth = Column(Date)
    id_series = Column(String)
    id_number = Column(String)

    orders = relationship("Order", back_populates="user")


    @classmethod
    def from_create_schema(cls, schema: 'UserCreate') -> 'User':
        return cls(
            first_name=schema.first_name,
            last_name=schema.last_name,
            email=schema.email,
            date_of_birth=schema.date_of_birth,
            id_series=schema.id_series,
            id_number=schema.id_number)
