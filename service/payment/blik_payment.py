from service.payment.payment_interface import PaymentStrategy
import logging

class BlikPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        logging.info(f"Paying {amount} PLN via BLIK")