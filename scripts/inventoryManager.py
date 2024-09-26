from datetime import datetime, timedelta
import Item, Supplier, copy
from Order_Class import Order
from file_manager import read_items, read_suppliers
class InventoryManager():
    stock = []
    suppliers = []
    currentOrder = None
    date = []
    shiftDate = 0

    def __init__(self):
        # self.date = datetime.datetime.today()
        self.date.append(datetime.today().year)
        self.date.append(datetime.today().month)
        self.date.append(datetime.today().day)
        self.stock = read_items()
        self.suppliers = read_suppliers()

    def getDate(self):
        # print(datetime.now() + timedelta(2))
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
        item.update_quantity(-quantity)
        if item.quantity < 0:
            print("Quantity < 0 | oh no")

    def getItem(self, id):
        for item in self.stock:
            if item.item_id == id:
                return item
            
    def addStock(self, id, quantity):
        item = self.getItem(self, id)
        item.updatequantity(item.quantity + quantity)

    def getStockWarnings(self):
        low = []
        for item in self.stock:
            if item.quantity <= 10:
                low.append(item.item_id)
        return low
    
    def dateTicker(self):
        self.shiftDate += 1
        toOrder = self.getStockWarnings()
        for id in toOrder:
            self.addOrderItem(id)

    def addOrderItem(self, id):
        item = self.getItem(id)
        amount = 30 - item.quantity
        self.currentOrder = Order()
        self.currentOrder.add_item(item.name, amount, item.supplier_id, item.price)
        self.currentOrder.write_order_to_file()


    def searchItem(self, searchable):
        matches = []

        for item in self.stock:
            if str(item.item_id).__contains__(searchable) or item.name.__contains__(searchable):
                print(item)
                matches.append(item)
        return matches