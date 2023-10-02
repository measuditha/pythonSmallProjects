class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
            else:
                print(f"Error: Not enough {item_name} in stock.")
        else:
            print(f"Error: {item_name} not found in inventory.")

    def view_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

def main():
    inventory = Inventory()

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(item_name, quantity)
        elif choice == '3':
            inventory.view_inventory()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
