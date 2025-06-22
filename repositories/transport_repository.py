from sqlalchemy.orm import Session
from models import Transport

def save_transport(db: Session, transport: Transport) -> Transport:
    db.add(transport)
    db.commit()
    db.refresh(transport)
    return transport