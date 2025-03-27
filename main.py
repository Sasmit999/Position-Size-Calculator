import tkinter as tk
from tkinter import ttk, messagebox

# Forex currency pairs list
currency_pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "USD/CHF", "NZD/USD", "EUR/GBP", "EUR/JPY"]

# Function to calculate lot size
def calculate_lot():
    try:
        account_size = float(account_entry.get())
        risk_percent = float(risk_entry.get())
        stop_loss = float(sl_entry.get())
        selected_currency = currency_var.get()
        
        if account_size <= 0 or risk_percent <= 0 or stop_loss <= 0:
            raise ValueError("Values must be greater than zero.")
        
        risk_amount = (risk_percent / 100) * account_size
        lot_size = risk_amount / stop_loss / 10  # Standard forex lot size calculation
        
        result_label.config(text=f"{selected_currency} Lot Size: {lot_size:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI Setup
root = tk.Tk()
root.title("Forex Lot Size Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))

# Labels and Entries
ttk.Label(root, text="Account Size ($):").pack(pady=5)
account_entry = ttk.Entry(root)
account_entry.pack(pady=5)

ttk.Label(root, text="Risk Percentage (%):").pack(pady=5)
risk_entry = ttk.Entry(root)
risk_entry.pack(pady=5)

ttk.Label(root, text="Stop Loss (Pips):").pack(pady=5)
sl_entry = ttk.Entry(root)
sl_entry.pack(pady=5)

# Currency Selection
ttk.Label(root, text="Select Currency:").pack(pady=5)
currency_var = tk.StringVar()
currency_combobox = ttk.Combobox(root, textvariable=currency_var, values=currency_pairs, state="readonly")
currency_combobox.pack(pady=5)
currency_combobox.current(0)

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate Lot Size", command=calculate_lot)
calculate_button.pack(pady=15)

# Result Label
result_label = ttk.Label(root, text="Recommended Lot Size: ")
result_label.pack(pady=10)

# Run the App
root.mainloop()
