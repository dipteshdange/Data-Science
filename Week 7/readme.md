# Statistical Business Analysis

## Project Overview

This project focuses on performing statistical analysis on sales data to extract meaningful business insights. The analysis includes descriptive statistics, data distribution, correlation analysis, hypothesis testing, confidence intervals, and regression modeling.

The objective is to use statistical methods to understand patterns in the data and support data-driven decision-making.

---

## Objectives

* Calculate descriptive statistics for key variables
* Analyze data distribution and normality
* Identify relationships using correlation analysis
* Perform hypothesis testing to validate assumptions
* Calculate confidence intervals for key metrics
* Build a regression model to understand variable impact
* Provide actionable business insights

---

## Dataset Description

### sales_data.csv

Contains transactional sales data with the following columns:

| Column      | Description                      |
| ----------- | -------------------------------- |
| Date        | Transaction date                 |
| Product     | Product name                     |
| Quantity    | Units sold                       |
| Price       | Price per unit                   |
| Customer_ID | Unique customer identifier       |
| Region      | Sales region                     |
| Total_Sales | Total revenue (Quantity × Price) |

---

## Project Structure

```
statistical-business-analysis/
│── statistical_analysis.py
│── sales_data.csv
│── requirements.txt
│── statistical_report.pdf
│── hypothesis_tests_results.txt
│── README.md
```

---

## Setup Instructions

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Run the Analysis

```
python statistical_analysis.py
```

---

## Methodology

### 1. Descriptive Statistics

* Mean, median, and mode calculated
* Standard deviation used to measure variability

### 2. Data Distribution Analysis

* Histogram plotted for Total Sales
* Shapiro-Wilk test used to check normality

### 3. Correlation Analysis

* Pearson correlation calculated
* Heatmap used for visualization

### 4. Hypothesis Testing

#### Test 1: One-Sample t-test

* H0: Mean sales = 100000
* H1: Mean sales ≠ 100000

#### Test 2: Two-Sample t-test

* H0: No difference between regions
* H1: Sales differ between regions

#### Test 3: ANOVA

* H0: All product means are equal
* H1: At least one product differs

### 5. Confidence Interval

* 95% confidence interval calculated for Total Sales
* Margin of error determined

### 6. Regression Analysis

* Linear regression model built using Quantity and Price
* R-squared used to evaluate model performance

---

## Key Results (Example)

* Average Sales: Calculated with 95% confidence interval
* Strong correlation observed between Quantity and Total Sales
* Statistical significance determined using p-values
* Regression model explains variation in Total Sales

---

## Business Insights

* Higher quantity and pricing significantly impact total sales
* Sales patterns vary across different regions
* Certain products outperform others consistently
* Statistical tests confirm meaningful differences in sales behavior

---

## Testing and Validation

* Missing values handled appropriately
* Data types validated before analysis
* Statistical assumptions checked before applying tests
* Results verified using multiple statistical methods

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Statsmodels

---

## Future Improvements

* Include marketing spend data for deeper analysis
* Apply advanced machine learning models
* Build an interactive dashboard for real-time insights
* Expand dataset for more robust conclusions

---
