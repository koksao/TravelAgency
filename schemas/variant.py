from decimal import Decimal

from pydantic import BaseModel
from datetime import date

class VariantCreate(BaseModel):
    trip_id: int
    start_date: date
    end_date: date
    cost: Decimal
    availability: int

    class Config:
        from_attributes = True