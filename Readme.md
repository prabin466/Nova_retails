# 📊 Nova Retail Analytics Pipeline

A **retail analytics pipeline** built with **PySpark** and **MongoDB**, designed to process and analyze sales, customer, and stock data. Supports **daily sales aggregation**, **moving average computations**, **RFM scoring**, and **stock-out risk detection** with a **pre-trained Logistic Regression Model**.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![PySpark](https://img.shields.io/badge/PySpark-3.5.2-orange.svg)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Features

### 💡 Data Processing
- Curates **sales, customer, and stock datasets**.
- Stores processed datasets in **MongoDB collections**.
- Efficient **PySpark transformations** with **caching, partitioning, and broadcast joins**.

### 📊 Customer Analytics
- Computes **Recency, Frequency, Monetary (RFM) scores**.
- Generates **RFM total score** for actionable insights.
- Identifies **top customers likely to respond to promotions**.

### 🛒 Sales Analytics
- Computes **daily item-store sales**.
- Calculates **moving average demand** per SKU.
- Identifies **fast-moving SKUs**.

### 📦 Stock Analytics
- Detects **stock-out risks** for inventory management.
- Highlights **at-risk SKUs by store**.

.

### 🧪 Model Evaluation

- Evaluates binary stock-out prediction using accuracy, precision, recall, F1-score, and class distribution.
- Accepts test data and model path via CLI.
- Outputs a tidy summary table for immediate inspection.

---

## 📂 Project Structure
```
NovaRetail/
├── scripts/
│   ├── data_generation.py        # Script to generate or tweak input data
│   ├── pipeline.ipynb            # PySpark data processing and curation
│   ├── analysis.ipynb            # Analysis and insights notebook
│   └── model_evaluate.py         # CLI script to evaluate pre-trained model
├── config.yaml                   # Paths, MongoDB URI, and thresholds
├── requirements.txt              # Python dependencies
├── data/
│   ├── raw/
│   ├── curated/
│   │   └── test_inventory.parquet
│   └── models/
│       └── stock_out_model       # Pre-trained Logistic Regression model

```

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- PySpark 3.5.2
- MongoDB 4.7+
- Pandas, PyYAML

### Installation

```bash
# Clone the repository
git clone https://github.com/prabin466/nova-retail.git
cd nova-retail

# Create and activate Virtual environment
python -m venv venv               # Create virtual environment
source venv/bin/activate          # Linux/macOS
venv\Scripts\activate           # Windows

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install MongoDB if not already installed
Follow instructions at: https://www.mongodb.com/docs/manual/installation/
# After Installing MongoDB
# Start  MongoDB server
mongod --dbpath pathtoyourfolder/data/mongo_data/db
# Check connection
mongosh --eval 'db.runCommand({ connectionStatus: 1 })'  # Check connection, should return 1

# Run scripts
python scripts/Data_generation.py       # Creates required folders, also can make tweaks for better data
# Process, curate data and analysis
Run pipeline.ipynb to clean , transform and assemble features
# Model training
Model is trained in pipeline.ipynb and stored in data/models/stock_out_model

Evaluate model through CLI
# You can use the test data that is created through pipeline.ipynb or test with your own data.
# Please use full path to your folder for consistent followups.
python scripts/model_evaluate.py \
  --model_path file:///pathToYourFolder/data/models/stock_out_model \
  --test_path file:///pathToYourFolder/data/curated/test_inventory.parquet



```
# Configuration
Update config.yaml with your local paths and MongoDB URI.
Ensure the collections (daily_sales, customers_curated, Stock_risk_signal) exist in your database.

 # Running the Pipeline
Open pipeline.ipynb to process raw data and curate datasets.
Processed data is saved to MongoDB for analytics and reporting.
Use PySpark caching and partitioning for optimal performance.

```
⚠️ Notes

Run in a fresh virtual environment to avoid dependency conflicts.

config.yaml contains sensitive info — do not commit publicly.

Optimized for fast, large-scale retail analytics.

```
👤 Author

Prabin Shrestha – Data Science & Big Data Enthusiast
Email: sthprabin46@gmail.com












