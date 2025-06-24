from typing import List

from sqlalchemy.orm import Session

from models import Trip
from repositories import trip_repository
from schemas.trip import TripCreate

def create_trip(trip_data: TripCreate, db: Session) -> Trip:
    new_trip = Trip.from_create_schema(trip_data)
    return trip_repository.save_trip(db, new_trip)

def delete_trip(trip_id: int, db: Session) -> None:
    trip_repository.delete_trip_by_id(db, trip_id)

def get_all_trips(db: Session) -> List[Trip]:
    trips = trip_repository.get_all_trips(db)
    return trips