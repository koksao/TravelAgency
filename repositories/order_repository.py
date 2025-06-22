from sqlalchemy.orm import Session

from models import Order

def save_order(db: Session, order: Order) -> Order:
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_order_by_id(db: Session, order_id: int) -> Order:
    return db.query(Order).filter(Order.id == order_id).first()

def delete_order(db: Session, order: Order) -> None:
    db.delete(order)
    db.commit()
