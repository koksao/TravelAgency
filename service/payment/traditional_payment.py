import logging

from service.payment.payment_interface import PaymentStrategy

class TraditionalTransfer(PaymentStrategy):
    def pay(self, amount: float) -> None:
        logging.info(f"Paying {amount} PLN by traditional transfer")