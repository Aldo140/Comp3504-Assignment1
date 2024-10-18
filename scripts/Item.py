class Item:
<<<<<<< HEAD
    def __init__(self, item_id, name, quantity, price, supplier_id):
        self.item_id = item_id            # Unique identifier for the item
=======
    def __init__ (self, item_id, name, quantity, price, supplier_id):
        self.item_id = int(item_id)          # Unique identifier for the item
>>>>>>> upstream/main
        self.name = name                  # Name of the tool
        self.quantity = int(quantity)          # Quantity in stock
        self.price = price                # Price of the tool
        self.supplier_id = int(supplier_id)   # Supplier identifier

<<<<<<< HEAD
    def update_quantity(self, amount):   # Update quantity
=======
     # Getter and Setter for item_id
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        if int(value) > 0:
            self._item_id = int(value)
        else:
            raise ValueError("Item ID must be positive.")

    # Getter and Setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter and Setter for quantity
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if int(value) >= 0:
            self._quantity = int(value)
        else:
            raise ValueError("Quantity cannot be negative.")

    # Getter and Setter for price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if float(value) >= 0:
            self._price = float(value)
        else:
            raise ValueError("Price cannot be negative.")

    # Getter and Setter for supplier_id
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        if int(value) > 0:
            self._supplier_id = int(value)
        else:
            raise ValueError("Supplier ID must be positive.")

    def update_quantity(self, amount):    # Update quantity
>>>>>>> upstream/main
        self.quantity += amount

    def update_price(self, new_price):    # Update price
        self.price = new_price

<<<<<<< HEAD
    def __str__(self):  # String representation
        return f"Item[ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Supplier ID: {self.supplier_id}]"
=======
    def __str__(self):                    # String representation
        return (f"Item[ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, "
                f"Price: {self.price}, Supplier ID: {self.supplier_id}]")
    
    def __repr__(self):
        return self.__str__()
>>>>>>> upstream/main
