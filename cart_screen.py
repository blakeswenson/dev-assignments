import tkinter as tk
from checkout_screen import show_customer_info_screen, show_payment_screen  # Import checkout screen modules
from PIL import Image, ImageTk  # Make sure Pillow is installed for image handling
import os # Import os for file path handling

# Function to load and resize images from the 'assets' folder
def load_image(name, size):
    base_path = os.path.dirname(__file__)  # Folder where main.py is
    asset_path = os.path.join(base_path, "assets", name)
    img = Image.open(asset_path)
    return ImageTk.PhotoImage(img.resize(size, Image.Resampling.LANCZOS))

# Function to display the cart screen where users can view and modify their cart items
def show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart):
    clear_frame()  # Clear the main frame to prepare for new content

    # Display the cart title
    tk.Label(main_frame, text="IN-CART ITEMS", font=("Helvetica", 20, "bold"), bg="black", fg="white").pack(pady=10)

    # Get the list of items in the cart
    items = cart.get_items()
    
    # If the cart is empty, show a message and a button to go back to the menu
    if not items:
        tk.Label(main_frame, text="Your cart is empty.", fg="white", bg="black", font=("Helvetica", 14)).pack(pady=20)
        tk.Button(main_frame, text="Back to Menu", command=go_back, bg="gray", fg="white", font=("Helvetica", 12)).pack()
        return

    # Load images for each item (using the filenames provided earlier)
    item_images = {
        "Chips & Queso": load_image("chips_and_queso.png", (100, 100)),
        "Mozzarella Sticks (6)": load_image("mozzarella_sticks.png", (100, 100)),
        "Onion Ring": load_image("onion_rings.png", (100, 100)),
        "Fried Pickles": load_image("fried_pickles.png", (100, 100)),
        "Jalapeño Poppers (8)": load_image("jalapeno_poppers.png", (100, 100)),
        "Smothered Nachos": load_image("smothered_nachos.png", (100, 100)),
        "BBQ Wings (6)": load_image("bbq_wings.png", (100, 100)),
        "BBQ Wings (12)": load_image("bbq_wings.png", (100, 100)),
        "Smashburger": load_image("smashburger.png", (100, 100)),
        "Pepperoni Pizza": load_image("pepporoni_pizza.png", (100, 100)),
        "Turkey Sub": load_image("turkey_sub.png", (100, 100)),
        "Footlong Chili Dog": load_image("hot_dog.png", (100, 100)),
        "Small Popcorn": load_image("popcorn.png", (100, 100)),
        "Large Popcorn": load_image("popcorn.png", (100, 100)),  # Use the same popcorn image
        "Twizzlers": load_image("twizzlers.png", (100, 100)),
        "Gummy Bears": load_image("gummy_bears.png", (100, 100)),
        "Cotton Candy": load_image("cotton_candy.png", (100, 100)),
        "Pepsi Can": load_image("pepsi.png", (100, 100)),
        "Coke Can": load_image("coke.png", (100, 100)),
        "Beer Bottle": load_image("beer.png", (100, 100)),
        "Red Bull": load_image("red_bull.png", (100, 100)),
        "Water Bottle": load_image("water.png", (100, 100)),
        "Pure Leaf Tea": load_image("tea.png", (100, 100)),
        "Pretzels": load_image("pretzels.png", (100, 100)),
    }

    # For each item in the cart, display its details (name, price, quantity)
    for item in items:
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]

        # Create a frame to hold the item details
        item_frame = tk.Frame(main_frame, bg="black")
        item_frame.pack(pady=10)

        # Create a sub-frame for the image
        left = tk.Frame(item_frame, bg="black")
        left.pack(side="left", padx=10)

        # Load the image for the item, if available
        item_image = item_images.get(name, None)  # Default to None if the image doesn't exist
        if not item_image:
            print(f"Image not found for: {name}")  # Debugging message if image is missing
        else:
            image_label = tk.Label(left, image=item_image)  # Create a label for the image
            image_label.image = item_image  # Keep reference to image to avoid garbage collection
            image_label.pack()

        # Create a sub-frame for the name, price, and quantity of the item
        center = tk.Frame(item_frame, bg="black")
        center.pack(side="left")
        tk.Label(center, text=name, fg="white", bg="black", font=("Helvetica", 12, "bold")).pack(anchor="w")
        tk.Label(center, text=f"${price:.2f}", fg="white", bg="black").pack(anchor="w")

        # Create a sub-frame for modifying the quantity of the item
        qty_frame = tk.Frame(center, bg="black")
        qty_frame.pack(pady=5)
        tk.Button(qty_frame, text="-", width=2, bg="red", fg="white",
                  command=lambda n=name: update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, n, -1)).pack(side="left", padx=2)
        tk.Label(qty_frame, text=quantity, fg="white", bg="black", width=3).pack(side="left")
        tk.Button(qty_frame, text="+", width=2, bg="green", fg="white",
                  command=lambda n=name: update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, n, 1)).pack(side="left", padx=2)

        # Button to remove the item from the cart
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
              command=lambda: show_checkout_screen(
                  main_frame,
                  clear_frame,
                  show_cart_screen,
                  show_payment_screen,
                  cart
              )).pack(pady=10)

    # Button to cancel and return to the menu screen
    tk.Button(main_frame, text="Go Back", font=("Helvetica", 12), bg="gray", fg="white", command=go_back).pack()

# Function to update the quantity of an item in the cart
def update_qty(cart, main_frame, clear_frame, go_back, show_checkout_screen, name, delta):
    if delta > 0:  # If adding, increase the quantity
        cart.add_item(name, cart.get_items()[0]["price"])
    else:  # If removing, decrease the quantity
        cart.remove_item(name)
    # Refresh the cart screen to reflect the updated cart contents
    show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart)

# Function to remove an item completely from the cart
def remove_item(cart, main_frame, clear_frame, go_back, show_checkout_screen, name):
    cart.remove_all(name)  # Remove all occurrences of the item from the cart
    # Refresh the cart screen to reflect the updated cart contents
    show_cart_screen(main_frame, clear_frame, go_back, show_checkout_screen, cart)

# Function to create a row displaying a label and value (e.g., Subtotal, Taxes, Total)
def row(frame, label, value):
    r = tk.Frame(frame, bg="black")
    r.pack(anchor="e")
    tk.Label(r, text=label, font=("Helvetica", 12), fg="white", bg="black").pack(side="left")
    tk.Label(r, text=value, font=("Helvetica", 12, "bold"), fg="white", bg="black").pack(side="left", padx=10)
