from typing import List, Optional

from sqlalchemy.orm import Session
from models import Transport
from schemas.transport_type import TransportType


def save_transport(db: Session, transport: Transport) -> Transport:
    db.add(transport)
    db.commit()
    db.refresh(transport)
    return transport

def delete_transport(transport_id: int, db: Session):
    transport = db.query(Transport).filter(Transport.id == transport_id).first()
    if transport is not None:
        db.delete(transport)
        db.commit()

def get_transport_by_variant_and_type(db: Session, variant_id: int, transport_type: TransportType) -> Optional[Transport]:
    return db.query(Transport).filter_by(variant_id=variant_id, transport_type=transport_type).first()

def get_transports_by_variant_id(db: Session, variant_id: int) -> List[Transport]:
    return db.query(Transport).filter_by(variant_id=variant_id).all()

