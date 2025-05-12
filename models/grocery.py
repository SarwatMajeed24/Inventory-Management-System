from .product import Product
from datetime import datetime

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.expiry_date = expiry_date  # Format: YYYY-MM-DD

    def is_expired(self):
        return datetime.strptime(self.expiry_date, "%Y-%m-%d") < datetime.now()

    def __str__(self):
        return f"[Grocery] {self._name} | Expiry: {self.expiry_date} | Price: {self._price} | Stock: {self._quantity_in_stock}"

    def to_dict(self):
        return {
            "type": "Grocery",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity_in_stock,
            "expiry_date": self.expiry_date
        }

    @staticmethod
    def from_dict(data):
        return Grocery(
            data["product_id"], data["name"], data["price"],
            data["quantity"], data["expiry_date"]
        )
