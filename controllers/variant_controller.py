from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from exceptions import CreationException
from schemas.variant import VariantCreate, VariantGet
from service import variant_service
from session import get_db

router = APIRouter()

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_variant(variant: VariantCreate, db: Session = Depends(get_db)):
    new_variant = variant_service.create_variant(variant, db)
    if new_variant:
        return {"message": "Variant created successfully"}
    else:
        raise CreationException()

@router.delete("/{variant_id}")
def delete_variant_endpoint(variant_id: int, db: Session = Depends(get_db)):
    variant_service.delete_variant(variant_id, db)
    return {"Variant deleted"}

@router.get("/{trip_id}", response_model=List[VariantGet])
def get_variants_by_trip(trip_id: int, db: Session = Depends(get_db)):
        return variant_service.get_variants_by_trip_id(db, trip_id)