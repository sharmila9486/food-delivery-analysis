import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("data/ONLINE_FOOD_DELIVERY_ANALYSIS.csv")

# =============================
# DATA CLEANING (same as step1)
# =============================
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].mean())
df['Delivery_Time_Min'] = df['Delivery_Time_Min'].fillna(df['Delivery_Time_Min'].median())
df['Distance_km'] = df['Distance_km'].fillna(df['Distance_km'].median())
df['Order_Value'] = df['Order_Value'].fillna(df['Order_Value'].median())
df['Final_Amount'] = df['Final_Amount'].fillna(df['Final_Amount'].median())
df['Discount_Applied'] = df['Discount_Applied'].fillna(0)
df['Delivery_Rating'] = df['Delivery_Rating'].fillna(df['Delivery_Rating'].median())
df['Customer_Gender'] = df['Customer_Gender'].fillna(df['Customer_Gender'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])
df['Area'] = df['Area'].fillna(df['Area'].mode()[0])
df['Cuisine_Type'] = df['Cuisine_Type'].fillna(df['Cuisine_Type'].mode()[0])
df['Payment_Mode'] = df['Payment_Mode'].fillna(df['Payment_Mode'].mode()[0])
df['Cancellation_Reason'] = df['Cancellation_Reason'].fillna("Not Cancelled")
df['Peak_Hour'] = df['Peak_Hour'].fillna(False).infer_objects(copy=False)
df['Order_Date'] = df['Order_Date'].ffill()
df['Order_Time'] = df['Order_Time'].ffill()

# =============================
# MYSQL CONNECTION
# =============================

# உன் MySQL password இங்க போடு
from sqlalchemy import URL
connection_url = URL.create(
    "mysql+pymysql",
    username="root",
    password="Sharmi@#9818",  
    host="localhost",
    database="food_delivery_db"
)
engine = create_engine(connection_url)

# Upload to MySQL
df.to_sql("food_delivery", con=engine, if_exists="replace", index=False)

print("✅ Data uploaded to MySQL successfully!")
print(f"Total rows uploaded: {len(df)}")