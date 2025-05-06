import csv
import random
import time
from datetime import datetime

products = [
    ("Electronics", "Smartphone", 699.99),
    ("Fashion", "T-Shirt", 19.99),
    ("Books", "Fiction Novel", 12.99),
    ("Fashion", "Jeans", 49.99),
    ("Electronics", "Laptop", 999.99)
]

customers = ["John Doe", "Jane Smith", "Sam Brown", "Alice White", "Bob Stone"]

order_id = 1002  # starting from next ID

while True:
    category, product, price = random.choice(products)
    quantity = random.randint(1, 3)
    customer = random.choice(customers)
    total = round(quantity * price, 2)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("data/orders.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([order_id, date, customer, category, product, quantity, price, total])
        print(f"🆕 Order Added: {order_id} - {product} x{quantity} (${total})")

    order_id += 1
    time.sleep(5)  # wait 5 seconds before next order
