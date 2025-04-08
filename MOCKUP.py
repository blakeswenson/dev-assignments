import tkinter as tk
from tkinter import Entry

# --- App Setup ---
root = tk.Tk()
root.title("Texas Movie Bistro")
root.geometry("480x800")
root.configure(bg="black")

main_frame = tk.Frame(root, bg="black")
main_frame.pack(fill="both", expand=True)

def clear_frame():
    """Clears everything in the main frame."""
    for widget in main_frame.winfo_children():
        widget.destroy()

# --- Screens ---

def show_welcome_screen():
    clear_frame()

    # Logo and Tagline
    logo_label = tk.Label(main_frame, text="TEXAS MOVIE BISTRO", font=("Helvetica", 24, "bold"), fg="#ED1C24", bg="black")
    logo_label.pack(pady=(100, 10))

    tagline_label = tk.Label(main_frame, text="No Pause in the Movie —\nDelivered to Your Seat!", 
                             font=("Helvetica", 16), fg="white", bg="black", justify="center")
    tagline_label.pack(pady=(10, 40))

    # Begin Order Button
    start_button = tk.Button(main_frame, text="BEGIN ORDER", font=("Helvetica", 14, "bold"),
                             bg="#ED1C24", fg="white", padx=20, pady=10, bd=0,
                             command=show_menu_screen)
    start_button.pack()

def show_menu_screen():
    clear_frame()

    # Top navigation (stubbed Help and Cart)
    top_frame = tk.Frame(main_frame, bg="black")
    top_frame.pack(fill="x", pady=10, padx=10)

    help_btn = tk.Button(top_frame, text="Help", bg="black", fg="white", font=("Helvetica", 10), bd=0)
    help_btn.pack(side="left")

    cart_btn = tk.Button(top_frame, text="🛒", bg="black", fg="white", font=("Helvetica", 14), bd=0)
    cart_btn.pack(side="right")

    # Logo again
    logo_label = tk.Label(main_frame, text="TEXAS MOVIE BISTRO", font=("Helvetica", 18, "bold"), fg="#ED1C24", bg="black")
    logo_label.pack()

    # Tagline
    tagline = tk.Label(main_frame, text="No Pause in the Movie —\nDelivered to Your Seat!",
                       font=("Helvetica", 14), fg="white", bg="black", justify="center")
    tagline.pack(pady=10)

    # Search bar
    search_entry = Entry(main_frame, font=("Helvetica", 12))
    search_entry.insert(0, "Search")
    search_entry.pack(pady=10, ipadx=10, ipady=6)

    # Category buttons (placeholders with text)
    categories = ["APPETIZERS", "ENTREES", "SNACKS", "BEVERAGES"]
    for category in categories:
        cat_btn = tk.Button(main_frame, text=category, font=("Helvetica", 14, "bold"),
                            width=30, height=2, bg="gray20", fg="white", bd=0)
        cat_btn.pack(pady=5)

# --- Start App ---
show_welcome_screen()
root.mainloop()
