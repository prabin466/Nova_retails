import pandas as pd
import os
from pathlib import Path
import json
from datetime import datetime, timedelta
import random

# Create paths for data
project_root = Path.cwd().parent
raw_path = os.path.join(project_root, "data", "raw")
curated_path = os.path.join(project_root, "data", "curated")
models_path = os.path.join(project_root, "data", "models")

os.makedirs(os.path.join(raw_path, "inventory_stream"), exist_ok=True)
os.makedirs(curated_path, exist_ok=True)
os.makedirs(models_path, exist_ok=True)

# Basic Data
store_ids = ["X001", "X002"]
sku_ids = ["P001", "P002", "P003"]
customer_ids = ["C001", "C002", "C003", "C004"]
start_date = datetime(2025, 8, 30)
num_days = 6
base_prices = {"P001": 100, "P002": 200, "P003": 300}

# Generate sales data
sales_data = []

for day in range(num_days):
    date = (start_date + timedelta(days=day)).strftime("%Y%m%d")
    for store_id in store_ids:
        for sku_id in sku_ids:
            # Generate multiple transactions per SKU/store/day
            for _ in range(random.randint(5, 10)):  # 5-10 transactions
                quantity = random.randint(5, 50)
                # ±10% variation per unit
                unit_price = base_prices[sku_id] * random.uniform(0.9, 1.1)
                price = unit_price * quantity
                sales_data.append({
                    "txn_id": f"T{random.randint(10000,99999)}",
                    "date": date,
                    "sku_id": sku_id,
                    "store_id": store_id,
                    "customer_id": random.choice(customer_ids),
                    "quantity": quantity,
                    "price": round(price, 2),
                })

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv(os.path.join(raw_path, "sales_data.csv"), index=False)
print("sales_data.csv created:", sales_df.shape)


#  Generate customer summary
customers_data = []
for c in customer_ids:
    last_purchase_days = random.randint(0, 10)
    total_orders = random.randint(20, 100)
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

# Generate inventory stream
# Inventory stream aligned with sales dates
num_days = 6  # same as sales data: 2025-08-30 to 2025-09-04
batches_per_day = 1  # can increase if you want more frequent micro-batches

for day in range(num_days):
    for batch_num in range(batches_per_day):
        batch = []
        for store_id in store_ids:
            for sku_id in sku_ids:
                # Random time during the day for realism
                random_hour = random.randint(0, 23)
                random_minute = random.randint(0, 59)
                random_second = random.randint(0, 59)

                ts = (start_date + timedelta(days=day, hours=random_hour,
                                             minutes=random_minute, seconds=random_second)).strftime(
                    "%Y-%m-%dT%H:%M:%S")

                batch.append({
                    "timestamp": ts,
                    "store_id": store_id,
                    "sku_id": sku_id,
                    "on_stock": random.randint(20, 100),
                })

        batch_file = os.path.join(raw_path, "inventory_stream", f"batch_{day * batches_per_day + batch_num + 1}.json")
        with open(batch_file, "w") as f:
            for record in batch:
                f.write(json.dumps(record) + "\n")

print("Inventory stream JSON files created in:", os.path.join(raw_path, "inventory_stream"))

