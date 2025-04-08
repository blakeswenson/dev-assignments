## Program: Texas Movie Bistro App
## Date: 4/5/2025
## Author: Blake Swenson
## Purpose: Allow users to order food & drink directly to their seats

class Cart:
    # Constructor method to initialize the cart with an empty dictionary of items
    def __init__(self):
        self.items = {}  # Holds the items in the cart as a dictionary, where the key is the item name

    # Method to add an item to the cart. If the item already exists, it increases the quantity.
    def add_item(self, name, price):
        if name in self.items:
            # If the item is already in the cart, increase its quantity by 1
            self.items[name]["quantity"] += 1
        else:
            # If the item is not in the cart, add it with a quantity of 1 and its price
            self.items[name] = {"price": price, "quantity": 1}

    # Method to remove one quantity of an item from the cart. If the quantity reaches 0, the item is removed.
    def remove_item(self, name):
        if name in self.items:
            # Decrease the item's quantity by 1
            self.items[name]["quantity"] -= 1
            # If the item's quantity is 0 or less, remove the item from the cart
            if self.items[name]["quantity"] <= 0:
                del self.items[name]

    # Method to completely remove an item from the cart, regardless of quantity.
    def remove_all(self, name):
        if name in self.items:
            # Remove the item from the cart entirely
            del self.items[name]

    # Method to get all items in the cart as a list of dictionaries with item details (name, price, quantity)
    def get_items(self):
        return [
            {"name": name, "price": data["price"], "quantity": data["quantity"]}
            for name, data in self.items.items()
        ]

    # Method to get the quantity of a specific item in the cart. Returns 0 if the item is not in the cart.
    def get_quantity(self, name):
        return self.items[name]["quantity"] if name in self.items else 0

    # Method to calculate the subtotal (total price) of all items in the cart based on their price and quantity.
    def get_subtotal(self):
        return sum(data["price"] * data["quantity"] for data in self.items.values())

    # Method to calculate the total number of items (sum of quantities) in the cart.
    def get_total_items(self):
        return sum(data["quantity"] for data in self.items.values())

    # Method to clear the entire cart (remove all items).
    def clear_cart(self):
        self.items.clear()  # Removes all items from the cart by clearing the dictionary
