# 📊 Nova Retail Analytics Pipeline

A **retail analytics pipeline** built with **PySpark** and **MongoDB**, designed to process and analyze sales, customer, and stock data. Supports **daily sales aggregation**, **moving average computations**, **RFM scoring**, and **stock-out risk detection**.

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

---

## 📂 Project Structure
NovaRetail/
├── scripts/
│ ├── data_generation.py # Script to generate or tweak input data
│ ├── pipeline.ipynb # PySpark data processing and curation
│ └── analysis.ipynb # Analysis and insights notebook
├── config.yaml # Paths, MongoDB URI, and thresholds
├── requirements.txt # Python dependencies
└── data/ # Raw and curated CSV/Parquet files
---

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- PySpark 3.5.2
- MongoDB 4.7+
- Pandas, PyYAML

### Installation

```bash
git clone https://github.com/yourusername/nova-retail.git
cd nova-retail
python -m venv venv               # Create virtual environment
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows
pip install --upgrade pip
pip install -r requirements.txt

Configuration

Update config.yaml with your local paths and MongoDB URI.

Ensure the collections (daily_sales, customers_curated, Stock_risk_signal) exist in your database.

Running the Pipeline

Open pipeline.ipynb to process raw data and curate datasets.

Processed data is saved to MongoDB for analytics and reporting.

Use PySpark caching and partitioning for optimal performance.

⚠️ Notes

Run in a fresh virtual environment to avoid dependency conflicts.

config.yaml contains sensitive info — do not commit publicly.

Optimized for fast, large-scale retail analytics.

👤 Author

Prabin Shrestha – Data Science & Big Data Enthusiast
Email: pravinxtha123@gmail.com


