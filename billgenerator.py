import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

def generate_bill():
    try:
        customer_name = entry_name.get().strip()
        contact = entry_contact.get().strip()
        amt = float(entry_amt.get())
        gst = float(entry_gst.get())
        tip = float(entry_tip.get())
        payment_method = payment_var.get()

        if not customer_name or not contact:
            messagebox.showerror("Input Error", "Customer Name & Contact are required!")
            return
        if amt <= 0:
            messagebox.showerror("Input Error", "Amount must be positive!")
            return
        if gst < 0 or tip < 0:
            messagebox.showerror("Input Error", "GST and Tip cannot be negative!")
            return

        gst_amt = amt * (gst / 100)
        sgst = gst_amt / 2
        cgst = gst_amt / 2
        tip_amt = amt * (tip / 100)
        final_amt = amt + gst_amt + tip_amt
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bill_number = f"SC{datetime.now().strftime('%Y%m%d%H%M%S')}"

        bill_content = f"""
{"*"*40}
{" "*10}SAM'S COFFEEWORK ☕
{" "*5}Block -23, Metro Mall, Kalyan
{" "*8}Contact: +91-8928575445
{" "*7}www.samscoffee.com
{"*"*40}

Bill No.      : {bill_number}
Date          : {dt}
Customer Name : {customer_name}
Contact No.   : {contact}

{"="*40}
Item                Amount (Rs.)
{"-"*40}
Subtotal            : ₹ {amt:10.2f}
SGST ({gst/2:.1f}%)         : ₹ {sgst:10.2f}
CGST ({gst/2:.1f}%)         : ₹ {cgst:10.2f}
Tip ({tip:.1f}%)           : ₹ {tip_amt:10.2f}
{"-"*40}
TOTAL AMOUNT        : ₹ {final_amt:10.2f}
Payment Method      : {payment_method}
{"="*40}

Thank You for Visiting Sam's Coffeework! ☕
We Hope to See You Again Soon 😊
{"*"*40}
"""

        bill_filename = f"bill_{bill_number}.txt"
        with open(bill_filename, "w", encoding="utf-8") as f:
            f.write(bill_content)

        messagebox.showinfo("Success", f"Bill generated successfully!\nFile: {bill_filename}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values!")

# GUI Setup
root = tk.Tk()
root.title("Billing Software - Sam's Coffeework")
root.geometry("600x600")  
root.configure(bg="#f5e6cc")

# Title Label
tk.Label(root, text="☕ Sam's Coffeework Billing ☕", font=("Arial", 20, "bold"), bg="#f5e6cc", fg="#6d4c41").pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#d7ccc8", padx=15, pady=15, relief="ridge", bd=3)
frame.pack(pady=10, padx=10, fill="both")

# Customer Name
tk.Label(frame, text="Customer Name:", font=("Arial", 12), bg="#d7ccc8").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(frame, font=("Arial", 12), width=25)
entry_name.grid(row=0, column=1)

# Contact Number
tk.Label(frame, text="Contact No.:", font=("Arial", 12), bg="#d7ccc8").grid(row=1, column=0, sticky="w", pady=5)
entry_contact = tk.Entry(frame, font=("Arial", 12), width=25)
entry_contact.grid(row=1, column=1)

# Amount
tk.Label(frame, text="Enter Amount (Rs.):", font=("Arial", 12), bg="#d7ccc8").grid(row=2, column=0, sticky="w", pady=5)
entry_amt = tk.Entry(frame, font=("Arial", 14), width=25)
entry_amt.grid(row=2, column=1)

# GST %
tk.Label(frame, text="Enter GST %:", font=("Arial", 12), bg="#d7ccc8").grid(row=3, column=0, sticky="w", pady=5)
entry_gst = tk.Entry(frame, font=("Arial", 14), width=25)
entry_gst.grid(row=3, column=1)

# Tip %
tk.Label(frame, text="Enter Tip %:", font=("Arial", 12), bg="#d7ccc8").grid(row=4, column=0, sticky="w", pady=5)
entry_tip = tk.Entry(frame, font=("Arial", 14), width=25)
entry_tip.grid(row=4, column=1)

# Payment Method Dropdown
tk.Label(frame, text="Payment Method:", font=("Arial", 12), bg="#d7ccc8").grid(row=5, column=0, sticky="w", pady=5)
payment_var = tk.StringVar(value="Cash")
payment_dropdown = ttk.Combobox(frame, textvariable=payment_var, values=["Cash", "Card", "UPI", "Online Payment"], font=("Arial", 12), state="readonly")
payment_dropdown.grid(row=5, column=1)

# Generate Bill Button
tk.Button(root, text="Generate Bill", command=generate_bill, bg="#8d6e63", fg="white", font=("Arial", 14, "bold"), padx=10, pady=5).pack(pady=20)

# Thank You Label
tk.Label(root, text="Thank You! Visit Again ☕😊", font=("Arial", 16, "italic"), bg="#f5e6cc", fg="#6d4c41").pack(pady=20)

root.mainloop()
