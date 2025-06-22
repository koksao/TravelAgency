from decimal import Decimal

from pydantic import BaseModel
from datetime import date
from .transport_type import TransportType

class TransportCreate(BaseModel):
    transport_type: TransportType
    place_of_departure: str
    destination: str
    date_of_departure: date
    date_of_return: date
    variant_id: int
    cost: Decimal

    class Config:
        from_attributes = True

class TransportRead(BaseModel):
    id: int
    transport_type: TransportType
    place_of_departure: str
    destination: str
    date_of_departure: date
    date_of_return: date
    cost: float
    variant_id: int