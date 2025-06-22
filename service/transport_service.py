from typing import Optional

from sqlalchemy.orm import Session

from exceptions import InvalidTransportDatesException, VariantNotFoundException, \
    TransportDatesOutOfVariantRangeException
from models import Variant
from models.transport import Transport
from repositories import transport_repository
from schemas.transport import TransportCreate

def create_transport(db: Session, transport_data: TransportCreate) -> Transport:
    if transport_data.date_of_departure >= transport_data.date_of_return:
        raise InvalidTransportDatesException()

    variant: Optional[Variant] = db.query(Variant).filter(Variant.id == transport_data.variant_id).first()
    if not variant:
        raise VariantNotFoundException()

    if transport_data.date_of_departure < variant.start_date or transport_data.date_of_return > variant.end_date:
        raise TransportDatesOutOfVariantRangeException()

    new_transport = Transport.from_create_schema(transport_data)
    return transport_repository.save_transport(db, new_transport)