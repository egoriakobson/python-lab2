# Sample E-commerce Inventory Database
inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

for sku, item in inventory.items():
    if item["category"] == "Electronics":
        item["price"] = item["price"] * 0.85  # Apply a 15% discount to electronics

    if item["stock_count"] == 0:
        item["restock_urgent"] = True  # Mark items with zero stock for urgent restocking

    if "last sold" not in item:
        item.setdefault("last sold", "Never")  # Set default value for last sold if not present

print(inventory)