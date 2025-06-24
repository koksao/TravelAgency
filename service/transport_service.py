from typing import Optional, List

from sqlalchemy.orm import Session

from exceptions import InvalidTransportDatesException, VariantNotFoundException, \
    TransportDatesOutOfVariantRangeException, TransportNotFoundException
from models import Variant
from models.transport import Transport
from repositories import transport_repository
from schemas.transport import TransportCreate, TransportRead
from schemas.transport_type import TransportType


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

def get_transport_by_variant_id_and_transport_type(db: Session, variant_id: int, transport_type: TransportType) -> Transport:
    transport = transport_repository.get_transport_by_variant_and_type(db, variant_id, transport_type)
    if transport is None:
        raise TransportNotFoundException()
    return transport

def get_transports_by_variant_id(variant_id: int, db: Session) -> List[TransportRead]:
    transports = transport_repository.get_transports_by_variant_id(db, variant_id)
    if not transports:
        raise TransportNotFoundException()
    return transports
