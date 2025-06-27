from typing import List, Any

from sqlalchemy.orm import Session
from models import Addon
from schemas.addon import AddonGet


def save_addon(db: Session, addon: Addon) -> Addon:
    db.add(addon)
    db.commit()
    db.refresh(addon)
    return addon


def get_addons_by_ids(db: Session, ids: List[int]) -> list[type[Addon]]:
    return db.query(Addon).filter(Addon.id.in_(ids)).all()

def get_addons_by_trip_id(db: Session, trip_id: int) -> List[AddonGet]:
    addons = db.query(Addon).filter(Addon.trip_id == trip_id).all()
    return addons

def delete_addon(db: Session, addon_id: int) -> None:
    addon = db.query(Addon).filter(Addon.id == addon_id).first()
    if addon is not None:
        db.delete(addon)
        db.commit()
        return True