"""
AI Sales Intelligence Tool — E-Commerce Edition
Author: Deborah Musuamba
GitHub: github.com/Deborahmk
Description: Collects, cleans, and analyzes e-commerce sales data using
             AI-powered pattern detection, trend analysis, and forecasting.
"""

import csv
import os
import statistics
from datetime import datetime

# ─── Sample Data Generator ───────────────────────────────────────────────────
SAMPLE_DATA = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "units": 5, "price": 999.99, "region": "North"},
    {"date": "2026-01-01", "product": "T-Shirt", "category": "Clothing", "units": 20, "price": 29.99, "region": "South"},
    {"date": "2026-01-02", "product": "Headphones", "category": "Electronics", "units": 8, "price": 149.99, "region": "East"},
    {"date": "2026-01-02", "product": "Jeans", "category": "Clothing", "units": 15, "price": 59.99, "region": "West"},
    {"date": "2026-01-03", "product": "Laptop", "category": "Electronics", "units": 3, "price": 999.99, "region": "South"},
    {"date": "2026-01-03", "product": "Coffee Maker", "category": "Home", "units": 10, "price": 79.99, "region": "North"},
    {"date": "2026-01-04", "product": "Sneakers", "category": "Clothing", "units": 25, "price": 89.99, "region": "East"},
    {"date": "2026-01-04", "product": "Tablet", "category": "Electronics", "units": 6, "price": 499.99, "region": "West"},
    {"date": "2026-01-05", "product": "Blender", "category": "Home", "units": 12, "price": 49.99, "region": "North"},
    {"date": "2026-01-05", "product": "Headphones", "category": "Electronics", "units": 4, "price": 149.99, "region": "South"},
    {"date": "2026-01-06", "product": "T-Shirt", "category": "Clothing", "units": 30, "price": 29.99, "region": "West"},
    {"date": "2026-01-06", "product": "Laptop", "category": "Electronics", "units": 7, "price": 999.99, "region": "East"},
    {"date": "2026-01-07", "product": "Coffee Maker", "category": "Home", "units": 8, "price": 79.99, "region": "South"},
    {"date": "2026-01-07", "product": "Sneakers", "category": "Clothing", "units": 18, "price": 89.99, "region": "North"},
    {"date": "2026-01-08", "product": "Tablet", "category": "Electronics", "units": 9, "price": 499.99, "region": "East"},
]


# ─── Data Collection ──────────────────────────────────────────────────────────
def collect_data_manual():
    """Collect sales data through manual entry."""
    data = []
    print("\n📥 MANUAL DATA ENTRY MODE")
    print("Enter sales records (type 'done' when finished)\n")

    while True:
        print(f"Record #{len(data) + 1}:")
        date = input("  Date (YYYY-MM-DD): ").strip()
        if date.lower() == "done":
            break
        product = input("  Product name: ").strip()
        category = input("  Category: ").strip()
        try:
            units = int(input("  Units sold: ").strip())
            price = float(input("  Price per unit ($): ").strip())
        except ValueError:
            print("  ⚠️ Invalid number — skipping record.")
            continue
        region = input("  Region (North/South/East/West): ").strip()

        data.append({
            "date": date, "product": product, "category": category,
            "units": units, "price": price, "region": region
        })
        print(f"  ✅ Record added!\n")

    return data


def load_sample_data():
    """Load built-in sample e-commerce data."""
    print("\n📦 Loading sample e-commerce data...")
    return SAMPLE_DATA


def load_csv_data(filepath):
    """Load sales data from a CSV file."""
    data = []
    try:
        with open(filepath, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    "date": row.get("date", ""),
                    "product": row.get("product", ""),
                    "category": row.get("category", ""),
                    "units": int(row.get("units", 0)),
                    "price": float(row.get("price", 0)),
                    "region": row.get("region", "")
                })
        print(f"✅ Loaded {len(data)} records from {filepath}")
    except FileNotFoundError:
        print(f"⚠️ File not found: {filepath}")
    return data


# ─── Data Cleaning ────────────────────────────────────────────────────────────
def clean_data(data):
    """Remove duplicates, fix missing values, validate records."""
    print("\n🧹 Cleaning data...")
    original_count = len(data)
    cleaned = []
    seen = set()

    for record in data:
        key = (record["date"], record["product"], record["region"])
        if key in seen:
            continue
        if not record["product"] or record["units"] <= 0 or record["price"] <= 0:
            continue
        seen.add(key)
        record["revenue"] = round(record["units"] * record["price"], 2)
        cleaned.append(record)

    removed = original_count - len(cleaned)
    print(f"  ✅ {len(cleaned)} valid records | {removed} duplicates/invalid removed")
    return cleaned


# ─── AI Analysis Engine ───────────────────────────────────────────────────────
def calculate_revenue(data):
    """Calculate total and per-product revenue."""
    totals = {}
    for record in data:
        product = record["product"]
        totals[product] = totals.get(product, 0) + record["revenue"]
    return dict(sorted(totals.items(), key=lambda x: x[1], reverse=True))


def analyze_by_category(data):
    """Analyze sales performance by category."""
    categories = {}
    for record in data:
        cat = record["category"]
        if cat not in categories:
            categories[cat] = {"revenue": 0, "units": 0}
        categories[cat]["revenue"] += record["revenue"]
        categories[cat]["units"] += record["units"]
    return dict(sorted(categories.items(), key=lambda x: x[1]["revenue"], reverse=True))


def analyze_by_region(data):
    """Analyze sales performance by region."""
    regions = {}
    for record in data:
        reg = record["region"]
        if reg not in regions:
            regions[reg] = {"revenue": 0, "units": 0}
        regions[reg]["revenue"] += record["revenue"]
        regions[reg]["units"] += record["units"]
    return dict(sorted(regions.items(), key=lambda x: x[1]["revenue"], reverse=True))


def detect_anomalies(data):
    """AI anomaly detection — flags unusually high or low sales."""
    revenues = [r["revenue"] for r in data]
    if len(revenues) < 3:
        return []
    mean = statistics.mean(revenues)
    stdev = statistics.stdev(revenues)
    anomalies = []
    for record in data:
        z_score = (record["revenue"] - mean) / stdev if stdev > 0 else 0
        if abs(z_score) > 1.5:
            flag = "📈 Unusually HIGH" if z_score > 0 else "📉 Unusually LOW"
            anomalies.append({
                "product": record["product"],
                "date": record["date"],
                "revenue": record["revenue"],
                "flag": flag
            })
    return anomalies


def forecast_trend(data):
    """Simple AI trend forecasting based on revenue trajectory."""
    revenues = [r["revenue"] for r in data]
    if len(revenues) < 4:
        return "Not enough data for forecasting."
    mid = len(revenues) // 2
    first_half_avg = statistics.mean(revenues[:mid])
    second_half_avg = statistics.mean(revenues[mid:])
    change = ((second_half_avg - first_half_avg) / first_half_avg) * 100 if first_half_avg > 0 else 0

    if change > 10:
        return f"📈 UPWARD trend detected (+{change:.1f}%) — Sales are growing. Recommend increasing inventory."
    elif change < -10:
        return f"📉 DOWNWARD trend detected ({change:.1f}%) — Sales are declining. Recommend reviewing pricing strategy."
    else:
        return f"➡️ STABLE trend detected ({change:+.1f}%) — Sales are consistent. Maintain current strategy."


def generate_ai_recommendations(product_revenue, category_revenue, region_revenue, anomalies):
    """Generate AI-powered business recommendations."""
    recommendations = []
    top_product = list(product_revenue.keys())[0]
    bottom_product = list(product_revenue.keys())[-1]
    top_category = list(category_revenue.keys())[0]
    top_region = list(region_revenue.keys())[0]

    recommendations.append(f"🏆 Focus marketing on '{top_product}' — your highest revenue product.")
    recommendations.append(f"⚠️  Review strategy for '{bottom_product}' — lowest revenue product.")
    recommendations.append(f"📦 Expand '{top_category}' category inventory — top performing category.")
    recommendations.append(f"🌍 Prioritize '{top_region}' region — highest sales volume.")
    if anomalies:
        recommendations.append(f"🔍 Investigate {len(anomalies)} anomalous transactions detected by AI.")
    recommendations.append("💡 Consider bundle deals to increase average order value.")

    return recommendations


# ─── Report Generation ────────────────────────────────────────────────────────
def display_report(data, product_revenue, category_revenue, region_revenue, anomalies, trend, recommendations):
    """Display the full AI Sales Intelligence Report."""
    total_revenue = sum(r["revenue"] for r in data)
    total_units = sum(r["units"] for r in data)

    print("\n" + "=" * 60)
    print("       AI SALES INTELLIGENCE REPORT — E-COMMERCE")
    print("       Author: Deborah Musuamba | github.com/Deborahmk")
    print("=" * 60)

    print(f"\n📊 OVERVIEW")
    print(f"   Total Records Analyzed : {len(data)}")
    print(f"   Total Revenue          : ${total_revenue:,.2f}")
    print(f"   Total Units Sold       : {total_units:,}")
    print(f"   Avg Revenue per Sale   : ${total_revenue/len(data):,.2f}")

    print(f"\n🏆 TOP PRODUCTS BY REVENUE")
    for i, (product, rev) in enumerate(list(product_revenue.items())[:5], 1):
        bar = "█" * int(rev / max(product_revenue.values()) * 20)
        print(f"   {i}. {product:<15} ${rev:>10,.2f}  {bar}")

    print(f"\n📦 SALES BY CATEGORY")
    for cat, data_cat in category_revenue.items():
        print(f"   {cat:<15} Revenue: ${data_cat['revenue']:>10,.2f}  |  Units: {data_cat['units']:>5,}")

    print(f"\n🌍 SALES BY REGION")
    for reg, data_reg in region_revenue.items():
        print(f"   {reg:<10} Revenue: ${data_reg['revenue']:>10,.2f}  |  Units: {data_reg['units']:>5,}")

    print(f"\n🤖 AI TREND FORECAST")
    print(f"   {trend}")

    if anomalies:
        print(f"\n⚠️  AI ANOMALY DETECTION ({len(anomalies)} found)")
        for a in anomalies[:5]:
            print(f"   {a['flag']} — {a['product']} on {a['date']} (${a['revenue']:,.2f})")

    print(f"\n💡 AI RECOMMENDATIONS")
    for rec in recommendations:
        print(f"   {rec}")

    print("\n" + "=" * 60)
    print("   Report generated by AI Sales Intelligence Tool")
    print(f"   Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")


def save_report(data, product_revenue, total_revenue, trend, recommendations):
    """Save report to a text file."""
    filename = f"sales_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("AI SALES INTELLIGENCE REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Revenue: ${total_revenue:,.2f}\n")
        f.write(f"Total Records: {len(data)}\n\n")
        f.write("TOP PRODUCTS:\n")
        for product, rev in list(product_revenue.items())[:5]:
            f.write(f"  {product}: ${rev:,.2f}\n")
        f.write(f"\nTREND: {trend}\n\n")
        f.write("RECOMMENDATIONS:\n")
        for rec in recommendations:
            f.write(f"  {rec}\n")
    print(f"✅ Report saved to {filename}")


# ─── Main Program ─────────────────────────────────────────────────────────────
def main():
    print("\n" + "=" * 60)
    print("    AI SALES INTELLIGENCE TOOL — E-Commerce Edition")
    print("    Author: Deborah Musuamba | github.com/Deborahmk")
    print("=" * 60)

    print("\nHow would you like to load your sales data?")
    print("  1. Use sample e-commerce data (recommended for demo)")
    print("  2. Enter data manually")
    print("  3. Load from CSV file")
    choice = input("\nEnter choice (1/2/3): ").strip()

    if choice == "1":
        raw_data = load_sample_data()
    elif choice == "2":
        raw_data = collect_data_manual()
    elif choice == "3":
        filepath = input("Enter CSV file path: ").strip()
        raw_data = load_csv_data(filepath)
    else:
        print("Invalid choice. Loading sample data...")
        raw_data = load_sample_data()

    if not raw_data:
        print("⚠️ No data to analyze. Exiting.")
        return

    # Clean
    data = clean_data(raw_data)

    # Analyze
    print("\n🤖 Running AI analysis...")
    product_revenue = calculate_revenue(data)
    category_revenue = analyze_by_category(data)
    region_revenue = analyze_by_region(data)
    anomalies = detect_anomalies(data)
    trend = forecast_trend(data)
    recommendations = generate_ai_recommendations(product_revenue, category_revenue, region_revenue, anomalies)

    # Report
    display_report(data, product_revenue, category_revenue, region_revenue, anomalies, trend, recommendations)

    # Save
    save = input("Would you like to save the report? (yes/no): ").strip().lower()
    if save in ["yes", "y"]:
        save_report(data, product_revenue, sum(r["revenue"] for r in data), trend, recommendations)


if __name__ == "__main__":
    main()
