from typing import List, Optional

from sqlalchemy.orm import Session
from models import Transport
from schemas.transport_type import TransportType


def save_transport(db: Session, transport: Transport) -> Transport:
    db.add(transport)
    db.commit()
    db.refresh(transport)
    return transport


def get_transport_by_variant_and_type(db: Session, variant_id: int, transport_type: TransportType) -> Optional[Transport]:
    return db.query(Transport).filter_by(variant_id=variant_id, transport_type=transport_type).first()

from typing import List

def get_transports_by_variant_id(db: Session, variant_id: int) -> List[Transport]:
    return db.query(Transport).filter_by(variant_id=variant_id).all()

