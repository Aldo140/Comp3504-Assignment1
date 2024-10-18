import random
from datetime import datetime

class Order:
    """
    The Order class creates an order when stock is low. 
    It generates an order ID, stores the date, items, and calculates the total cost.
    It can also save order details to a list and return it.
    """
    
    def __init__(self, date):
        """
        Sets up the Order with a random ID, the current date, 
        an empty list for items, and a starting total cost of zero.
        """
        self.order_id = random.randint(10000, 99999)  # Generate a random 5-digit order ID
        self.date_ordered = date
        self.items_ordered = []  # List to hold ordered items
        self.total_cost = 0.0  # Starting total cost of the order
        self.supplier_distribution = {}  # Store distribution for suppliers

    def set_supplier_distribution(self, distribution):
        """
        Sets the percentage distribution of the order across suppliers.
        Example: {'SupplierA': 0.1, 'SupplierB': 0.9, 'SupplierC': 0.0}
        """
        if abs(sum(distribution.values()) - 1.0) > 1e-6:
            raise ValueError("The total percentage distribution must equal 100% (1.0).")
        self.supplier_distribution = distribution

    def add_item(self, description, total_amount, price_per_item):
        """
        Adds items to the order based on the distribution across suppliers
        and updates the total cost.
        """
        if not self.supplier_distribution:
            raise ValueError("Supplier distribution has not been set.")

        for supplier, percentage in self.supplier_distribution.items():
            amount = int(total_amount * percentage)  # Calculate amount for each supplier
            if amount > 0:
                self.items_ordered.append([description, amount, supplier])
                self.total_cost += amount * price_per_item

    def append_order_to_data(self):
        """
        Appends the order details to a list and returns it.
        """
        data = []  # List to hold order details
        
        # Append Order ID and Date
        data.append(f"ORDER ID.:            {self.order_id}")
        data.append(f"Date Ordered:         {self.date_ordered}")
        
        # Append all items ordered
        for item in self.items_ordered:
            description, amount, supplier = item
            data.append(f"Item description:     {description}")
            data.append(f"Amount ordered:       {amount}")
            data.append(f"Supplier:             {supplier}")
        
        # Append the total cost
        data.append(f"Total cost:           ${self.total_cost:.2f}")
        data.append("=" * 60)
        
        return data

    def get_order_details(self):
        """
        Returns the list of items ordered, including description, amount, and supplier.
        """
        return self.items_ordered