def main():
  """
  This function simulates a simple inventory management system.
  It demonstrates the use of for loops and if-else statements.
  """

  inventory = {'item1': 10, 'item2': 5, 'item3': 20}  # Sample inventory

  while True:
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Add Items")
    print("3. Sell Items")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      print("\nCurrent Inventory:")
      for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

    elif choice == 2:
      item_to_add = input("Enter the item name to add: ")
      quantity_to_add = int(input("Enter the quantity to add: "))
      if item_to_add in inventory:
        inventory[item_to_add] += quantity_to_add
      else:
        inventory[item_to_add] = quantity_to_add
      print(f"{quantity_to_add} units of {item_to_add} added.")

    elif choice == 3:
      item_to_sell = input("Enter the item name to sell: ")
      quantity_to_sell = int(input("Enter the quantity to sell: "))
      if item_to_sell in inventory:
        if inventory[item_to_sell] >= quantity_to_sell:
          inventory[item_to_sell] -= quantity_to_sell
          print(f"{quantity_to_sell} units of {item_to_sell} sold.")
        else:
          print("Insufficient stock.")
      else:
        print("Item not found in inventory.")

    elif choice == 4:
      print("Exiting...")
      break

    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()