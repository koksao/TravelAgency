from sqlalchemy.orm import Session

from models import Addon
from repositories import addon_repository
from schemas.addon import AddonCreate

def create_addon(addon_data: AddonCreate, db: Session) -> Addon:
    new_addon = Addon.from_create_schema(addon_data)
    return addon_repository.save_addon(db, new_addon)