class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            self.items[name]["quantity"] += 1
        else:
            self.items[name] = {"price": price, "quantity": 1}

    def remove_item(self, name):
        if name in self.items:
            self.items[name]["quantity"] -= 1
            if self.items[name]["quantity"] <= 0:
                del self.items[name]

    def remove_all(self, name):
        if name in self.items:
            del self.items[name]

    def get_items(self):
        return [
            {"name": name, "price": data["price"], "quantity": data["quantity"]}
            for name, data in self.items.items()
        ]

    def get_quantity(self, name):
        return self.items[name]["quantity"] if name in self.items else 0

    def get_subtotal(self):
        return sum(data["price"] * data["quantity"] for data in self.items.values())

    def get_total_items(self):
        return sum(data["quantity"] for data in self.items.values())

    def clear_cart(self):
        self.items.clear()