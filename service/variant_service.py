from sqlalchemy.orm import Session

from exceptions import VariantNotFoundException
from models import Variant
from repositories import variant_repository
from schemas.variant import VariantCreate


def create_variant(variant_data: VariantCreate, db: Session) -> Variant:
    new_variant = Variant.from_create_schema(variant_data)
    return variant_repository.save_variant(db, new_variant)

def delete_variant(variant_id: int, db: Session) -> None:
    variant = variant_repository.get_variant_by_id(db, variant_id)
    if not variant:
        raise VariantNotFoundException()

    variant_repository.delete_variant_by_id(db, variant_id)