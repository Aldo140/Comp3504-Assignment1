from inventoryManager import InventoryManager
from splicer import Splicer
from command import Command

commands = []
commands.append(Command("add", ['int', 'int'])) # add <item_id> <quantity>
commands.append(Command("remove", ['int', 'int'])) # remove <item_id> <quantity>
commands.append(Command("quit", [])) # quit
commands.append(Command("search", ['str'])) # search "<partial item name or number>"
commands.append(Command("list", [])) # list
commands.append(Command("order", [])) # list

base_path = 'Files for Retail store/Files for Retail store/'
stock = InventoryManager(base_path)
characters = ["\"", " "]
inputSplicer = Splicer(characters, True)
while True:
    print("Basic Commands")
    print("Note: only replace <value> with the appropriate value.")
    print("Note: The | divides the command fromat and it's description.")
    print("Note: all commands are cases sensitive.")
    print("add <item_id> <quantity> | adds the quantity of the specified item to the inventory")
    print("remove <item_id> <quantity> | removes the quantity of the specified item from the inventory")
    print("search \"<partial item name or number>\" | searches for the item with whole or partially matching ID or name")
    print("list | lists all the items")
    print("order | generates the receipt for the stock that needs to be ordered.")
    # print("")
    print("quit | closes the program")
    cmd = inputSplicer.splice(input())
    # print(cmd[1:])
    if commands[0].checkCall(cmd[0]):
        stock.addStock(cmd[1], cmd[2])
    elif commands[1].checkCall(cmd[0]):
        stock.removeStock(cmd[1], cmd[2])
    elif commands[2].checkCall(cmd[0]):
        quit()
    elif commands[3].checkCall(cmd[0]):
        stock.searchItem(cmd[1])
    elif commands[4].checkCall(cmd[0]):
        stock.searchItem("")
    elif commands[5].checkCall(cmd[0]):
        stock.dateTicker()

# old test/sample code
# print(stock.getDate())
# print("=" * 10) 
# print(stock.getStock())
# print("=" * 10)
# print(stock.getSuppliers())
# stolen = stock.searchItem("Nic")
# stock.removeStock(stolen[0].item_id, 230)
# stolen = stock.searchItem("Nic")
# stock.dateTicker()
# print("=" * 15)
# splicer = Splicer(characters, True)
# commandTest = splicer.splice("add \"Barge Bogs\" 9 there")
# for i in commandTest:
#     print(i)