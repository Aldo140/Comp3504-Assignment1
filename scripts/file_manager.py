import os
from Item import Item  # path for Item
from Supplier import Supplier  # path for Supplier

# Define the relative file path
base_path = 'Files for Retail store/Files for Retail store'

def read_items():
    """
    Reads items from a text file and returns a list of Item objects.
    """
    file_path = os.path.join(base_path, 'items.txt')
    items = []
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return items
    
    with open(file_path, 'r') as file:
        for line in file:
            item_id, name, quantity, price, supplier_id = line.strip().split(';')
            item = Item(item_id, name, int(quantity), float(price), supplier_id)
            items.append(item)
    
    return items

def read_suppliers():
    """
    Reads suppliers from a text file and returns a list of Supplier objects.
    """
    file_path = os.path.join(base_path, 'suppliers.txt')
    suppliers = []
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return suppliers
    
    with open(file_path, 'r') as file:
        for line in file:
            supplier_id, company_name, address, sales_person = line.strip().split(';')
            supplier = Supplier(supplier_id, company_name, address, sales_person)
            suppliers.append(supplier)
    
    return suppliers

def print_first_10_items():
    """
    Prints the first 10 lines from items.txt.
    """
    file_path = os.path.join(base_path, 'suppliers.txt')
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return
    
    with open(file_path, 'r') as file:
        for _ in range(10):
            line = file.readline()
            if not line:
                break  # Stop if there are fewer than 10 lines
            print(line.strip())



# Example:
if __name__ == "__main__":
    items = read_items()
    suppliers = read_suppliers()
    
   
    #print("First 10 items from items.txt:")
    #print_first_10_items()
     #Loop through the list and print each item
    for item in items:
        print(item)
