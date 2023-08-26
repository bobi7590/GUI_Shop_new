import json
import os

DB_FOLDER_NAME = "db"
PRODUCTS_FILE_NAME = "products.txt"

def get_prod():
    products = []
    with open (os.path.join('db','products.txt'), 'r') as file:
        for lines in file:
            products.append(json.loads(lines.strip()))
        return products

