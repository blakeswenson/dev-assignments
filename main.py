## Program: Texas Movie Bistro App
## Date: 4/5/2025
## Author: Blake Swenson
## Purpose: Allow users to order food & drink directly to their seats

import tkinter as tk
from PIL import Image, ImageTk
import os

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

root = tk.Tk()
root.title("Texas Movie Bistro")
root.geometry("480x800")

cart = Cart()

# Load and resize images from assets folder
def load_image(name, size):
    img = Image.open(f"assets/{name}")
    return ImageTk.PhotoImage(img.resize(size, Image.Resampling.LANCZOS))

images = {
    "logo": load_image("logo.png", (180, 40)),
    "appetizers": load_image("appetizers.png", (320, 120)),
    "entrees": load_image("entrees.png", (320, 120)),
    "snacks": load_image("snacks.png", (150, 120)),
    "beverages": load_image("beverages.png", (150, 120)),
    "welcome_bg": load_image("welcome_bg.png", (480, 800))
}

main_frame = tk.Frame(root, bg="black")
main_frame.pack(fill="both", expand=True)

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def create_menu_tile(parent, image, label, command=None, width=320, height=120):
    canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0, bg="black")
    canvas.create_image(0, 0, anchor="nw", image=image)
    canvas.create_text(width // 2, height // 2, text=label.upper(), fill="white", font=("Helvetica", 16, "bold"))
    canvas.image = image
    if command:
        canvas.bind("<Button-1>", lambda e: command())
    canvas.pack(pady=5, padx=5, side="left" if width == 150 else "top")

def show_welcome_screen():
    clear_frame()
    tk.Label(main_frame, image=images["welcome_bg"]).place(relx=0, rely=0, relwidth=1, relheight=1)
    tk.Label(main_frame, image=images["logo"], bg="black").place(relx=0.5, y=150, anchor="center")
    tk.Label(main_frame, text="No Pause in the Movie —\nDelivered to Your Seat!",
             font=("Helvetica", 16), fg="white", bg="black", justify="center").place(relx=0.5, y=230, anchor="center")
    tk.Button(main_frame, text="BEGIN ORDER", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0,
              command=show_menu_screen).place(relx=0.5, y=300, anchor="center")

def show_menu_screen():
    clear_frame()

    top = tk.Frame(main_frame, bg="black")
    top.pack(fill="x", pady=5, padx=10)
    tk.Button(top, text="Help", bg="black", fg="white", bd=0).pack(side="left")
    tk.Button(top, text="🛒", bg="black", fg="white", bd=0,
              command=lambda: show_cart_screen(
                  main_frame,
                  clear_frame,
                  show_menu_screen,
                  show_customer_info_screen,
                  cart
              )).pack(side="right")

    tk.Label(main_frame, image=images["logo"], bg="black").pack(pady=(0, 10))
    tk.Label(main_frame, text="No Pause in the Movie —\nDelivered to Your Seat!",
             font=("Helvetica", 14), fg="white", bg="black").pack()

    search = tk.Entry(main_frame, font=("Helvetica", 12))
    search.insert(0, "Search")
    search.pack(pady=10, ipadx=10, ipady=6)

    create_menu_tile(main_frame, images["appetizers"], "Appetizers",
                     command=lambda: show_appetizers_screen(main_frame, clear_frame, show_menu_screen, cart))

    create_menu_tile(main_frame, images["entrees"], "Entrées",
                     command=lambda: show_entrees_screen(main_frame, clear_frame, show_menu_screen, cart))

    row_frame = tk.Frame(main_frame, bg="black")
    row_frame.pack(pady=5)

    create_menu_tile(row_frame, images["snacks"], "Snacks", width=150, height=120,
                     command=lambda: show_snacks_screen(main_frame, clear_frame, show_menu_screen, cart))

    create_menu_tile(row_frame, images["beverages"], "Beverages", width=150, height=120,
                     command=lambda: show_beverages_screen(main_frame, clear_frame, show_menu_screen, cart))

show_welcome_screen()
root.mainloop()
