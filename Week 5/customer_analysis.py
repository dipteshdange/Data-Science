import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================
# 1. LOAD DATA (EXCEL FIX ✅)
# ==============================
print("Files in folder:", os.listdir())

sales = pd.read_csv('sales_data.csv')
customers = pd.read_csv('customer_churn.csv')

print("\nSales Columns:", sales.columns)
print("Customer Columns:", customers.columns)

# ==============================
# STANDARDIZE COLUMN NAMES ✅
# ==============================
sales.columns = sales.columns.str.lower().str.strip()
customers.columns = customers.columns.str.lower().str.strip()

# Rename columns correctly
sales.rename(columns={
    'date': 'order_date',
    'product': 'product_name',
    'customer_id': 'customer_id',   # already fine after lowercase
    'total_sales': 'revenue'
}, inplace=True)

customers.rename(columns={
    'customerid': 'customer_id'
}, inplace=True)

# ==============================
# 3. DATA CLEANING
# ==============================

# Convert date
if 'order_date' in sales.columns:
    sales['order_date'] = pd.to_datetime(sales['order_date'], errors='coerce')

# Fill missing values
sales.fillna(0, inplace=True)
customers.fillna("Unknown", inplace=True)

# Create revenue column
if 'revenue' not in sales.columns:
    sales['revenue'] = sales['quantity'] * sales['price']
else:
    print("⚠️ Missing 'quantity' or 'price' column")

# ==============================
# 4. CUSTOMER ANALYSIS
# ==============================

# Ensure customer_id exists
if 'customer_id' not in sales.columns:
    print("❌ 'customer_id' missing in sales data")
    exit()

# Aggregation 1: CLV
customer_value = sales.groupby('customer_id')['revenue'].sum().reset_index()
customer_value.rename(columns={'revenue': 'CLV'}, inplace=True)

# Merge
customer_full = pd.merge(customers, customer_value, on='customer_id', how='inner')

# Top customers
top_customers = customer_full.sort_values(by='CLV', ascending=False).head(10)

# Aggregation 2: Region
if 'region' in customer_full.columns:
    region_sales = customer_full.groupby('region')['CLV'].sum().sort_values(ascending=False)
else:
    region_sales = pd.Series()

# ==============================
# 5. SALES ANALYSIS
# ==============================

# Monthly trend
if 'order_date' in sales.columns:
    sales['month'] = sales['order_date'].dt.to_period('M')
    monthly_sales = sales.groupby('month')['revenue'].sum()
else:
    monthly_sales = pd.Series()

# Aggregation 3: Products
if 'product_name' in sales.columns:
    top_products = sales.groupby('product_name')['revenue'].sum().sort_values(ascending=False)
else:
    top_products = pd.Series()

# ==============================
# 6. PIVOT TABLE
# ==============================

if 'region' in sales.columns and 'product_name' in sales.columns:
    pivot_table = pd.pivot_table(
        sales,
        values='revenue',
        index='region',
        columns='product_name',
        aggfunc='sum',
        fill_value=0
    )
else:
    pivot_table = pd.DataFrame()

# ==============================
# 7. RETENTION RATE
# ==============================

repeat_customers = sales.groupby('customer_id').size()
retention_rate = (repeat_customers > 1).mean()

# ==============================
# 8. VISUALIZATIONS
# ==============================

# Monthly trend
if not monthly_sales.empty:
    plt.figure()
    monthly_sales.plot()
    plt.title("Monthly Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_sales.png")

# Top customers
if not top_customers.empty:
    plt.figure()
    top_customers.plot(kind='bar', x='customer_name', y='CLV')
    plt.title("Top Customers")
    plt.tight_layout()
    plt.savefig("top_customers.png")

# Region pie
if not region_sales.empty:
    plt.figure()
    region_sales.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Region Sales")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("region_sales.png")

# Products
if not top_products.empty:
    plt.figure()
    top_products.head(10).plot(kind='bar')
    plt.title("Top Products")
    plt.tight_layout()
    plt.savefig("top_products.png")

# Heatmap
if not pivot_table.empty:
    plt.figure()
    sns.heatmap(pivot_table)
    plt.title("Heatmap")
    plt.tight_layout()
    plt.savefig("heatmap.png")

# ==============================
# 9. FINAL REPORT
# ==============================

total_revenue = sales['revenue'].sum()
total_customers = customers['customer_id'].nunique()
avg_order_value = sales['revenue'].mean()

print("\n==============================")
print("CUSTOMER SALES ANALYSIS REPORT")
print("==============================")

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Customers: {total_customers}")
print(f"Average Order Value: ${avg_order_value:,.2f}")

if not top_customers.empty:
    print(f"\nTop Customer: {top_customers.iloc[0]['customer_name']} - ${top_customers.iloc[0]['CLV']:,.2f}")

if not region_sales.empty:
    print(f"Top Region: {region_sales.index[0]}")

if not top_products.empty:
    print(f"Best Product: {top_products.index[0]}")

print(f"Customer Retention Rate: {retention_rate:.2%}")

# ==============================
# 10. SAVE REPORT
# ==============================

with open("analysis_report.txt", "w") as f:
    f.write("CUSTOMER SALES ANALYSIS REPORT\n\n")
    f.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    f.write(f"Total Customers: {total_customers}\n")
    f.write(f"Average Order Value: ${avg_order_value:,.2f}\n")
    f.write(f"Customer Retention Rate: {retention_rate:.2%}\n")

print("\n✅ Done! Charts + report generated.")
