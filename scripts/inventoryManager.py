from datetime import datetime, timedelta
# import copy
from Order_Class import Order
from file_manager import FileManager
from splicer import Splicer
from Item import Item
from Supplier import Supplier
class InventoryManager():
    stock = []
    suppliers = []
    currentOrder = None
    date = None
    shiftDate = 0

    def __init__(self, dataLocation):
        characters = [";", '\n']
        self.date = datetime.now()
        splicer = Splicer(characters)
        itemsFile = FileManager(dataLocation + 'items.txt')
        suppliersFile = FileManager(dataLocation + 'suppliers.txt')
        # self.date = datetime.datetime.today()
        # self.date.append(datetime.today().year)
        # self.date.append(datetime.today().month)
        # self.date.append(datetime.today().day)
        itemsData = itemsFile.read_file()
        suppliersData = suppliersFile.read_file()
        for i in itemsData:
            self.stock.append(Item(*splicer.splice(i)))
        for i in suppliersData:
            self.suppliers.append(Supplier(*splicer.splice(i)))

    def getDate(self):
        # print(da + timedelta(2))
        return self.date
    
    def setDate(self, newDate):
        date = newDate

    def getStock(self):
        return self.stock
    
    def setStock(self, newStockList):
        for item in newStockList:
            self.stock.add(Item(item[0], item[1], item[2], item[3], item[4]))
    
    def getSuppliers(self):
        return self.suppliers
    
    def setSuppliers(self, newSuppliersList):
        for supplier in newSuppliersList:
            self.suppliers.add(Item(supplier[0], supplier[1], supplier[2], supplier[3]))

    def removeStock(self, id, quantity):
        item = self.getItem(id)
        item.quantity = item.quantity - int(quantity)
        if item.quantity < 0:
            print("Quantity < 0 | oh no")

    def getItem(self, id):
        for item in self.stock:
            if item.item_id == int(id):
                return item
            
    def addStock(self, id, quantity):
        item = self.getItem(id)
        item.quantity = item.quantity + int(quantity)

    def getStockWarnings(self):
        low = []
        for item in self.stock:
            if item.quantity <= 10:
                print(item.item_id, item.quantity)
                low.append(item.item_id)
        return low
    
    def dateTicker(self):
        self.shiftDate += 1
        toOrder = self.getStockWarnings()
        for id in toOrder:
            self.addOrderItem(id)
        self.currentOrder.write_order_to_file()

    def addOrderItem(self, id):
        item = self.getItem(id)
        amount = 30 - item.quantity
        self.currentOrder = Order()#(self.date + timedelta(self.shiftDate)).strftime('%B %d, %Y'))
        self.currentOrder.add_item(item.name, amount, self.searchSupplier(str(item.supplier_id)).company_name, item.price)

    def searchSupplier(self, searchable):
        for supplier in self.suppliers:
            if str(supplier.supplier_id).__contains__(searchable):
                # print(suppliers)
                return supplier
    
    def searchItem(self, searchable):
        matches = []

        for item in self.stock:
            if str(item.item_id).__contains__(searchable) or item.name.__contains__(searchable):
                print(item)
                matches.append(item)
        return matches