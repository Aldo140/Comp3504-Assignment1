import random
from datetime import datetime

class Order:
    """
    The Order class creates an order when stock is low. 
    It generates an order ID, stores the date, items, and calculates the total cost.
    It can also save order details to a text file.
    """
    
    def __init__(self):
        """
        Sets up the Order with a random ID, the current date, 
        an empty list for items, and a starting total cost of zero.
        """
        self.order_id = random.randint(10000, 99999)  # Generate a random 5-digit order ID
        self.date_ordered = datetime.now().strftime('%B %d, %Y')  # Get the current date
        self.items_ordered = []  # List to hold ordered items
        self.total_cost = 0.0  # Starting total cost of the order

    def add_item(self, description, amount, supplier, price_per_item):
        
        self.items_ordered.append((description, amount, supplier))  # Add item to the order
        self.total_cost += amount * price_per_item  # Update the total cost

    def generate_order_line(self, tool_name, quantity, supplier, price):
        """
        Adds an order line if stock is below 10.
        """
        if quantity < 10:
            amount_ordered = 30 - quantity  # Calculate how much to order
            self.add_item(tool_name, amount_ordered, supplier, price)  # Add item to the order

    def write_order_to_file(self):
        """
        Saves the order details to 'orders.txt'.
        """
        with open('orders.txt', 'a') as file:
            file.write(f"ORDER ID.: {self.order_id}\n")  # Write order ID
            file.write(f"Date Ordered: {self.date_ordered}\n\n")  # Write date
            for item in self.items_ordered:
                description, amount, supplier = item
                file.write(f"Item description: {description}\n")  # Write item description
                file.write(f"Amount ordered: {amount}\n")  # Write quantity ordered
                file.write(f"Supplier: {supplier}\n\n")  # Write supplier name
            file.write(f"Total cost: ${self.total_cost:.2f}\n")  # Write total cost
            file.write("="*60 + "\n")