# Import pandas library
import pandas as pd

# -----------------------------
# STEP 1: LOAD DATA
# -----------------------------
# Load CSV file into DataFrame
df = pd.read_csv('sales_data.csv')

print("Initial Data:")
print(df)

# -----------------------------
# STEP 2: EXPLORE DATA
# -----------------------------
print("\nData Info:")
print(df.info())

print("\nShape of dataset:", df.shape)
print("\nColumns:", df.columns)

# -----------------------------
# STEP 3: CLEAN DATA
# -----------------------------

# Handle missing values
# Fill missing Quantity with 0
df['Quantity'] = df['Quantity'].fillna(0)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Quantity to integer
df['Quantity'] = df['Quantity'].astype(int)

# -----------------------------
# STEP 4: ANALYZE SALES
# -----------------------------

# Create Total_Sales column
df['Total_Sales'] = df['Quantity'] * df['Price']

# 1. Total Revenue
total_revenue = df['Total_Sales'].sum()

# 2. Best-selling product (by quantity)
best_product = df.groupby('Product')['Quantity'].sum().idxmax()

# 3. Highest revenue product
top_revenue_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# 4. Average order value
average_order_value = df['Total_Sales'].mean()

# -----------------------------
# STEP 5: PRINT REPORT
# -----------------------------

print("\n--- SALES REPORT ---")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best Selling Product (Quantity): {best_product}")
print(f"Top Revenue Product: {top_revenue_product}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
