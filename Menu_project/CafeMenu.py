menu = {
    "coffee": 50,
    "pizza": 150,
    "sandwich": 120,
    "icecream": 60,
    "maggi": 40
}

print("Welcome to CAFFEE MENU")
for item, price in menu.items():
    print(f"{item.capitalize()} : {price}")

total_order = 0
ordered_items = []

while True:
    item = input("\nEnter the item you want to order: ").strip().lower()
    
    if item in menu:
        total_order += menu[item]
        ordered_items.append(item)
        print(f"Your order for {item} is confirmed.")
    else:
        print(f"Sorry, {item} is not available.")

    more = input("Do you want to order more items? (Yes/No): ").strip().lower()
    if more == "no":
        break
    elif more != "yes":
        print("Invalid input. Assuming you want to stop ordering.")
        break

# Final bill
if ordered_items:
    print(f"\nYou have ordered: {', '.join(ordered_items)}")
    print(f"Your total bill is: {total_order}")
else:
    print("\nYou have not ordered any available items.")
