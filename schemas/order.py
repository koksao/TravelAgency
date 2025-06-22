from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from models import TransportType


class OrderCreate(BaseModel):
    user_id: int
    variant_id: int
    transport_type: TransportType
    order_date: date
    addon_ids: Optional[List[int]] = []

    class Config:
        from_attributes = True