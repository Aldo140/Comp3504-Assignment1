from inventoryManager import InventoryManager

stock = InventoryManager()
print(stock.getDate())
print("=" * 10)
print(stock.getStock())
print("=" * 10)
print(stock.getSuppliers())
stock.searchItem("")