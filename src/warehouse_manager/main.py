from warehouse_manager.models import WarehouseItem
from warehouse_manager.services import (
    add_stock,
    calculate_total_warehouse_value,
    decrease_stock,
    find_item_by_code,
    find_low_stock_items,
)


def create_demo_items() -> list[WarehouseItem]:
    return [
        WarehouseItem(code="A001", name="Laptop Pro 15", quantity=4, price=35000.0),
        WarehouseItem(code="A002", name="Wireless Mouse", quantity=25, price=850.0),
        WarehouseItem(code="B001", name="Mechanical Keyboard", quantity=3, price=2800.0),
        WarehouseItem(code="C001", name="USB-C Hub", quantity=15, price=1200.0),
    ]


def print_items(items: list[WarehouseItem]) -> None:
    print("\nWarehouse Inventory:")
    print(f"{'Code':<8} {'Name':<25} {'Qty':<8} {'Price':<10} {'Total':<10}")
    print("-" * 65)
    for item in items:
        print(
            f"{item.code:<8} "
            f"{item.name:<25} "
            f"{item.quantity:<8} "
            f"{item.price:<10.2f} "
            f"{item.total_value:<10.2f}"
        )


def print_menu() -> None:
    print("\n--- WAREHOUSE MANAGEMENT SYSTEM ---")
    print("1. Show all inventory")
    print("2. Find item by code")
    print("3. Stock in (Add quantity)")
    print("4. Stock out (Decrease quantity)")
    print("5. Show total warehouse value")
    print("6. Show low stock items")
    print("7. Exit")


def run_menu(items: list[WarehouseItem]) -> None:
    while True:
        print_menu()
        command = input("Select command: ").strip()

        if command == "1":
            print_items(items)

        elif command == "2":
            code = input("Enter item code: ").strip()
            item = find_item_by_code(items, code)
            if item:
                print(f"\nFound: {item.name} | Qty: {item.quantity} | Price: {item.price:.2f}")
            else:
                print("\nItem not found.")

        elif command == "3":
            code = input("Enter item code: ").strip()
            item = find_item_by_code(items, code)
            if item:
                try:
                    amount = int(input("Enter quantity to add: "))
                    add_stock(item, amount)
                    print(f"\nSuccess! New quantity for {item.name}: {item.quantity}")
                except ValueError:
                    print("\nInvalid number format.")
            else:
                print("\nItem not found.")

        elif command == "4":
            code = input("Enter item code: ").strip()
            item = find_item_by_code(items, code)
            if item:
                try:
                    amount = int(input("Enter quantity to write off: "))
                    success = decrease_stock(item, amount)
                    if success:
                        print(f"\nSuccess! Remaining quantity for {item.name}: {item.quantity}")
                    else:
                        print("\nError: Insufficient stock or invalid amount.")
                except ValueError:
                    print("\nInvalid number format.")
            else:
                print("\nItem not found.")

        elif command == "5":
            total = calculate_total_warehouse_value(items)
            print(f"\nTotal warehouse inventory value: {total:.2f} UAH")

        elif command == "6":
            low_stock = find_low_stock_items(items, threshold=5)
            print_items(low_stock)

        elif command == "7":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Please try again.")


def main() -> None:
    items = create_demo_items()
    run_menu(items)


if __name__ == "__main__":
    main()