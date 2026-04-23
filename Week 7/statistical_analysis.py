# ==============================
# 📦 IMPORT LIBRARIES
# ==============================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# ==============================
# 📊 LOAD DATA
# ==============================
df = pd.read_csv("sales_data.csv")

# ==============================
# 🧹 CLEAN DATA
# ==============================
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

# ==============================
# 📈 1. DESCRIPTIVE STATISTICS
# ==============================
print("\n===== DESCRIPTIVE STATISTICS =====")

desc = df[['Quantity', 'Price', 'Total_Sales']].describe()
print(desc)

print("\nMean:")
print(df[['Quantity', 'Price', 'Total_Sales']].mean())

print("\nMedian:")
print(df[['Quantity', 'Price', 'Total_Sales']].median())

print("\nMode:")
print(df[['Quantity', 'Price', 'Total_Sales']].mode().iloc[0])

print("\nStandard Deviation:")
print(df[['Quantity', 'Price', 'Total_Sales']].std())

# ==============================
# 📊 2. DISTRIBUTION ANALYSIS
# ==============================
sns.histplot(df['Total_Sales'], kde=True)
plt.title("Distribution of Total Sales")
plt.show()

# Normality test
stat, p = stats.shapiro(df['Total_Sales'])
print("\nShapiro Test p-value:", p)

# ==============================
# 📊 3. CORRELATION ANALYSIS
# ==============================
corr = df[['Quantity', 'Price', 'Total_Sales']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

print("\nCorrelation Matrix:\n", corr)

# ==============================
# 📊 4. HYPOTHESIS TESTING
# ==============================

print("\n===== HYPOTHESIS TESTS =====")

# --- Test 1: One-sample t-test (Mean Sales > 100000?)
t_stat, p_val = stats.ttest_1samp(df['Total_Sales'], 100000)
print("\nTest 1: Mean Sales > 100000")
print("t-stat:", t_stat, "p-value:", p_val)

# --- Test 2: Two-sample t-test (North vs South)
north = df[df['Region'] == 'North']['Total_Sales']
south = df[df['Region'] == 'South']['Total_Sales']

t_stat2, p_val2 = stats.ttest_ind(north, south)
print("\nTest 2: North vs South Sales")
print("t-stat:", t_stat2, "p-value:", p_val2)

# --- Test 3: ANOVA (Product comparison)
groups = [group['Total_Sales'].values for name, group in df.groupby('Product')]
f_stat, p_val3 = stats.f_oneway(*groups)

print("\nTest 3: ANOVA across Products")
print("F-stat:", f_stat, "p-value:", p_val3)

# ==============================
# 📊 5. CONFIDENCE INTERVAL
# ==============================

confidence = 0.95
data = df['Total_Sales']
mean = np.mean(data)
sem = stats.sem(data)
margin = sem * stats.t.ppf((1 + confidence) / 2., len(data)-1)

print("\n===== CONFIDENCE INTERVAL =====")
print(f"Mean Sales: {mean:.2f} ± {margin:.2f} (95% CI)")

# ==============================
# 📊 6. REGRESSION ANALYSIS
# ==============================

print("\n===== REGRESSION ANALYSIS =====")

X = df[['Quantity', 'Price']]
y = df['Total_Sales']

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.summary())

# ==============================
# 📊 7. BUSINESS INSIGHTS
# ==============================

print("\n===== BUSINESS INSIGHTS =====")

print(f"Average Sales: {mean:.2f} ± {margin:.2f}")

print("\nCorrelation Insights:")
print(corr['Total_Sales'])

if p_val < 0.05:
    print("Mean sales significantly different from 100000")

if p_val2 < 0.05:
    print("Sales differ significantly between North and South")

if p_val3 < 0.05:
    print("Sales differ significantly across products")

print("\nRegression R-squared:", model.rsquared)

print("\nConclusion:")
print("Quantity and Price strongly influence Total Sales.")
