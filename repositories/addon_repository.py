from typing import List, Any

from sqlalchemy.orm import Session
from models import Addon

def save_addon(db: Session, addon: Addon) -> Addon:
    db.add(addon)
    db.commit()
    db.refresh(addon)
    return addon


def get_addons_by_ids(db: Session, ids: List[int]) -> list[type[Addon]]:
    return db.query(Addon).filter(Addon.id.in_(ids)).all()
