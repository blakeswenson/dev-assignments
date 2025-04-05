import tkinter as tk
from tkinter import IntVar

# === Appetizers Screen ===
def show_appetizers_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "APPETIZERS", [
            {"name": "Chips & Queso", "price": 8.25},
            {"name": "Mozzarella Sticks (6)", "price": 8.50},
            {"name": "Onion Ring", "price": 8.50},
            {"name": "Fried Pickles", "price": 8.50},
            {"name": "Jalapeño Poppers (8)", "price": 8.50},
            {"name": "Smothered Nachos", "price": 9.75},
        ]
    )

# === Entrees Screen ===
def show_entrees_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "ENTREES", [
            {"name": "BBQ Wings (6)", "price": 8.25},
            {"name": "BBQ Wings (12)", "price": 8.50},
            {"name": "Smashburger", "price": 8.50},
            {"name": "Pepperoni Pizza", "price": 10.50},
            {"name": "Turkey Sub", "price": 8.50},
            {"name": "Footlong Chili Dog", "price": 5.75},
        ]
    )

# === Snacks Screen ===
def show_snacks_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "SNACKS", [
            {"name": "Small Popcorn", "price": 7.75},
            {"name": "Large Popcorn", "price": 9.50},
            {"name": "Twizzlers", "price": 5.75},
            {"name": "Cotton Candy", "price": 5.75},
            {"name": "Gummy Bears", "price": 5.75},
            {"name": "Pretzels", "price": 5.75},
        ]
    )

# === Beverages Screen ===
def show_beverages_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "BEVERAGES", [
            {"name": "Pepsi Can", "price": 3.75},
            {"name": "Coke Can", "price": 3.75},
            {"name": "Water Bottle", "price": 5.50},
            {"name": "Beer Bottle", "price": 8.50},
            {"name": "Red Bull", "price": 3.75},
            {"name": "Pure Leaf Tea", "price": 4.25},
        ]
    )

# === Internal Shared Screen Builder ===
def _show_menu_items(main_frame, clear_frame, show_menu_screen, cart, title, items):
    clear_frame()

    tk.Label(main_frame, text=title, font=("Helvetica", 20, "bold"), bg="black", fg="white").pack(pady=10)

    grid_frame = tk.Frame(main_frame, bg="black")
    grid_frame.pack()

    for idx, item in enumerate(items):
        item_frame = tk.Frame(grid_frame, bg="black", padx=10, pady=10)
        row = idx // 2
        col = idx % 2
        item_frame.grid(row=row, column=col, padx=10, pady=10)

        placeholder = tk.Label(item_frame, width=18, height=9, bg="#444444")
        placeholder.pack()

        tk.Label(item_frame, text=item["name"], fg="white", bg="black", font=("Helvetica", 10, "bold")).pack()
        tk.Label(item_frame, text=f"${item['price']:.2f}", fg="white", bg="black").pack()

        qty_var = IntVar(value=0)

        qty_frame = tk.Frame(item_frame, bg="black")
        qty_frame.pack(pady=5)

        def increase(q=qty_var, i=item):
            q.set(q.get() + 1)
            cart.add_item(i["name"], i["price"])

        def decrease(q=qty_var, i=item):
            if q.get() > 0:
                q.set(q.get() - 1)
                cart.remove_item(i["name"])

        tk.Button(qty_frame, text="-", command=decrease, width=2, bg="red", fg="white").pack(side="left", padx=2)
        tk.Label(qty_frame, textvariable=qty_var, fg="white", bg="black", width=3).pack(side="left")
        tk.Button(qty_frame, text="+", command=increase, width=2, bg="green", fg="white").pack(side="left", padx=2)

    # Back button
    tk.Button(
        main_frame,
        text="GO BACK",
        font=("Helvetica", 14, "bold"),
        bg="#ED1C24",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        command=show_menu_screen
    ).pack(pady=20)