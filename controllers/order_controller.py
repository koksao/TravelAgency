from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from exceptions import CreationException
from schemas.order import OrderCreate
from service import  order_service
from session import get_db

router = APIRouter()

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = order_service.create_order(order, db)
    if new_order:
        return {"message": "Order created successfully"}
    else:
        raise CreationException()

@router.delete("/{order_id}")
def delete_user_endpoint(order_id: int, db: Session = Depends(get_db)):
    order_service.delete_order(order_id, db)
    return {"Order deleted"}