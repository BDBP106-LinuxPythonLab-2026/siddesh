items = []


while True:
    choice = input("\nChoose a number between 1 to 5 according to your wants as => 1 to Add,  2 to Remove,  3 to View,  4 to Sort,  5 to Quit: ").strip()

    if choice == "1":
        new_item = input("Add item: ").strip()
        if any(x.lower() == new_item.lower() for x in items):
            print(f"'{new_item}' is already in the list.")
        elif new_item:
            items.append(new_item)

    elif choice == "2":
        rem = input("Remove item: ").strip()
        found = next((x for x in items if x.lower() == rem.lower()), None)
        if found in items:
            items.remove(found)
            print(f"Removed '{found}'.")
        else:
            print(f"Sorry, '{rem}' is not on the list.")

    elif choice == "3":
        for i, x in enumerate(items, 1):
            print(f"{i}. {x}")

    elif choice == "4":
        items.sort(key=str.lower)
        print("List sorted.")

    elif choice == "5":
        break
