from typing import Optional, List

from sqlalchemy.orm import Session

from models import Variant
from schemas.variant import VariantGet


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

def get_variants_by_trip_id(db: Session, trip_id: int) -> Optional[List[VariantGet]]:
    variants = db.query(Variant).filter(Variant.trip_id == trip_id).all()
    return variants