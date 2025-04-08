## Program: Texas Movie Bistro App
## Date: 4/5/2025
## Author: Blake Swenson
## Purpose: Allow users to order food & drink directly to their seats

import tkinter as tk

# Shared form data state for customer and payment info
# This dictionary holds customer and payment info across screens
form_data = {
    "customer": {},  # Holds customer information
    "payment": {}     # Holds payment information
}

# Function to display the customer information screen where users enter their personal details
def show_customer_info_screen(main_frame, clear_frame, show_cart_screen, show_payment_screen, cart):
    clear_frame()  # Clear the current screen content

    # Display the screen title
    tk.Label(main_frame, text="CUSTOMER INFO", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=10)

    # Fields required for customer information
    entries = {}
    fields = ["Name", "Phone Number", "Email Address", "Movie", "Seat Number"]

    # Create a label and input field for each required customer detail
    for field in fields:
        tk.Label(main_frame, text=field, fg="white", bg="black", anchor="w").pack(fill="x", padx=30)
        entry = tk.Entry(main_frame)
        entry.pack(fill="x", padx=30, pady=5)
        entries[field] = entry

    # Function to proceed to the payment screen after collecting customer info
    def next_step():
        for field in fields:
            form_data["customer"][field] = entries[field].get()  # Store the input values in form_data
        show_payment_screen(main_frame, clear_frame, show_customer_info_screen, show_summary_screen, cart)

    # Add a footer showing the cart summary (subtotal, taxes, total)
    add_summary_footer(main_frame, cart)

    # Button to proceed to the payment screen
    tk.Button(main_frame, text="Proceed to Payment Method", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0, command=next_step).pack(pady=(10, 5))

# Function to display the payment method screen where users input payment details
def show_payment_screen(main_frame, clear_frame, show_customer_info_screen, show_summary_screen, cart):
    clear_frame()  # Clear the current screen content

    # Display the screen title
    tk.Label(main_frame, text="PAYMENT METHOD INFO", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=10)

    # Fields required for payment information
    entries = {}
    fields = ["Name on Card", "Card Number", "Expiration Date", "CVV", "Billing Address", "City", "State", "Zip Code"]

    # Create a label and input field for each required payment detail
    for field in fields:
        tk.Label(main_frame, text=field, fg="white", bg="black", anchor="w").pack(fill="x", padx=30)
        entry = tk.Entry(main_frame)
        entry.pack(fill="x", padx=30, pady=5)
        entries[field] = entry

    # Function to proceed to the order summary screen after collecting payment info
    def next_step():
        for field in fields:
            form_data["payment"][field] = entries[field].get()  # Store the input values in form_data
        show_summary_screen(main_frame, clear_frame, show_payment_screen, cart)

    # Add a footer showing the cart summary (subtotal, taxes, total)
    add_summary_footer(main_frame, cart)

    # Button to proceed to the order summary screen
    tk.Button(main_frame, text="Proceed to Order Summary", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0, command=next_step).pack(pady=(10, 5))

    # Button to go back to the customer info screen
    tk.Button(main_frame, text="Go Back", font=("Helvetica", 12), bg="gray", fg="white",
              command=lambda: show_customer_info_screen(main_frame, clear_frame, None, show_payment_screen, cart)).pack()

# Function to add the cart summary footer (subtotal, taxes, total) to the bottom of the screen
def add_summary_footer(main_frame, cart):
    subtotal = cart.get_subtotal()  # Get the subtotal of all items in the cart
    tax = round(subtotal * 0.0625, 2)  # Calculate tax (6.25% sales tax)
    total = round(subtotal + tax, 2)  # Calculate total price (subtotal + tax)
    count = cart.get_total_items()  # Get the total number of items in the cart

    footer = tk.Frame(main_frame, bg="black")  # Frame to hold the summary information
    footer.pack(pady=10)

    # Helper function to create a row for the summary (e.g., Subtotal, Taxes, Total)
    def row(label, value):
        f = tk.Frame(footer, bg="black")
        f.pack(anchor="e", padx=20)  # Align to the right
        tk.Label(f, text=label, fg="white", bg="black", font=("Helvetica", 12)).pack(side="left")  # Label text
        # Display the value, formatted as currency if it's a float
        tk.Label(f, text=f"${value:.2f}" if isinstance(value, float) else value, fg="white", bg="black", font=("Helvetica", 12, "bold")).pack(side="right")

    # Display the rows for Subtotal, Taxes, and Total
    row(f"Subtotal ({count})", subtotal)
    row("Taxes", tax)
    row("Total", total)

# Function to display the order summary screen, where users can review their order details
def show_summary_screen(main_frame, clear_frame, go_back, cart):
    clear_frame()  # Clear the current screen content

    # Display the screen title
    tk.Label(main_frame, text="ORDER SUMMARY", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=10)

    # Display customer information
    for field, value in form_data["customer"].items():
        tk.Label(main_frame, text=f"{field}: {value}", fg="white", bg="black").pack(anchor="w", padx=30)

    # Display payment information (obscure sensitive data like card details and CVV)
    tk.Label(main_frame, text="\nPayment Info", font=("Helvetica", 14, "bold"), fg="white", bg="black").pack(anchor="w", padx=30)
    for field, value in form_data["payment"].items():
        # Mask sensitive payment info (card number and CVV)
        display_value = value if "Card" not in field and field != "CVV" else "****"
        tk.Label(main_frame, text=f"{field}: {display_value}", fg="white", bg="black").pack(anchor="w", padx=30)

    # Add the cart summary footer
    add_summary_footer(main_frame, cart)

    # Function to confirm the order and show a thank you message
    def confirm():
        clear_frame()
        tk.Label(main_frame, text="Thank you for your order!", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=(20, 5))

        # Draw a checkmark symbol using a canvas (to symbolize order confirmation)
        canvas = tk.Canvas(main_frame, width=100, height=100, bg="black", highlightthickness=0)
        canvas.pack()
        canvas.create_oval(10, 10, 90, 90, outline="white", width=3)
        canvas.create_line(30, 50, 45, 65, fill="white", width=4)
        canvas.create_line(45, 65, 70, 35, fill="white", width=4)

        # Display the order number
        tk.Label(main_frame, text="ORDER NUMBER", font=("Helvetica", 12), fg="white", bg="black").pack(pady=(10, 0))
        tk.Label(main_frame, text="#000001", font=("Helvetica", 16, "bold"), fg="white", bg="black").pack(pady=(0, 10))

        # Display the order summary (items in the cart)
        tk.Label(main_frame, text="ORDER SUMMARY", font=("Helvetica", 14, "bold"), fg="white", bg="black").pack(pady=(10, 5))
        for item in cart.get_items():
            name = item["name"]
            qty = item["quantity"]
            price = item["price"]
            if qty > 0:
                tk.Label(main_frame, text=f"{name}  {qty} x ${price:.2f}", fg="white", bg="black").pack()

        # Add the cart summary footer
        add_summary_footer(main_frame, cart)

        # Button to return to the homepage after confirming the order
        tk.Button(main_frame, text="HOMEPAGE", font=("Helvetica", 14, "bold"),
                  bg="#ED1C24", fg="white", padx=20, pady=10, bd=0)

    # Button to place the order and confirm the payment
    tk.Button(main_frame, text="PLACE ORDER", font=("Helvetica", 14, "bold"), bg="#28a745", fg="white",
              padx=20, pady=10, bd=0, command=confirm).pack(pady=15)
