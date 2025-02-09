import csv

import requests

DATA_URL = "https://raw.githubusercontent.com/AegisVP/goit-algo2-hw/refs/heads/HW03/HW03/generated_items_data.csv"


def load_data_from_csv(url):
    response = requests.get(url)
    response.raise_for_status()
    data = []
    reader = csv.DictReader(response.text.strip().split('\n'))
    for row in reader:
        row['ID'] = int(row['ID'])
        row['Price'] = float(row['Prpipice'])
        data.append(row)
    return data


def add_item(structure, item):
    structure[item['ID']] = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': item['Price'],
    }


def range_query(structure, min_price, max_price):
    return [value for value in structure.values() if min_price <= value['Price'] <= max_price]