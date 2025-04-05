import tkinter as tk
from tkinter import messagebox

def show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart):
    clear_frame()

    tk.Label(main_frame, text="IN-CART ITEMS", font=("Helvetica", 20, "bold"),
             bg="black", fg="white").pack(pady=10)

    items = cart.get_items()
    if not items:
        tk.Label(main_frame, text="Your cart is empty.", fg="white", bg="black",
                 font=("Helvetica", 14)).pack(pady=20)
        tk.Button(main_frame, text="Back to Menu", command=go_back,
                  bg="gray", fg="white", font=("Helvetica", 12)).pack()
        return

    for name, data in items.items():
        item_frame = tk.Frame(main_frame, bg="black")
        item_frame.pack(pady=10)

        left = tk.Frame(item_frame, bg="black")
        left.pack(side="left", padx=10)
        tk.Label(left, text="[IMG]", width=10, height=5, bg="#444").pack()

        center = tk.Frame(item_frame, bg="black")
        center.pack(side="left")
        tk.Label(center, text=name, fg="white", bg="black",
                 font=("Helvetica", 12, "bold")).pack(anchor="w")
        tk.Label(center, text=f"${data['price']:.2f}", fg="white", bg="black").pack(anchor="w")

        qty_frame = tk.Frame(center, bg="black")
        qty_frame.pack(pady=5)
        tk.Button(qty_frame, text="-", width=2, bg="red", fg="white",
                  command=lambda n=name: update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, n, -1)).pack(side="left", padx=2)
        tk.Label(qty_frame, text=data['quantity'], fg="white", bg="black", width=3).pack(side="left")
        tk.Button(qty_frame, text="+", width=2, bg="green", fg="white",
                  command=lambda n=name: update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, n, 1)).pack(side="left", padx=2)

        tk.Button(item_frame, text="X", fg="white", bg="red", width=2,
                  command=lambda n=name: remove_item(cart, main_frame, clear_frame, go_back, show_checkout_screen, n)).pack(side="right", padx=10)

    subtotal = cart.get_subtotal()
    tax = round(subtotal * 0.0625, 2)
    total = round(subtotal + tax, 2)
    count = cart.get_total_items()

    tk.Frame(main_frame, height=2, bg="white").pack(fill="x", pady=10)
    summary = tk.Frame(main_frame, bg="black")
    summary.pack()
    row(summary, f"Subtotal ({count})", f"${subtotal:.2f}")
    row(summary, "Taxes", f"${tax:.2f}")
    row(summary, "Total", f"${total:.2f}")

    tk.Button(main_frame, text="Proceed to Checkout", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0,
              command=lambda: show_checkout_screen(main_frame, clear_frame, show_cart_screen, None, cart)).pack(pady=10)

    tk.Button(main_frame, text="Cancel", font=("Helvetica", 12), bg="gray", fg="white",
              command=go_back).pack()

def update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, name, delta):
    if delta > 0:
        cart.add_item(name, cart.get_items()[name]['price'])
    else:
        cart.remove_item(name)
    show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart)

def remove_item(cart, main_frame, clear_frame, go_back, show_checkout_screen, name):
    cart.remove_item(name, remove_all=True)
    show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart)

def row(frame, label, value):
    r = tk.Frame(frame, bg="black")
    r.pack(anchor="e")
    tk.Label(r, text=label, font=("Helvetica", 12), fg="white", bg="black").pack(side="left")
    tk.Label(r, text=value, font=("Helvetica", 12, "bold"), fg="white", bg="black").pack(side="left", padx=10)