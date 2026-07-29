from product import (
    Shop,
    ProductError,
    DuplicateBarcodeError,
    ProductNotFoundError,
    InsufficientStockError,
    InvalidQuantityError,
)

store = Shop()


def prompt_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("That is not a valid number. Please try again!")


def add_product_flow():
    name = input("Enter the name of the product: ")
    qty = prompt_int("Enter the number of quantity: ")
    price = prompt_int("Enter the price of the product: ")
    barcode = input("Enter the barcode of the product: ")
    try:
        store.add_product(name, qty, barcode, price)
        print(f"Added '{name}' to inventory.")
    except DuplicateBarcodeError as e:
        print(e)
    except ProductError as e:
        print(f"Could not add product: {e}")


def sell_items_flow():
    barcode = input("Enter the product barcode: ")
    qty = prompt_int("Enter the quantity of the item to be sold: ")
    try:
        store.sell_items(barcode, qty)
        print(f"Sold {qty} unit(s) of barcode {barcode}.")
    except (ProductNotFoundError, InsufficientStockError, InvalidQuantityError) as e:
        print(e)


def search_flow():
    barcode = input("Enter the product barcode you wanna search: ")
    try:
        product = store.get_product(barcode)
    except ProductNotFoundError as e:
        print(e)
        return

    print(product.get_name(), product.get_qty(), product.get_price())
    print(f"Enter 1 to increase stock of the {product.get_name()}")
    print("Enter 2 to decrease stock:")
    print("Enter 3 to delete the product completely:")
    choice = prompt_int("Enter your answer here:: ")

    try:
        if choice == 1:
            amount = prompt_int("Enter the number of quantity you want to add: ")
            store.increase_product_stock(barcode, amount)
        elif choice == 2:
            amount = prompt_int("Enter the number of quantity you want to delete: ")
            store.decrease_product_stock(barcode, amount)
        elif choice == 3:
            store.delete_product(barcode)
            print("Product deleted.")
        else:
            print("Please enter a valid input!!")
    except (InsufficientStockError, InvalidQuantityError, ProductNotFoundError) as e:
        print(e)


def main():
    print("***************** INVENTORY MANAGEMENT SYSTEM *****************")
    while True:
        print("\nEnter 1 to add product!")
        print("Enter 2 to sell items!")
        print("Enter 3 to search product!")
        print("Enter 4 to view sales!")
        print("Enter 5 to exit the system!")
        choice = prompt_int("Enter your input:: ")

        if choice == 1:
            add_product_flow()
        elif choice == 2:
            sell_items_flow()
        elif choice == 3:
            search_flow()
        elif choice == 4:
            print("Sales till now::", store.get_sales_amount())
        elif choice == 5:
            print("Sales till now::", store.get_sales_amount())
            print("Goodbye!")
            break
        else:
            print("invalid input")


if __name__ == "__main__" : 
    main() 