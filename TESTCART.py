from cart_screen import Cart

# Create a cart instance
cart = Cart()

# Add items
cart.add_item("Appetizer Sampler", 7.99, 2)
cart.add_item("Large Popcorn", 5.50)

# Print current items
print("Cart Contents:")
for item in cart.get_items():
    print(f"- {item['name']} x{item['quantity']} = ${item['price'] * item['quantity']:.2f}")

# Total
print(f"\nTotal: ${cart.get_total():.2f}")

# Remove item
cart.remove_item("Large Popcorn")

# Print updated cart
print("\nAfter removing Large Popcorn:")
for item in cart.get_items():
    print(f"- {item['name']} x{item['quantity']}")

# Clear cart
cart.clear_cart()
print("\nCart after clearing:", cart.get_items())
