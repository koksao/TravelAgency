from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from schemas.transport_type import TransportType
from schemas.payment_type import PaymentMethod


class OrderCreate(BaseModel):
    user_email: str
    variant_id: int
    transport_type: TransportType
    order_date: date = date.today()
    payment_type: PaymentMethod
    addon_ids: Optional[List[int]] = []

    class Config:
        from_attributes = True

class OrderGet(BaseModel):
    id: int
    user_email: str
    variant_id: int
    transport_type: TransportType
    order_date: date = date.today()
    payment_type: PaymentMethod
    addon_ids: Optional[List[int]] = []

    class Config:
        from_attributes = True