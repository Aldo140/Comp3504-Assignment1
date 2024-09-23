class Item:
    def __init__(self, item_id, name, quantity, price, supplier_id):
        self.item_id = item_id            # Unique identifier for the item
        self.name = name                  # Name of the tool
        self.quantity = quantity          # Quantity in stock
        self.price = price                # Price of the tool
        self.supplier_id = supplier_id    # Supplier identifier

    def update_quantity(self, amount):   # Update quantity
        self.quantity += amount

    def update_price(self, new_price):    # Update price
        self.price = new_price

    def __str__(self):  # String representation
        return f"Item[ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Supplier ID: {self.supplier_id}]"
