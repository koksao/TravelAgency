from decimal import Decimal

from sqlalchemy.orm import Session

from exceptions import VariantNotFoundException, VariantUnavailableException, AddonNotFoundException, \
    AddonUnavailableException, AddonTripMismatchException, TransportNotFoundException, OrderNotFoundException, \
    UnsupportedPaymentMethodException
from models import Order, Transport, OrderAddon, Addon, Variant
from models.payment_type import PaymentMethod
from repositories import order_repository, variant_repository, addon_repository
from schemas.order import OrderCreate
from service.order_builder import OrderBuilder
from service.payment.blik_payment import BlikPayment
from service.payment.payment_interface import PaymentStrategy
from service.payment.traditional_payment import TraditionalTransfer
from service.user_service import get_user_by_email
from service.transport_service import get_transport_by_variant_id_and_transport_type


def create_order(order_data: OrderCreate, db: Session) -> Order:
    user = get_user_by_email(db, order_data.user_email)

    variant = variant_repository.get_variant_by_id(db, order_data.variant_id)
    if variant is None:
        raise VariantNotFoundException()

    if variant.availability < 1:
        raise VariantUnavailableException()

    variant.availability -= 1
    db.add(variant)

    transport = get_transport_by_variant_id_and_transport_type(db, variant.id, order_data.transport_type)

    total_cost = variant.cost + transport.cost

    addons = []
    if order_data.addon_ids:
        addons = addon_repository.get_addons_by_ids(db, order_data.addon_ids)
        if len(addons) != len(order_data.addon_ids):
            raise AddonNotFoundException()

        for addon in addons:
            if addon.trip_id != variant.trip_id:
                raise AddonTripMismatchException(addon.description)
            if addon.availability < 1:
                raise AddonUnavailableException(addon.description)
            addon.availability -= 1
            db.add(addon)
            total_cost += addon.cost

    builder = OrderBuilder()
    new_order = (builder
                 .set_user(user)
                 .set_variant(variant)
                 .set_transport(transport)
                 .set_order_date(order_data.order_date)
                 .set_cost(total_cost)
                 .build())

    saved_order = order_repository.save_order(db, new_order)

    for addon in addons:
        order_addon = OrderAddon(order_id=saved_order.id, addon_id=addon.id)
        db.add(order_addon)

    db.commit()

    payment_strategy = get_payment_strategy(order_data.payment_type)
    payment_strategy.pay(total_cost)

    return saved_order

def delete_order(order_id: int, db: Session) -> Decimal:
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise OrderNotFoundException(order_id)

    variant = db.query(Variant).filter(Variant.id == order.variant_id).first()
    if variant:
        variant.availability += 1
        db.add(variant)

    order_addons = db.query(OrderAddon).filter(OrderAddon.order_id == order.id).all()
    for order_addon in order_addons:
        addon = db.query(Addon).filter(Addon.id == order_addon.addon_id).first()
        if addon:
            addon.availability += 1
            db.add(addon)
        db.delete(order_addon)

    refund = order.cost * Decimal('0.30')

    order_repository.delete_order(db, order)

    return refund.quantize(Decimal("0.01"))

def get_order_by_id(order_id: int, db: Session) -> Order:
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise OrderNotFoundException(order_id)
    return order

def get_payment_strategy(method: PaymentMethod) -> PaymentStrategy:
    if method == PaymentMethod.BLIK:
        return BlikPayment()
    elif method == PaymentMethod.TRADITIONAL_TRANSFER:
        return TraditionalTransfer()
    else:
        raise UnsupportedPaymentMethodException()

