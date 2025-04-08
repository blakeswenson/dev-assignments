import tkinter as tk
from tkinter import IntVar  # Import IntVar for handling variable values in Tkinter widgets
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL for image loading and resizing
import os

# Function to load and resize images from the 'assets' folder
def load_image(name, size):
    base_path = os.path.dirname(__file__)  # Folder where main.py is
    asset_path = os.path.join(base_path, "assets", name)
    img = Image.open(asset_path)
    return ImageTk.PhotoImage(img.resize(size, Image.Resampling.LANCZOS))

# === Appetizers Screen ===
# Function to display the appetizers menu screen
def show_appetizers_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "APPETIZERS", [
            {"name": "Chips & Queso", "price": 8.25, "image": "chips_and_queso.png"},
            {"name": "Mozzarella Sticks (6)", "price": 8.50, "image": "mozzarella_sticks.png"},
            {"name": "Onion Ring", "price": 8.50, "image": "onion_rings.png"},
            {"name": "Fried Pickles", "price": 8.50, "image": "fried_pickles.png"},
            {"name": "Jalapeño Poppers (8)", "price": 8.50, "image": "jalapeno_poppers.png"},
            {"name": "Smothered Nachos", "price": 9.75, "image": "smothered_nachos.png"},
        ]
    )

# === Entrees Screen ===
# Function to display the entrees menu screen
def show_entrees_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "ENTREES", [
            {"name": "BBQ Wings (6)", "price": 8.25, "image": "bbq_wings.png"},
            {"name": "BBQ Wings (12)", "price": 8.50, "image": "bbq_wings.png"},
            {"name": "Smashburger", "price": 8.50, "image": "smashburger.png"},
            {"name": "Pepperoni Pizza", "price": 10.50, "image": "pepporoni_pizza.png"},
            {"name": "Turkey Sub", "price": 8.50, "image": "turkey_sub.png"},
            {"name": "Footlong Chili Dog", "price": 5.75, "image": "hot_dog.png"},
        ]
    )

# === Snacks Screen ===
# Function to display the snacks menu screen
def show_snacks_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "SNACKS", [
            {"name": "Small Popcorn", "price": 7.75, "image": "popcorn.png"},
            {"name": "Large Popcorn", "price": 9.50, "image": "popcorn.png"},
            {"name": "Twizzlers", "price": 5.75, "image": "twizzlers.png"},
            {"name": "Cotton Candy", "price": 5.75, "image": "cotton_candy.png"},
            {"name": "Gummy Bears", "price": 5.75, "image": "gummy_bears.png"},
            {"name": "Pretzels", "price": 5.75, "image": "pretzels.png"},
        ]
    )

# === Beverages Screen ===
# Function to display the beverages menu screen
def show_beverages_screen(main_frame, clear_frame, show_menu_screen, cart):
    _show_menu_items(
        main_frame, clear_frame, show_menu_screen, cart, "BEVERAGES", [
            {"name": "Pepsi Can", "price": 3.75, "image": "pepsi.png"},
            {"name": "Coke Can", "price": 3.75, "image": "coke.png"},
            {"name": "Water Bottle", "price": 5.50, "image": "water.png"},
            {"name": "Beer Bottle", "price": 8.50, "image": "beer.png"},
            {"name": "Red Bull", "price": 3.75, "image": "red_bull.png"},
            {"name": "Pure Leaf Tea", "price": 4.25, "image": "tea.png"},
        ]
    )

# === Internal Shared Screen Builder ===
# Function to display menu items (used across all screens like appetizers, entrees, etc.)
def _show_menu_items(main_frame, clear_frame, show_menu_screen, cart, title, items):
    clear_frame()  # Clear the existing content in the main frame

    # Display the menu title (Appetizers, Entrees, etc.)
    tk.Label(main_frame, text=title, font=("Helvetica", 20, "bold"), bg="black", fg="white").pack(pady=10)

    # Create a frame to hold the menu items in a grid layout
    grid_frame = tk.Frame(main_frame, bg="black")
    grid_frame.pack()

    # Loop through each item in the menu and display it
    for idx, item in enumerate(items):
        item_frame = tk.Frame(grid_frame, bg="black", padx=10, pady=10)
        row = idx // 2  # Determine the row in the grid (2 items per row)
        col = idx % 2  # Determine the column in the grid (2 items per row)
        item_frame.grid(row=row, column=col, padx=10, pady=10)  # Place the item frame in the grid

        # Load the image for the item (from the 'image' key in the item dictionary)
        item_image = load_image(item["image"], (100, 100))  # Load and resize the image
        
        # Create a label for the image
        img_label = tk.Label(item_frame, image=item_image)
        img_label.image = item_image  # Keep a reference to the image to prevent garbage collection
        img_label.pack()

        # Display the item's name and price
        tk.Label(item_frame, text=item["name"], fg="white", bg="black", font=("Helvetica", 10, "bold")).pack()
        tk.Label(item_frame, text=f"${item['price']:.2f}", fg="white", bg="black").pack()

        # Create a variable to hold the quantity of the item (initialized to 0)
        qty_var = IntVar(value=0)

        # Frame for the quantity buttons
        qty_frame = tk.Frame(item_frame, bg="black")
        qty_frame.pack(pady=5)

        # Function to increase the quantity of the item
        def increase(q=qty_var, i=item):
            q.set(q.get() + 1)  # Increase the quantity by 1
            cart.add_item(i["name"], i["price"])  # Add the item to the cart

        # Function to decrease the quantity of the item
        def decrease(q=qty_var, i=item):
            if q.get() > 0:  # Only allow decrease if quantity is greater than 0
                q.set(q.get() - 1)  # Decrease the quantity by 1
                cart.remove_item(i["name"])  # Remove the item from the cart

        # Buttons to increase or decrease the quantity
        tk.Button(qty_frame, text="-", command=decrease, width=2, bg="red", fg="white").pack(side="left", padx=2)
        tk.Label(qty_frame, textvariable=qty_var, fg="white", bg="black", width=3).pack(side="left")
        tk.Button(qty_frame, text="+", command=increase, width=2, bg="green", fg="white").pack(side="left", padx=2)

    # Back button to return to the previous menu screen
    tk.Button(
        main_frame,
        text="Add To Order",
        font=("Helvetica", 14, "bold"),
        bg="#ED1C24",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        command=show_menu_screen  # When clicked, it shows the menu screen
    ).pack(pady=20)