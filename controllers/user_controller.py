from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from exceptions import CreationException
from schemas.user import UserCreate
from service import user_service
from session import get_db

router = APIRouter()

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = user_service.create_user(user, db)

    if new_user:
        return {"message": "User created successfully"}
    else:
        raise CreationException()

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(user_id, db)
    return {"User deleted"}

@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(user_id, db)