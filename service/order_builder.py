from models import Order


class OrderBuilder:
    def __init__(self):
        self._order_data = {}

    def set_user(self, user):
        self._order_data['user_id'] = user.id
        return self

    def set_variant(self, variant):
        self._order_data['variant_id'] = variant.id
        return self

    def set_transport(self, transport):
        self._order_data['transport_id'] = transport.id
        return self

    def set_order_date(self, order_date):
        self._order_data['order_date'] = order_date
        return self

    def set_cost(self, cost):
        self._order_data['cost'] = cost
        return self

    def build(self):
        return Order(**self._order_data)
