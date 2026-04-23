# ==============================
# 📦 IMPORT LIBRARIES
# ==============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os

# ==============================
# 📁 CREATE FOLDERS
# ==============================
os.makedirs("visualizations", exist_ok=True)

# ==============================
# 🎨 STYLE
# ==============================
sns.set_theme(style="whitegrid")
palette = ["#2E86AB", "#F6C85F", "#6F4E7C", "#9FD356"]

# ==============================
# 📊 LOAD DATA
# ==============================
df = pd.read_csv("sales_data.csv")

# ==============================
# 🧹 CLEAN DATA
# ==============================

# Fix mixed date formats safely
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True, errors='coerce')

# Remove invalid rows
df = df.dropna(subset=['Date'])

# Remove other missing values
df = df.dropna()

# ==============================
# 📈 FEATURE ENGINEERING
# ==============================
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# ==============================
# 📊 SEABORN VISUALS
# ==============================

# --- Bar Plot
plt.figure(figsize=(8,5))
sns.barplot(x='Product', y='Total_Sales', data=df, palette=palette)
plt.xticks(rotation=45)
plt.title('Total Sales by Product')
plt.savefig("visualizations/barplot.png")
plt.close()

# --- Line Plot
monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(x='Month', y='Total_Sales', data=monthly_sales, marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Sales Trend')
plt.savefig("visualizations/lineplot.png")
plt.close()

# --- Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(x='Product', y='Total_Sales', data=df, palette=palette)
plt.xticks(rotation=45)
plt.title('Sales Distribution by Product')
plt.savefig("visualizations/boxplot.png")
plt.close()

# --- Violin Plot
plt.figure(figsize=(8,5))
sns.violinplot(x='Product', y='Total_Sales', data=df, palette=palette)
plt.xticks(rotation=45)
plt.title('Sales Distribution (Violin)')
plt.savefig("visualizations/violinplot.png")
plt.close()

# --- Heatmap
plt.figure(figsize=(6,4))
corr = df[['Quantity', 'Price', 'Total_Sales']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig("visualizations/heatmap.png")
plt.close()

# ==============================
# 📊 PLOTLY INTERACTIVE
# ==============================

# --- Bar
fig_bar = px.bar(
    df,
    x='Product',
    y='Total_Sales',
    color='Region',
    title='Sales by Product'
)

# --- Line
fig_line = px.line(
    monthly_sales,
    x='Month',
    y='Total_Sales',
    markers=True,
    title='Monthly Trend'
)

# --- Pie
region_counts = df['Region'].value_counts().reset_index()
region_counts.columns = ['Region', 'Count']

fig_pie = px.pie(
    region_counts,
    names='Region',
    values='Count',
    title='Region Distribution'
)

# ==============================
# 📊 DASHBOARD
# ==============================

fig_dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Sales by Product",
        "Monthly Trend",
        "Region Distribution",
        "Sales Distribution"
    ),
    specs=[[{"type": "bar"}, {"type": "scatter"}],
           [{"type": "domain"}, {"type": "box"}]]
)

# Add charts
for trace in fig_bar.data:
    fig_dashboard.add_trace(trace, row=1, col=1)

for trace in fig_line.data:
    fig_dashboard.add_trace(trace, row=1, col=2)

for trace in fig_pie.data:
    fig_dashboard.add_trace(trace, row=2, col=1)

fig_dashboard.add_trace(
    go.Box(x=df['Product'], y=df['Total_Sales'], name='Distribution'),
    row=2, col=2
)

# ==============================
# 🎛️ DROPDOWN FILTER
# ==============================

buttons = []

# All option
buttons.append(dict(
    label="All",
    method="update",
    args=[{"visible": [True]*len(fig_dashboard.data)},
          {"title": "Full Dashboard"}]
))

# Region filters (simple UI only)
for region in df['Region'].unique():
    buttons.append(dict(
        label=region,
        method="update",
        args=[{"visible": [True]*len(fig_dashboard.data)},
              {"title": f"Dashboard - {region}"}]
    ))

fig_dashboard.update_layout(
    updatemenus=[dict(buttons=buttons, x=1.15, y=1.2)]
)

# ==============================
# 🎨 FINAL LAYOUT
# ==============================

fig_dashboard.update_layout(
    title="📊 Interactive Sales Dashboard",
    height=800
)

# ==============================
# 💾 SAVE OUTPUT
# ==============================

fig_dashboard.write_html("visualizations/dashboard.html")

print("✅ Dashboard created successfully!")
