import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATA
# -------------------------
try:
    df = pd.read_csv('data/sales_data.csv')
except:
    print("Error loading file")
    exit()

# -------------------------
# FIX COLUMN NAMES (IMPORTANT)
# -------------------------
df.columns = df.columns.str.strip()

print("Columns in dataset:", df.columns)

# -------------------------
# CLEAN DATA
# -------------------------
df = df.drop_duplicates()
df['Quantity'] = df['Quantity'].fillna(0)

# -------------------------
# CREATE TOTAL SALES
# -------------------------
df['Total_Sales'] = df['Quantity'] * df['Price']

# -------------------------
# ANALYSIS
# -------------------------

# Check if Category column exists
if 'Category' in df.columns:
    category_sales = df.groupby('Category')['Total_Sales'].sum()
else:
    print("Category column not found, using Product instead")
    category_sales = df.groupby('Product')['Total_Sales'].sum()

# Best selling product
best_product = df.groupby('Product')['Quantity'].sum().idxmax()

# Total revenue
total_revenue = df['Total_Sales'].sum()

# -------------------------
# VISUALIZATION
# -------------------------

# Bar Chart
plt.figure()
category_sales.plot(kind='bar')
plt.title('Sales Analysis')
plt.xlabel('Category/Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('visualizations/bar_chart.png')

# Pie Chart
plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('visualizations/pie_chart.png')

# -------------------------
# OUTPUT
# -------------------------
print("\n--- RESULTS ---")
print("Total Revenue:", total_revenue)
print("Best Selling Product:", best_product)
