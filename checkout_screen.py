import tkinter as tk

# Shared form data state for customer and payment info
form_data = {
    "customer": {},
    "payment": {}
}

def show_customer_info_screen(main_frame, clear_frame, show_cart_screen, show_payment_screen, cart):
    clear_frame()

    tk.Label(main_frame, text="CUSTOMER INFO", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=10)

    entries = {}
    fields = ["Name", "Phone Number", "Email Address", "Movie", "Seat Number"]

    for field in fields:
        tk.Label(main_frame, text=field, fg="white", bg="black", anchor="w").pack(fill="x", padx=30)
        entry = tk.Entry(main_frame)
        entry.pack(fill="x", padx=30, pady=5)
        entries[field] = entry

    def next_step():
        for field in fields:
            form_data["customer"][field] = entries[field].get()
        show_payment_screen(main_frame, clear_frame, show_customer_info_screen, show_summary_screen, cart)

    add_summary_footer(main_frame, cart)

    tk.Button(main_frame, text="Proceed to Payment Method", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0, command=next_step).pack(pady=(10, 5))
    tk.Button(main_frame, text="Go Back", font=("Helvetica", 12), bg="gray", fg="white",
              command=lambda: show_cart_screen(main_frame, clear_frame, None, show_customer_info_screen, cart)).pack()

def show_payment_screen(main_frame, clear_frame, show_customer_info_screen, show_summary_screen, cart, go_home):
    clear_frame()

    tk.Label(main_frame, text="PAYMENT METHOD INFO", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=10)

    entries = {}
    fields = ["Name on Card", "Card Number", "Expiration Date", "CVV", "Billing Address", "City", "State", "Zip Code"]

    for field in fields:
        tk.Label(main_frame, text=field, fg="white", bg="black", anchor="w").pack(fill="x", padx=30)
        entry = tk.Entry(main_frame)
        entry.pack(fill="x", padx=30, pady=5)
        entries[field] = entry

    def next_step():
        for field in fields:
            form_data["payment"][field] = entries[field].get()
        show_summary_screen(main_frame, clear_frame, show_payment_screen, go_home, cart)

    add_summary_footer(main_frame, cart)

    tk.Button(main_frame, text="Proceed to Order Summary", font=("Helvetica", 14, "bold"),
              bg="#ED1C24", fg="white", padx=20, pady=10, bd=0, command=next_step).pack(pady=(10, 5))
    tk.Button(main_frame, text="Go Back", font=("Helvetica", 12), bg="gray", fg="white",
              command=lambda: show_customer_info_screen(main_frame, clear_frame, None, show_payment_screen, cart)).pack()

def add_summary_footer(main_frame, cart):
    subtotal = cart.get_subtotal()
    tax = round(subtotal * 0.0625, 2)
    total = round(subtotal + tax, 2)
    count = cart.get_total_items()

    footer = tk.Frame(main_frame, bg="black")
    footer.pack(pady=10)

    def row(label, value):
        f = tk.Frame(footer, bg="black")
        f.pack(anchor="e", padx=20)
        tk.Label(f, text=label, fg="white", bg="black", font=("Helvetica", 12)).pack(side="left")
        tk.Label(f, text=f"${value:.2f}" if isinstance(value, float) else value, fg="white", bg="black", font=("Helvetica", 12, "bold")).pack(side="right")

    row(f"Subtotal ({count})", subtotal)
    row("Taxes", tax)
    row("Total", total)

def show_summary_screen(main_frame, clear_frame, go_back, go_home, cart):
    clear_frame()
    tk.Label(main_frame, text="ORDER SUMMARY", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=10)

    for field, value in form_data["customer"].items():
        tk.Label(main_frame, text=f"{field}: {value}", fg="white", bg="black").pack(anchor="w", padx=30)

    tk.Label(main_frame, text="\nPayment Info", font=("Helvetica", 14, "bold"), fg="white", bg="black").pack(anchor="w", padx=30)
    for field, value in form_data["payment"].items():
        display_value = value if "Card" not in field and field != "CVV" else "****"
        tk.Label(main_frame, text=f"{field}: {display_value}", fg="white", bg="black").pack(anchor="w", padx=30)

    add_summary_footer(main_frame, cart)

    def confirm():
        clear_frame()
        tk.Label(main_frame, text="Thank you for your order!", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=(20, 5))

        canvas = tk.Canvas(main_frame, width=100, height=100, bg="black", highlightthickness=0)
        canvas.pack()
        canvas.create_oval(10, 10, 90, 90, outline="white", width=3)
        canvas.create_line(30, 50, 45, 65, fill="white", width=4)
        canvas.create_line(45, 65, 70, 35, fill="white", width=4)

        tk.Label(main_frame, text="ORDER NUMBER", font=("Helvetica", 12), fg="white", bg="black").pack(pady=(10, 0))
        tk.Label(main_frame, text="#000001", font=("Helvetica", 16, "bold"), fg="white", bg="black").pack(pady=(0, 10))

        tk.Label(main_frame, text="ORDER SUMMARY", font=("Helvetica", 14, "bold"), fg="white", bg="black").pack(pady=(10, 5))
        for item in cart.get_items():
            name = item["name"]
            qty = item["quantity"]
            price = item["price"]
            if qty > 0:
                tk.Label(main_frame, text=f"{name}  {qty} x ${price:.2f}", fg="white", bg="black").pack()

        add_summary_footer(main_frame, cart)

        tk.Button(main_frame, text="HOMEPAGE", font=("Helvetica", 14, "bold"),
                  bg="#ED1C24", fg="white", padx=20, pady=10, bd=0,
                  command=lambda: go_home()).pack(pady=20)

    tk.Button(main_frame, text="PLACE ORDER", font=("Helvetica", 14, "bold"), bg="#28a745", fg="white",
              padx=20, pady=10, bd=0, command=confirm).pack(pady=15)

    tk.Button(main_frame, text="Go Back", font=("Helvetica", 12), bg="gray", fg="white",
              command=lambda: go_back(main_frame, clear_frame, show_summary_screen, cart)).pack(pady=5)