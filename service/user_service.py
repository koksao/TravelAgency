from fastapi import HTTPException
from sqlalchemy.orm import Session

from exceptions import UserNotFoundException
from repositories import user_repository
from schemas.user import UserCreate
from models.user import User

def create_user(user_data: UserCreate, db: Session) -> User:
    existing = user_repository.get_user_by_email(db, user_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User.from_create_schema(user_data)
    return user_repository.save_user(db, new_user)


def delete_user(user_id: int, db: Session) -> None:
    user = user_repository.get_user_by_id(db, user_id)
    if not user:
        raise UserNotFoundException(user_id)

    user_repository.delete_user_by_id(db, user_id)