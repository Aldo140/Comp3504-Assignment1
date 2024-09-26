class Supplier:
    def __init__ (self, Supplier_id, Comapany_name, address, sales_person): 
        self.supplier_id = Supplier_id             # Unique identifier for Supplier
        self.comapany_name = Comapany_name         # Comapany name 
        self.address = address                     # Address
        self.sales_person = sales_person           # Sales person
    
    
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        if value > 0:
            self._supplier_id = value
        else:
            raise ValueError("Supplier ID must be positive.")

    # Getter and Setter for company_name
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        if isinstance(value, str) and value:
            self._company_name = value
        else:
            raise ValueError("Company name must be a non-empty string.")

    # Getter and Setter for address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, str) and value:
            self._address = value
        else:
            raise ValueError("Address must be a non-empty string.")

    # Getter and Setter for sales_person
    @property
    def sales_person(self):
        return self._sales_person

    @sales_person.setter
    def sales_person(self, value):
        if isinstance(value, str) and value:
            self._sales_person = value
        else:
            raise ValueError("Sales person must be a non-empty string.")

    # Method to update the sales person
    def update_sales_person(self, new_sales_person):
        self.sales_person = new_sales_person

    # Proper string representation
    def __str__(self):
        return ("Supplier[ID: {self.supplier_id}, Company Name: {self.company_name}, "
                "Address: {self.address}, Sales Person: {self.sales_person}]")
