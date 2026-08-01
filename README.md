# Inventory Management System

A simple command-line inventory management system built in Python to practice
custom exception handling and revise OOP concepts. I Followed principles from Clean Code(Robert C. Martin) — meaningful names,
  small functions, single responsibility. 

## What it does
- Add products (name, quantity, barcode, price)
- Sell items and track total sales
- Search for a product by barcode
- Increase / decrease stock
- Delete a product

## What I practiced
- Custom exceptions (`ProductError`, `DuplicateBarcodeError`,
  `InsufficientStockError`, `ProductNotFoundError`, `InvalidQuantityError`)
- Handling errors gracefully instead of letting the program crash

## How to run

```bash
python main.py
```

## Note
Data is stored in memory only — nothing is saved once the program exits.
