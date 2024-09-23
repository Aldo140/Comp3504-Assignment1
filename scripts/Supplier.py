class Supplier:
    def __init__ (self, Supplier_id, Comapany_name, address, sales_person): 
        self.supplier_id = Supplier_id             # Unique identifier for Supplier
        self.comapany_name = Comapany_name         # Comapany name 
        self.address = address                     # Address
        self.sales_person = sales_person           # Sales person
    
    def updatesalesperson(self,newsalesperson): # Update sales person
        self.sales_person = newsalesperson
    
    def __str__(self): # Return a string representations
        return ("Supplier ID: %s" % self.supplier_id, "Comapany Name: %s" % self.com, "Address: %s" % self.address, "Sale Person: %s" % self.sales_person)
       
