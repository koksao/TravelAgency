from enum import Enum

class PaymentMethod(str, Enum):
    BLIK = "blik"
    TRADITIONAL_TRANSFER = "traditional_transfer"