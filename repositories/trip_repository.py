from sqlalchemy.orm import Session

from exceptions import TripNotFoundException
from models import Trip

def save_trip(db: Session, trip: Trip) -> Trip:
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

def delete_trip(db: Session, trip_id: int) -> Trip:
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    db.delete(trip)
    db.commit()


def get_trip_by_id(db: Session, trip_id: int) -> Trip:
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise TripNotFoundException(trip_id)
    return trip

def delete_trip_by_id(db: Session, trip_id: int) -> Trip:
    trip = get_trip_by_id(db, trip_id)
    db.delete(trip)
    db.commit()