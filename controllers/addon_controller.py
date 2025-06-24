from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from exceptions import CreationException
from schemas.addon import AddonCreate, AddonGet
from service import addon_service
from session import get_db

router = APIRouter()

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_addon(addon: AddonCreate, db: Session = Depends(get_db)):
    new_addon = addon_service.create_addon(addon, db)
    if new_addon:
        return {"message": "Addon created successfully"}
    else:
        raise CreationException()

@router.get("/{trip_id}", response_model=List[AddonGet])
def get_addons_by_trip_id(trip_id: int, db: Session = Depends(get_db)):
        return addon_service.get_addons_by_trip_id(trip_id, db)