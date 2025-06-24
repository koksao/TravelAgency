from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class AddonCreate(BaseModel):
    description: str
    cost: Decimal
    availability: int
    date: date
    trip_id: int

    class Config:
        from_attributes = True

class AddonGet(BaseModel):
    description: str
    cost: Decimal
    availability: int
    date: date
    trip_id: int