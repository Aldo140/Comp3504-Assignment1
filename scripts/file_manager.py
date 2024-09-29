import os
from Item import Item  
from Supplier import Supplier  

# file_manager.py
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        """
        Reads the file and returns its content.
        """
        try:
            with open(self.file_name, 'r') as file:
                content = file.readlines()
            return content
        except FileNotFoundError:
            print(f"{self.file_name} not found.")
            return []
    
    def write_file(self, data):
        """
        Writes the given data to the file.
        """
        with open(self.file_name, 'a') as file:  # Append mode
            for line in data:
                file.write(line + '\n')
        print(f"Data successfully written to {self.file_name}")
