from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from exceptions import CreationException
from schemas.addon import AddonCreate
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