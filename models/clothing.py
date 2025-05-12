from .product import Product

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self._name} | Size: {self.size} | Material: {self.material} | Price: {self._price} | Stock: {self._quantity_in_stock}"

    def to_dict(self):
        return {
            "type": "Clothing",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity_in_stock,
            "size": self.size,
            "material": self.material
        }

    @staticmethod
    def from_dict(data):
        return Clothing(
            data["product_id"], data["name"], data["price"],
            data["quantity"], data["size"], data["material"]
        )
