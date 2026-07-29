class ProductError(Exception):
    pass


class DuplicateBarcodeError(ProductError):
    pass         


class ProductNotFoundError(ProductError):
    pass            


class InsufficientStockError(ProductError):
    pass                   


class InvalidQuantityError(ProductError):
    pass                       


class Product:
    def __init__(self, name, qty, barcode, price):
        if qty < 0:
            raise InvalidQuantityError("Initial quantity cannot be negative.")
        if price < 0:
            raise ProductError("Price cannot be negative.")
        self.name = name
        self.qty = qty
        self.barcode = barcode
        self.price = price

    def get_name(self):
        return self.name

    def get_qty(self):
        return self.qty

    def get_barcode(self):
        return self.barcode

    def get_price(self):
        return self.price

    def increase_stock(self, added_qty):
        if added_qty <= 0:
            raise InvalidQuantityError("Quantity to add must be positive.")
        self.qty += added_qty

    def decrease_stock(self, decreased_qty):
        if decreased_qty <= 0:
            raise InvalidQuantityError("Quantity to remove must be positive.")
        if decreased_qty > self.qty:
            raise InsufficientStockError(
                f"Only {self.qty} in stock, cannot remove {decreased_qty}."
            )
        self.qty -= decreased_qty

    def change_name(self, new_name):
        self.name = new_name

    def change_price(self, updated_price):
        if updated_price < 0:
            raise ProductError("Price cannot be negative.")
        self.price = updated_price


class Shop:
    def __init__(self):
        self.inventory = {}
        self.sales_amount = 0

    def add_product(self, name, qty, barcode, price):
        if barcode in self.inventory:
            raise DuplicateBarcodeError(
                f"Product with barcode '{barcode}' already exists."
            )
        self.inventory[barcode] = Product(name, qty, barcode, price)

    def sell_items(self, barcode, qty):
        product = self._get_product(barcode)
        product.decrease_stock(qty)  
        self.sales_amount += product.get_price() * qty

    def get_product(self, barcode):
        # for callers which only want info(eg:CLI) 
        return self._get_product(barcode) 

    def increase_product_stock(self, barcode, amount):
        self._get_product(barcode).increase_stock(amount)

    def decrease_product_stock(self, barcode, amount):
        self._get_product(barcode).decrease_stock(amount)

    def delete_product(self, barcode):
        self._get_product(barcode)  # validates existence, raises if missing
        del self.inventory[barcode]

    def get_sales_amount(self):
        return self.sales_amount

    def _get_product(self, barcode):
        if barcode not in self.inventory:
            raise ProductNotFoundError(f"No product with barcode '{barcode}'.")
        return self.inventory[barcode]  