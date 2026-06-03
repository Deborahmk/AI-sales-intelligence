# 📊 AI Sales Intelligence Tool — E-Commerce Edition

**Author:** Deborah Musuamba  
**GitHub:** [github.com/Deborahmk](https://github.com/Deborahmk)

---

## 📌 Overview

An AI-powered sales intelligence tool that collects, cleans, and analyzes e-commerce sales data to generate actionable business insights, trend forecasts, and AI-driven recommendations.

**This project demonstrates:**
- **Data Collection** — manual entry, CSV upload, or built-in sample data
- **Data Cleaning** — deduplication, validation, revenue calculation
- **AI Analysis** — anomaly detection, trend forecasting, pattern recognition
- **Business Intelligence** — top products, category analysis, regional performance
- **Report Generation** — detailed reports with AI recommendations

---

## 🚀 How to Run

### Requirements
- Python 3.7 or higher
- No external libraries required

### Run the CLI app
```bash
python sales_intelligence.py
```

### Run the Web Interface
```bash
python web_app.py
```
Then open your browser at: `http://localhost:5000`

---

## 📊 Sample Output

```
============================================================
       AI SALES INTELLIGENCE REPORT — E-COMMERCE
============================================================

📊 OVERVIEW
   Total Records Analyzed : 15
   Total Revenue          : $32,608.20
   Total Units Sold       : 180

🏆 TOP PRODUCTS BY REVENUE
   1. Laptop           $14,999.85  ████████████████████
   2. Tablet           $ 7,499.85  █████████
   3. Sneakers         $ 3,869.57  █████

📦 SALES BY CATEGORY
   Electronics     Revenue: $24,299.58  |  Units:   42
   Clothing        Revenue: $ 6,268.92  |  Units:  108

🤖 AI TREND FORECAST
   📈 UPWARD trend detected (+20.0%) — Sales are growing.

💡 AI RECOMMENDATIONS
   🏆 Focus marketing on 'Laptop' — highest revenue product.
   📦 Expand 'Electronics' category — top performing category.
   🌍 Prioritize 'East' region — highest sales volume.
============================================================
```

---

## 🧠 How It Works

### 1. Data Collection
Three flexible input methods:
- **Sample data** — built-in e-commerce dataset for demo
- **Manual entry** — interactive CLI data input
- **CSV upload** — load your own sales data file

### 2. Data Cleaning Engine
```python
def clean_data(data):
    # Removes duplicates
    # Validates records (units > 0, price > 0)
    # Calculates revenue = units × price
```

### 3. AI Analysis Modules

| Module | Description |
|--------|-------------|
| Revenue Analysis | Ranks products by total revenue |
| Category Analysis | Groups and compares product categories |
| Regional Analysis | Identifies top-performing sales regions |
| Anomaly Detection | Uses Z-score to flag unusual transactions |
| Trend Forecasting | Compares first/second half revenue to detect trends |
| AI Recommendations | Generates actionable business insights |

### 4. Anomaly Detection (Z-Score Method)
```python
z_score = (record["revenue"] - mean) / stdev
if abs(z_score) > 1.5:
    flag as anomaly
```

---

## 📁 Project Structure

```
sales-intelligence/
│
├── sales_intelligence.py    # Main CLI application
├── web_app.py               # Web interface (Flask)
├── sample_sales_data.csv    # Sample dataset
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

---

## 🔭 Future Enhancements

- [ ] Integrate OpenAI API for natural language insights
- [ ] Add machine learning forecasting (Linear Regression)
- [ ] Build interactive charts with Matplotlib/Plotly
- [ ] Add database storage (SQLite/MySQL)
- [ ] Export reports to PDF
- [ ] Add user authentication for web interface

---

## ⚠️ Disclaimer

This tool is for **educational and portfolio demonstration purposes**.  
Sample data is fictional and does not represent any real business.

---

## 📄 License

MIT License — Copyright 2026 Deborah Musuamba
