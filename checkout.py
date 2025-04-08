## Program: Texas Movie Bistro App
## Date: 4/5/2025
## Author: Blake Swenson
## Purpose: Allow users to order food & drink directly to their seats

import tkinter as tk
from tkinter import messagebox  # Import the messagebox for showing dialogs (although not used in the provided code)

# Function to display the cart screen, showing items in the user's cart and their details
def show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart):
    clear_frame()  # Clear any existing content in the main frame

    # Display the title of the cart screen
    tk.Label(main_frame, text="IN-CART ITEMS", font=("Helvetica", 20, "bold"),
             bg="black", fg="white").pack(pady=10)

    # Get the list of items in the cart
    items = cart.get_items()

    # If the cart is empty, show a message and a "Back to Menu" button
    if not items:
        tk.Label(main_frame, text="Your cart is empty.", fg="white", bg="black",
                 font=("Helvetica", 14)).pack(pady=20)
        tk.Button(main_frame, text="Back to Menu", command=go_back,
                  bg="gray", fg="white", font=("Helvetica", 12)).pack()
        return

    # For each item in the cart, display its details
    for name, data in items.items():
        item_frame = tk.Frame(main_frame, bg="black")
        item_frame.pack(pady=10)

        # Create a sub-frame for the item image placeholder
        left = tk.Frame(item_frame, bg="black")
        left.pack(side="left", padx=10)
        tk.Label(left, text="[IMG]", width=10, height=5, bg="#444").pack()

        # Create a sub-frame for the item name and price
        center = tk.Frame(item_frame, bg="black")
        center.pack(side="left")
        tk.Label(center, text=name, fg="white", bg="black",
                 font=("Helvetica", 12, "bold")).pack(anchor="w")
        tk.Label(center, text=f"${data['price']:.2f}", fg="white", bg="black").pack(anchor="w")

        # Create a sub-frame for the quantity buttons (increase and decrease)
        qty_frame = tk.Frame(center, bg="black")
        qty_frame.pack(pady=5)

        # Decrease quantity button
        tk.Button(qty_frame, text="-", width=2, bg="red", fg="white",
                  command=lambda n=name: update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, n, -1)).pack(side="left", padx=2)

        # Display the current quantity of the item
        tk.Label(qty_frame, text=data['quantity'], fg="white", bg="black", width=3).pack(side="left")

        # Increase quantity button
        tk.Button(qty_frame, text="+", width=2, bg="green", fg="white",
                  command=lambda n=name: update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, n, 1)).pack(side="left", padx=2)

        # Remove item button (deletes the item from the cart)
        tk.Button(item_frame, text="X", fg="white", bg="red", width=2,
                  command=lambda n=name: remove_item(cart, main_frame, clear_frame, go_back, show_checkout_screen, n)).pack(side="right", padx=10)

    # Calculate and display the cart's subtotal, tax, and total
    subtotal = cart.get_subtotal()
    tax = round(subtotal * 0.0625, 2)  # Sales tax is 6.25%
    total = round(subtotal + tax, 2)
    count = cart.get_total_items()

    # Display the breakdown (Subtotal, Taxes, Total)
    tk.Frame(main_frame, height=2, bg="white").pack(fill="x", pady=10)  # Divider line
    summary = tk.Frame(main_frame, bg="black")
    summary.pack()
    row(summary, f"Subtotal ({count})", f"${subtotal:.2f}")
    row(summary, "Taxes", f"${tax:.2f}")
    row(summary, "Total", f"${total:.2f}")

    # Button to proceed to the checkout screen
    tk.Button(main_frame, text="Proceed to Checkout", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0,
              command=lambda: show_checkout_screen(main_frame, clear_frame, show_cart_screen, None, cart)).pack(pady=10)

    # Button to cancel and return to the previous screen
    tk.Button(main_frame, text="Cancel", font=("Helvetica", 12), bg="gray", fg="white",
              command=go_back).pack()

# Function to update the quantity of an item in the cart (either increase or decrease)
def update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, name, delta):
    if delta > 0:
        # If delta is positive, add the item to the cart
        cart.add_item(name, cart.get_items()[name]['price'])
    else:
        # If delta is negative, remove the item from the cart
        cart.remove_item(name)
    
    # After updating the quantity, refresh the cart screen
    show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart)

# Function to remove an item from the cart completely
def remove_item(cart, main_frame, clear_frame, go_back, show_checkout_screen, name):
    cart.remove_item(name, remove_all=True)  # Remove all instances of the item from the cart
    show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart)  # Refresh the cart screen

# Function to create a row for displaying label-value pairs (e.g., Subtotal, Taxes, Total)
def row(frame, label, value):
    r = tk.Frame(frame, bg="black")
    r.pack(anchor="e")  # Align the row to the right
    tk.Label(r, text=label, font=("Helvetica", 12), fg="white", bg="black").pack(side="left")  # Display label
    tk.Label(r, text=value, font=("Helvetica", 12, "bold"), fg="white", bg="black").pack(side="left", padx=10)  # Display value
