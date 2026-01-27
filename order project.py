import tkinter as tk
from tkinter import messagebox

# ------------------ Data ------------------
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Sandwich": 100,
    "Coffee": 80,
    "Tea": 50
}

order_total = 0

# ------------------ Functions ------------------
def add_item():
    global order_total

    item = item_var.get()
    qty = qty_var.get()

    if qty <= 0:
        messagebox.showerror("Error", "Quantity must be greater than 0")
        return

    price = menu[item] * qty
    order_total += price

    order_list.insert(tk.END, f"{item} x {qty} = ₹{price}")
    total_label.config(text=f"Total: ₹{order_total}")

def clear_order():
    global order_total
    order_total = 0
    order_list.delete(0, tk.END)
    total_label.config(text="Total: ₹0")

# ------------------ GUI ------------------
root = tk.Tk()
root.title("Restaurant Ordering System")
root.geometry("400x450")

tk.Label(root, text="Restaurant Ordering System",
         font=("Arial", 16, "bold")).pack(pady=10)

# Item selection
tk.Label(root, text="Select Item").pack()
item_var = tk.StringVar()
item_var.set(list(menu.keys())[0])  # default value

item_menu = tk.OptionMenu(root, item_var, *menu.keys())
item_menu.pack(pady=5)

# Quantity
tk.Label(root, text="Quantity").pack()
qty_var = tk.IntVar(value=1)
tk.Entry(root, textvariable=qty_var).pack(pady=5)

# Buttons
tk.Button(root, text="Add to Order", command=add_item,
          bg="green", fg="white").pack(pady=10)

tk.Button(root, text="Clear Order", command=clear_order,
          bg="red", fg="white").pack(pady=5)

# Order list
tk.Label(root, text="Your Order").pack(pady=5)
order_list = tk.Listbox(root, width=40, height=10)
order_list.pack()

# Total
total_label = tk.Label(root, text="Total: ₹0",
                       font=("Arial", 14, "bold"))
total_label.pack(pady=10)

root.mainloop()