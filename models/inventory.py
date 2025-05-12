import json
from .electronics import Electronics
from .grocery import Grocery
from .clothing import Clothing
from .product import Product
from utils.exceptions import DuplicateProductIDError

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.get_id() in self._products:
            raise DuplicateProductIDError(f"Product ID {product.get_id()} already exists.")
        self._products[product.get_id()] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p.get_name().lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.get_type() == product_type]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = [pid for pid, p in self._products.items()
                     if isinstance(p, Grocery) and p.is_expired()]
        for pid in to_remove:
            del self._products[pid]

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump([p.to_dict() for p in self._products.values()], f)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self._products.clear()
            for item in data:
                cls = item["type"]
                if cls == "Electronics":
                    prod = Electronics.from_dict(item)
                elif cls == "Grocery":
                    prod = Grocery.from_dict(item)
                elif cls == "Clothing":
                    prod = Clothing.from_dict(item)
                else:
                    continue
                self._products[prod.get_id()] = prod
