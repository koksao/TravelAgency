from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from exceptions import CreationException
from schemas.transport import TransportCreate
from service import transport_service
from session import get_db

router = APIRouter()

@router.post('/', response_model=dict, status_code=status.HTTP_201_CREATED)
def create_transport(transport: TransportCreate, db: Session = Depends(get_db)):
    new_transport = transport_service.create_transport(transport_data=transport, db=db)

    if new_transport:
        return {'message':'Transport created successfully'}
    else:
        raise CreationException()