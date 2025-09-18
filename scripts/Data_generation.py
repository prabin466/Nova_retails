import pandas as pd
import os
import json
from datetime import datetime, timedelta
import random

# Root data folder relative to this script
data_root = os.path.join(os.path.dirname(__file__), "../data")
raw_path = os.path.join(data_root, "raw")
curated_path = os.path.join(data_root, "curated")
models_path = os.path.join(data_root, "models")

# Create folders if not exist
os.makedirs(os.path.join(raw_path, "inventory_stream"), exist_ok=True)
os.makedirs(curated_path, exist_ok=True)
os.makedirs(models_path, exist_ok=True)


# Generates sales data
sales_data = []
store_ids = ["X001", "X002"]
sku_ids = ["P001", "P002", "P003"]
customer_ids = ["C001", "C002", "C003", "C004"]

start_date = datetime(2025, 8, 30)

# Define base price per SKU to make data logical
base_prices = {"P001": 100, "P002": 200, "P003": 300}

for day in range(6):
    date = (start_date + timedelta(days=day)).strftime("%Y%m%d")
    for store_id in store_ids:
        for sku_id in sku_ids:
            # Quantity between 1-50
            quantity = random.randint(5, 50)
            price = base_prices[sku_id] * quantity  # logical pricing
            sales_data.append({
                "txn_id": f"T{random.randint(1000,9999)}",
                "date": date,
                "sku_id": sku_id,
                "customer_id": random.choice(customer_ids),
                "quantity": quantity,
                "price": round(price, 2),
            })

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv(os.path.join(raw_path, "sales_data.csv"), index=False)
print("sales_data.csv created:", sales_df.shape)

# Generating customer data
customers_data = []
for c in customer_ids:
    last_purchase_days = random.randint(0, 10)
    total_orders = random.randint(10, 100)
    avg_order_value = random.randint(50, 200)
    total_spend = round(total_orders * avg_order_value, 2)
    customers_data.append({
        "customer_id": c,
        "last_purchase": (start_date - timedelta(days=last_purchase_days)).strftime("%Y%m%d"),
        "total_orders": total_orders,
        "total_spend": total_spend
    })

customers_df = pd.DataFrame(customers_data)
customers_df.to_csv(os.path.join(raw_path, "customers_data.csv"), index=False)
print("customers_data.csv created:", customers_df.shape)


# Generating files for stream processing
for i in range(5):  # 5 micro-batch files
    batch = []
    for store_id in store_ids:
        for sku_id in sku_ids:
            batch.append({
                "timestamp": (start_date + timedelta(minutes=i*10)).strftime("%Y-%m-%dT%H:%M:%S"),
                "store_id": store_id,
                "sku_id": sku_id,
                "on_stock": random.randint(20, 100),
            })
    batch_file = os.path.join(raw_path, "inventory_stream", f"batch_{i+1}.json")
    with open(batch_file, "w") as f:
        for record in batch:
            f.write(json.dumps(record) + "\n")
print("Inventory stream JSON files created in:", os.path.join(raw_path, "inventory_stream"))
