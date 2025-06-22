from typing import Optional
from sqlalchemy.orm import Session
from models import User

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def save_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user_by_id(db: Session, user_id: int) -> None:
    user = db.query(User).filter(User.id == user_id).first()
    if user is not None:
        db.delete(user)
        db.commit()


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()
