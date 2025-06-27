from typing import List

from sqlalchemy.orm import Session

from exceptions import AddonNotFoundException
from models import Addon
from repositories import addon_repository
from schemas.addon import AddonCreate, AddonGet


def create_addon(addon_data: AddonCreate, db: Session) -> Addon:
    new_addon = Addon.from_create_schema(addon_data)
    return addon_repository.save_addon(db, new_addon)

def get_addons_by_trip_id(trip_id: int, db: Session) -> List[AddonGet]:
    addons = addon_repository.get_addons_by_trip_id(db, trip_id)
    if not addons:
        raise AddonNotFoundException()
    return addons

def delete_addon(addon_id: int, db: Session):
    addon_repository.delete_addon(db, addon_id)