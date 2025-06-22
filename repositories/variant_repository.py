from typing import Optional

from sqlalchemy.orm import Session

from models import Variant

def save_variant(db: Session, variant: Variant) -> Variant:
    db.add(variant)
    db.commit()
    db.refresh(variant)
    return variant


def get_variant_by_id(db: Session, variant_id: int) -> Optional[Variant]:
    return db.query(Variant).filter(Variant.id == variant_id).first()

def delete_variant_by_id(db: Session, variant_id: int) -> None:
    variant = get_variant_by_id(variant_id)
    if variant is not None:
        db.delete(variant)
        db.commit()