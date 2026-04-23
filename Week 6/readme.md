# 📊 Interactive Sales Dashboard

## 🧠 Project Overview

The **Interactive Sales Dashboard** is a data visualization project designed to analyze and present sales data using both **static (Seaborn/Matplotlib)** and **interactive (Plotly)** visualizations.

This dashboard helps in understanding:

* 📈 Sales trends over time
* 🛍️ Product performance
* 🌍 Regional distribution of sales
* 📊 Statistical distribution of sales data

The goal is to transform raw data into meaningful insights through **clean, professional, and interactive visuals**.

---

## 🚀 Features

* ✔️ 5+ different chart types
* ✔️ Seaborn statistical visualizations
* ✔️ Interactive Plotly dashboard
* ✔️ Correlation heatmap
* ✔️ Automated folder creation
* ✔️ Exportable HTML dashboard

---

## 📁 Project Structure

```
sales-dashboard/
│── dashboard.py
│── sales_data.csv
│── visualizations/
│    ├── barplot.png
│    ├── lineplot.png
│    ├── boxplot.png
│    ├── violinplot.png
│    ├── heatmap.png
│    └── dashboard.html
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Project

```bash
python dashboard.py
```

---

## 📊 Dataset Description

The dataset contains sales records with the following columns:

| Column      | Description                      |
| ----------- | -------------------------------- |
| Date        | Transaction date                 |
| Product     | Product name                     |
| Quantity    | Number of items sold             |
| Price       | Price per unit                   |
| Customer    | Customer ID                      |
| Region      | Sales region                     |
| Total_Sales | Total revenue (Quantity × Price) |

---

## 📈 Visualizations Explained

### 🔹 1. Bar Chart

**Purpose:** Compare total sales across products
**Insight:** Identifies top-performing products

---

### 🔹 2. Line Chart

**Purpose:** Track monthly sales trends
**Insight:** Reveals growth patterns and seasonality

---

### 🔹 3. Box Plot

**Purpose:** Show distribution of sales values
**Insight:** Detects outliers and variability

---

### 🔹 4. Violin Plot

**Purpose:** Visualize data distribution shape
**Insight:** Provides deeper understanding of density

---

### 🔹 5. Heatmap

**Purpose:** Show correlation between numerical features
**Insight:** Identifies relationships between Quantity, Price, and Sales

---

### 🔹 6. Interactive Dashboard (Plotly)

**Features:**

* Hover tooltips
* Interactive layout
* Dropdown filter (Region)
* Multi-chart view

---

## 🧪 Data Cleaning & Processing

* Handled **mixed date formats**
* Removed missing values
* Converted dates to datetime format
* Created **Month column** for trend analysis

---

## 🎨 Design Choices

* Consistent color palette
* Clean layout with proper spacing
* Readable labels and titles
* Balanced visual hierarchy

---

## 🧪 Testing & Validation

* Checked for missing values
* Validated data types
* Ensured correct date parsing
* Verified calculations (Total_Sales)

---

## 📸 Output

After running the script:

📁 `visualizations/` folder will contain:

* Static charts (PNG format)
* ✅ **Interactive dashboard (HTML)**

👉 Open:

```
visualizations/dashboard.html
```

---

## 📌 Key Insights (Example)

* Some products generate higher revenue consistently
* Sales vary significantly across regions
* Strong correlation between Quantity and Total Sales
* Presence of outliers in certain product categories

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

---


