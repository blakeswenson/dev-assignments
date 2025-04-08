import tkinter as tk
from PIL import Image, ImageTk
import os
import tkinter.messagebox as messagebox

# === Custom Modules ===
from cart import Cart
from cart_screen import show_cart_screen
from checkout_screen import show_customer_info_screen  # Renamed from checkout_screen
from menu_screens import (
    show_appetizers_screen,
    show_entrees_screen,
    show_snacks_screen,
    show_beverages_screen
)

# Initialize the main window (root) for the application
root = tk.Tk()
root.title("Texas Movie Bistro")  # Set window title
root.geometry("500x800")  # Set window size

# Initialize an instance of Cart class to manage the user's cart
cart = Cart()

# Function to load and resize images from the 'assets' folder
def load_image(name, size):
    base_path = os.path.dirname(__file__)  # Folder where main.py is
    asset_path = os.path.join(base_path, "assets", name)
    img = Image.open(asset_path)
    return ImageTk.PhotoImage(img.resize(size, Image.Resampling.LANCZOS))

# Dictionary storing images used in the app, each image loaded and resized
images = {
    "logo": load_image("logo.png", (180, 40)),
    "appetizers": load_image("appetizers.png", (320, 120)),
    "entrees": load_image("entrees.png", (320, 120)),
    "snacks": load_image("snacks.png", (150, 120)),
    "beverages": load_image("beverages.png", (150, 120)),
    "welcome_bg": load_image("welcome_bg.png", (480, 800))  # Background image for welcome screen
}

# Create a main frame to hold UI elements, with black background color
main_frame = tk.Frame(root, bg="black")
main_frame.pack(fill="both", expand=True)

# Function to clear all widgets from the main frame
def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Function to create a menu tile (button) with an image and label
def create_menu_tile(parent, image, label, command=None, width=320, height=120):
    # Create a canvas to display the image and label
    canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0, bg="black")
    canvas.create_image(0, 0, anchor="nw", image=image)  # Add the image to the canvas
    canvas.create_text(width // 2, height // 2, text=label.upper(), fill="white", font=("Helvetica", 16, "bold"))  # Add label
    canvas.image = image  # Store the image reference
    if command:  # If a command is provided, bind it to the tile
        canvas.bind("<Button-1>", lambda e: command())
    canvas.pack(pady=5, padx=5, side="left" if width == 150 else "top")  # Position the tile based on the width

# Function to show the welcome screen
def show_welcome_screen():
    clear_frame()  # Clear any existing widgets on the screen

    # Display background image
    tk.Label(main_frame, image=images["welcome_bg"]).place(relx=0, rely=0, relwidth=1, relheight=1)
    # Display logo image
    tk.Label(main_frame, image=images["logo"], bg="black").place(relx=0.5, y=150, anchor="center")
    # Display text message
    tk.Label(main_frame, text="No Pause in the Movie —\nDelivered to Your Seat!",
             font=("Helvetica", 16), fg="white", bg="black", justify="center").place(relx=0.5, y=230, anchor="center")
    # Display the "BEGIN ORDER" button, which will navigate to the menu screen
    tk.Button(main_frame, text="BEGIN ORDER", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0,
              command=show_menu_screen).place(relx=0.5, y=300, anchor="center")

# Function to show the menu screen (after user clicks "BEGIN ORDER")
def show_menu_screen():
    clear_frame()  # Clear any existing widgets on the screen

    # Create the top frame with "Help" and cart button
    top = tk.Frame(main_frame, bg="black")
    top.pack(fill="x", pady=5, padx=10)
    tk.Button(top, text="Help", bg="black", fg="white", bd=0, command=show_help).pack(side="left")  # Help button (no functionality yet)
    # Cart button, when clicked shows the cart screen
    tk.Button(top, text="🛒", bg="black", fg="white", bd=0,
              command=lambda: show_cart_screen(
                  main_frame,
                  clear_frame,
                  show_menu_screen,
                  show_customer_info_screen,
                  cart
              )).pack(side="right")

    # Display logo image and text
    tk.Label(main_frame, image=images["logo"], bg="black").pack(pady=(0, 10))
    tk.Label(main_frame, text="No Pause in the Movie —\nDelivered to Your Seat!",
             font=("Helvetica", 14), fg="white", bg="black").pack()

    # Search bar (not fully functional yet)
    search = tk.Entry(main_frame, font=("Helvetica", 12))
    search.insert(0, "Search")
    search.pack(pady=10, ipadx=10, ipady=6)

    search_button = tk.Button(main_frame, text="Search", font=("Helvetica", 12), bg="gray", fg="white",
                              command=lambda: search_menu_items(search.get()))
    search_button.pack(pady=5)

    # Create menu tiles for different food categories
    create_menu_tile(main_frame, images["appetizers"], "Appetizers",
                     command=lambda: show_appetizers_screen(main_frame, clear_frame, show_menu_screen, cart))

    create_menu_tile(main_frame, images["entrees"], "Entrées",
                     command=lambda: show_entrees_screen(main_frame, clear_frame, show_menu_screen, cart))

    # Create a row frame for snacks and beverages tiles
    row_frame = tk.Frame(main_frame, bg="black")
    row_frame.pack(pady=5)

    create_menu_tile(row_frame, images["snacks"], "Snacks", width=150, height=120,
                     command=lambda: show_snacks_screen(main_frame, clear_frame, show_menu_screen, cart))

    create_menu_tile(row_frame, images["beverages"], "Beverages", width=150, height=120,
                     command=lambda: show_beverages_screen(main_frame, clear_frame, show_menu_screen, cart))

# Function to show help
def show_help():
    messagebox.showinfo("Help", "This is the Texas Movie Bistro staff. An employee will be with you shortly.")

# Function to handle search and display filtered results
def search_menu_items(query):
    query = query.lower()
    # Modify your item list to filter the items based on the search query
    filtered_items = [
        # Appetizers
        {"name": "Chips & Queso", "category": "Appetizers", "price": 8.25},
        {"name": "Mozzarella Sticks (6)", "category": "Appetizers", "price": 8.50},
        {"name": "Onion Ring", "category": "Appetizers", "price": 8.50},
        {"name": "Fried Pickles", "category": "Appetizers", "price": 8.50},
        {"name": "Jalapeño Poppers (8)", "category": "Appetizers", "price": 8.50},
        {"name": "Smothered Nachos", "category": "Appetizers", "price": 9.75},

        # Entrees
        {"name": "BBQ Wings (6)", "category": "Entrees", "price": 8.25},
        {"name": "BBQ Wings (12)", "category": "Entrees", "price": 8.50},
        {"name": "Smashburger", "category": "Entrees", "price": 8.50},
        {"name": "Pepperoni Pizza", "category": "Entrees", "price": 10.50},
        {"name": "Turkey Sub", "category": "Entrees", "price": 8.50},
        {"name": "Footlong Chili Dog", "category": "Entrees", "price": 5.75},

        # Snacks
        {"name": "Small Popcorn", "category": "Snacks", "price": 7.75},
        {"name": "Large Popcorn", "category": "Snacks", "price": 9.50},
        {"name": "Twizzlers", "category": "Snacks", "price": 5.75},
        {"name": "Cotton Candy", "category": "Snacks", "price": 5.75},
        {"name": "Gummy Bears", "category": "Snacks", "price": 5.75},
        {"name": "Pretzels", "category": "Snacks", "price": 5.75},

        # Beverages
        {"name": "Pepsi Can", "category": "Beverages", "price": 3.75},
        {"name": "Coke Can", "category": "Beverages", "price": 3.75},
        {"name": "Water Bottle", "category": "Beverages", "price": 5.50},
        {"name": "Beer Bottle", "category": "Beverages", "price": 8.50},
        {"name": "Red Bull", "category": "Beverages", "price": 3.75},
        {"name": "Pure Leaf Tea", "category": "Beverages", "price": 4.25}
    ]
    filtered = [
        item for item in filtered_items if query in item["name"].lower() or query in item["category"].lower()
    ]
    show_filtered_items(filtered)

def show_filtered_items(filtered):
    clear_frame()  # Clear previous content

    for item in filtered:
        tk.Label(main_frame, text=f"{item['name']} - ${item['price']:.2f}", fg="white", bg="black", font=("Helvetica", 12)).pack(pady=5)
    
    # Optionally, add a back button to go back to the menu screen
    tk.Button(main_frame, text="Back", font=("Helvetica", 12), bg="gray", fg="white", command=show_menu_screen).pack(pady=20)

# === Run the app ===
show_welcome_screen()

root.mainloop()