inventory = {
    "pen": (10.0, 50),
    "notebook": (45.0, 20),
    "eraser": (5.0, 100),
    "marker": (30.0, 15),
}

cart = {}

print("Available items:", ", ".join(inventory.keys()))
print("Enter 'item quantity' (e.g., pen 3) or 'done' to checkout.\n")

while True:
    entry = input("Order: ").strip().lower()
    if entry == "done":
        break

    parts = entry.split()
    if len(parts) != 2 or not parts[1].isdigit():
        print("Invalid input. Please enter '<item> <positive quantity>'.")
        continue

    item, qty = parts[0], int(parts[1])

    if qty <= 0:
        print("Quantity must be greater than zero.")
        continue

    if item not in inventory:
        print(f"Unknown item: '{item}'.")
        continue

    price, stock = inventory[item]
    if qty > stock:
        print(f"Insufficient stock for '{item}'. Only {stock} left.")
        continue

    
    cart[item] = cart.get(item, 0) + qty
    inventory[item] = (price, stock - qty)
    print(f"Added {qty} x {item} to cart.")

# to print aligned receipt
print("\n" + "=" * 44)
print("RECEIPT : ".center(44))
print("=" * 44)
print("Item".ljust(12) + "Qty".rjust(6) + "Price".rjust(12) + "Total".rjust(14))
print("-" * 44)

subtotal = 0.0
for item, qty in cart.items():
    price = inventory[item][0]
    line_total = price * qty
    subtotal += line_total
    print(
        f"{item.capitalize().ljust(12)}"
        f"{str(qty).rjust(6)}"
        f"{f'₹{price:.2f}'.rjust(12)}"
        f"{f'₹{line_total:.2f}'.rjust(14)}"
    )

print("-" * 44)
print(f"{'Subtotal:'.ljust(30)}{f'₹{subtotal:.2f}'.rjust(14)}")

discount = subtotal * 0.10 if subtotal > 500 else 0.0
if discount > 0:
    print(f"{'Discount (10%):'.ljust(30)}{f'-₹{discount:.2f}'.rjust(14)}")

final_total = subtotal - discount
print(f"{'Grand Total:'.ljust(30)}{f'₹{final_total:.2f}'.rjust(14)}")
print("=" * 44)

# to print updated inventory
print("\nUPDATED INVENTORY")
print("-" * 44)
for item, (price, stock) in inventory.items():
    status = " [LOW STOCK]" if stock < 10 else ""
    print(f"{item.capitalize().ljust(12)} | ₹{price:>6.2f} | Stock: {stock:>3}{status}")
