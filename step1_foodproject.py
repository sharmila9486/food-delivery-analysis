import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/ONLINE_FOOD_DELIVERY_ANALYSIS.csv")

# Basic Info
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum())
# =============================
# DATA CLEANING
# =============================

# Numeric columns - mean/median
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].mean())
df['Delivery_Time_Min'] = df['Delivery_Time_Min'].fillna(df['Delivery_Time_Min'].median())
df['Distance_km'] = df['Distance_km'].fillna(df['Distance_km'].median())
df['Order_Value'] = df['Order_Value'].fillna(df['Order_Value'].median())
df['Final_Amount'] = df['Final_Amount'].fillna(df['Final_Amount'].median())
df['Discount_Applied'] = df['Discount_Applied'].fillna(0)
df['Delivery_Rating'] = df['Delivery_Rating'].fillna(df['Delivery_Rating'].median())

# Categorical columns - mode
df['Customer_Gender'] = df['Customer_Gender'].fillna(df['Customer_Gender'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])
df['Area'] = df['Area'].fillna(df['Area'].mode()[0])
df['Cuisine_Type'] = df['Cuisine_Type'].fillna(df['Cuisine_Type'].mode()[0])
df['Payment_Mode'] = df['Payment_Mode'].fillna(df['Payment_Mode'].mode()[0])

# Special columns
df['Cancellation_Reason'] = df['Cancellation_Reason'].fillna("Not Cancelled")
df['Peak_Hour'] = df['Peak_Hour'].fillna(False).infer_objects(copy=False)
# Date columns - forward fill
df['Order_Date'] = df['Order_Date'].ffill()
df['Order_Time'] = df['Order_Time'].ffill()

# Verify cleaning
print("\nMissing after cleaning:")
print(df.isnull().sum())
# =============================
# OUTLIER TREATMENT
# =============================

# Delivery Time - cap at 120 mins
df['Delivery_Time_Min'] = df['Delivery_Time_Min'].clip(upper=120)

# Order Value - cap at 2000
df['Order_Value'] = df['Order_Value'].clip(upper=2000)

# Ratings - should be between 1 and 5
df['Delivery_Rating'] = df['Delivery_Rating'].clip(lower=1, upper=5)
df['Restaurant_Rating'] = df['Restaurant_Rating'].clip(lower=1, upper=5)

# Profit Margin - should be positive
df['Profit_Margin'] = df['Profit_Margin'].clip(lower=0)

print("\nOutlier Treatment Done! ✅")
print("Max Delivery Time:", df['Delivery_Time_Min'].max())
print("Max Order Value:", df['Order_Value'].max())
# =============================
# FEATURE ENGINEERING
# =============================

# 1. Customer Age Group
df['Age_Group'] = pd.cut(df['Customer_Age'],
                          bins=[0, 25, 35, 50, 100],
                          labels=['Young', 'Adult', 'Middle-Age', 'Senior'])

# 2. Delivery Performance
df['Delivery_Performance'] = pd.cut(df['Delivery_Time_Min'],
                                     bins=[0, 30, 60, 120],
                                     labels=['Fast', 'Normal', 'Slow'])

# 3. Profit Margin %
df['Profit_Margin_Pct'] = df['Profit_Margin'] * 100

print("\nFeature Engineering Done! ✅")
print(df[['Customer_Age', 'Age_Group', 'Delivery_Time_Min',
          'Delivery_Performance', 'Profit_Margin_Pct']].head())
          # =============================
# EDA VISUALIZATIONS
# =============================

# 1. Top 5 Cities by Orders
plt.figure(figsize=(8,4))
df['City'].value_counts().head(5).plot(kind='bar', color='orange')
plt.title("Top 5 Cities by Orders")
plt.xlabel("City")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("top_cities.png")
plt.show()
print("Chart 1 Done! ✅")

# 2. Top 5 Cuisines
plt.figure(figsize=(8,4))
df['Cuisine_Type'].value_counts().head(5).plot(kind='bar', color='green')
plt.title("Top 5 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("top_cuisines.png")
plt.show()
print("Chart 2 Done! ✅")

# 3. Order Value Distribution
plt.figure(figsize=(8,4))
df['Order_Value'].hist(bins=30, color='blue')
plt.title("Order Value Distribution")
plt.xlabel("Order Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("order_value_dist.png")
plt.show()
print("Chart 3 Done! ✅")

# 4. Cancellation Reasons
plt.figure(figsize=(8,4))
df['Cancellation_Reason'].value_counts().head(6).plot(kind='bar', color='red')
plt.title("Cancellation Reasons")
plt.xlabel("Reason")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("cancellation_reasons.png")
plt.show()
print("Chart 4 Done! ✅")
# 5. Correlation Heatmap
plt.figure(figsize=(10,6))
numeric_cols = ['Customer_Age', 'Delivery_Time_Min', 'Distance_km',
                'Order_Value', 'Discount_Applied', 'Final_Amount',
                'Delivery_Rating', 'Profit_Margin']
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()
print("Chart 5 Done! ✅")

print("\n✅ Step 1 Complete! Data Cleaning + EDA Done!")