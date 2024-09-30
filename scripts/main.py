from inventoryManager import InventoryManager
from splicer import Splicer

base_path = 'Files for Retail store/Files for Retail store/'
stock = InventoryManager(base_path)



# old test/sample code
# print(stock.getDate())
# print("=" * 10) 
# print(stock.getStock())
# print("=" * 10)
# print(stock.getSuppliers())
# stolen = stock.searchItem("Nic")
# stock.removeStock(stolen[0].item_id, 38)
# stolen = stock.searchItem("Nic")
# stock.dateTicker()
# print("=" * 15)
# characters = ["\"", " "]
# splicer = Splicer(characters, True)
# commandTest = splicer.splice("add \"Barge Bogs\" 9 there")
# for i in commandTest:
#     print(i)