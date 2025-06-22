from fastapi import APIRouter
from controllers import user_controller, transport_controller, variant_controller, trip_controller, order_controller, \
    addon_controller

api_router = APIRouter()

api_router.include_router(user_controller.router, prefix="/users", tags=["users"])
api_router.include_router(transport_controller.router, prefix="/transport", tags=["transport"])
api_router.include_router(variant_controller.router, prefix="/variant", tags=["variant"])
api_router.include_router(trip_controller.router, prefix="/trip", tags=["trip"])
api_router.include_router(order_controller.router, prefix="/order", tags=["order"])
api_router.include_router(addon_controller.router, prefix="/addon", tags=["addon"])