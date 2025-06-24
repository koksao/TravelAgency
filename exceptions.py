from fastapi import  HTTPException, status

from fastapi import HTTPException, status

class AppException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"[Application Error] {self.message}"


class CreationException(HTTPException):
    def __init__(self, detail: str = "Something went wrong during creation"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class InvalidTransportDatesException(AppException):
    def __init__(self):
        super().__init__("The departure date must be earlier than the return date.")


class VariantNotFoundException(AppException):
    def __init__(self):
        super().__init__("Variant not found.")


class TransportDatesOutOfVariantRangeException(AppException):
    def __init__(self):
        super().__init__("The transport dates must be within the variant dates.")


class VariantUnavailableException(AppException):
    def __init__(self):
        super().__init__("No availability for this variant.")


class AddonNotFoundException(AppException):
    def __init__(self):
        super().__init__("Addon not found.")


class AddonUnavailableException(AppException):
    def __init__(self, addon_description: str):
        super().__init__(f"Addon '{addon_description}' is unavailable.")


class AddonTripMismatchException(AppException):
    def __init__(self, addon_description: str):
        super().__init__(f"Addon '{addon_description}' does not belong to the same trip as the selected variant.")


class UserNotFoundException(AppException):
    def __init__(self):
        super().__init__(f"User not found.")


class TripNotFoundException(AppException):
    def __init__(self, trip_id: int):
        super().__init__(f"Trip with id {trip_id} not found.")


class TransportNotFoundException(AppException):
    def __init__(self):
        super().__init__(f"Transport not found.")


class OrderNotFoundException(AppException):
    def __init__(self, order_id: int):
        super().__init__(f"Order with id {order_id} not found.")

class UnsupportedPaymentMethodException(AppException):
    def __init__(self):
        super().__init__("Unsupported payment method")