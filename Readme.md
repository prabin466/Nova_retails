Nova Retail Analytics Pipeline

Project Overview

This project demonstrates a retail data analytics pipeline using PySpark and MongoDB. It processes curated datasets for sales, customers, and stock, computes customer RFM scores, daily item-store sales, moving averages, and stock-out risk signals, and serves actionable insights through MongoDB queries.

Features

Data Ingestion & Curation

Curates sales, customer, and stock data.

Stores curated datasets in MongoDB collections:

daily_sales

customers_curated

Stock_risk_signal

Customer Analysis

Computes Recency, Frequency, Monetary (RFM) scores.

Assigns RFM score (1-4) and combined RFM total score.

Identifies top customers likely to respond to promotions.

Sales Analysis

Computes daily item-store sales.

Calculates moving average demand per SKU.

Supports top SKU queries.

Stock Analysis

Computes stock-out risk signals.

Identifies fast-moving SKUs by store and globally.

Performance Optimization

Uses PySpark caching, partitioning, and broadcast joins for efficiency.

Setup & Installation

Clone the repository

git clone <your-repo-url>
cd NovaRetail


Create a new virtual environment

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate


Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

NovaRetail/
│
├─ pipeline.ipynb          # PySpark data processing pipeline
├─ serving.ipynb           # MongoDB queries & actionable insights
├─ config.yaml             # Config file for paths, DB URI, thresholds
├─ requirements.txt        # Project dependencies
└─ data/                   # Raw and curated data (CSV/Parquet)