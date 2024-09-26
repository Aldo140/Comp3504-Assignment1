from inventoryManager import InventoryManager

stock = InventoryManager()
print(stock.getDate())
print("=" * 10)
print(stock.getStock())
print("=" * 10)
print(stock.getSuppliers())
stolen = stock.searchItem("Nic")
stock.removeStock(stolen[0].item_id, 38)
stolen = stock.searchItem("Nic")
stock.dateTicker()
