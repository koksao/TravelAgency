from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from exceptions import CreationException
from schemas.trip import TripCreate, TripGet
from service import trip_service
from session import get_db

router = APIRouter()

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_trip(trip: TripCreate, db: Session = Depends(get_db)):
    new_trip = trip_service.create_trip(trip, db)
    if new_trip:
        return {"message": "Trip created successfully"}
    else:
        raise CreationException()

@router.delete("/{trip_id}")
def delete_trip_endpoint(trip_id: int, db: Session = Depends(get_db)):
    trip_service.delete_trip(trip_id, db)
    return {"Trip deleted"}

@router.get("/", response_model=List[TripGet])
def read_all_trips(db: Session = Depends(get_db)):
    return trip_service.get_all_trips(db)
