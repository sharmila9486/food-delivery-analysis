# 📋 Student Information

| Field | Details |
|-------|---------|
| Name | Sharmila B |
| Batch No | DS-S-WD-T-B103 |
| Course | Data Science |
| Project | Online Food Delivery Analysis |
| Platform | GUVI - HCL |

# 🍔 Online Food Delivery Analysis - Project Documentation

## 1. Project Overview
This project analyzes 1,00,000 online food delivery orders to extract
meaningful business insights about customer behavior, delivery performance,
restaurant performance, and revenue trends.

## 2. Problem Statement
Online food delivery platforms like Swiggy and Zomato generate massive
volumes of data every day. This project aims to:
- Understand customer ordering behavior
- Identify operational inefficiencies in delivery
- Evaluate restaurant performance
- Track revenue, profit, and cancellations
- Provide data-driven insights for business decision-making

## 3. Dataset Information
- Total Records: 1,00,000 orders
- Total Features: 25 columns
- Source: Online Food Delivery Dataset

### Key Columns:
| Column | Description |
|--------|-------------|
| Order_ID | Unique order identifier |
| Customer_ID | Unique customer identifier |
| City | City of delivery |
| Cuisine_Type | Type of food ordered |
| Order_Value | Original order amount |
| Final_Amount | Amount after discount |
| Delivery_Time_Min | Time taken for delivery |
| Order_Status | Delivered/Cancelled |
| Profit_Margin | Profit percentage |
| Payment_Mode | Card/COD/UPI/Wallet |

## 4. Tools & Technologies Used
| Tool | Purpose |
|------|---------|
| Python | Data cleaning & EDA |
| Pandas | Data manipulation |
| Matplotlib & Seaborn | Visualizations |
| MySQL | Data storage |
| SQLAlchemy | Python-MySQL connection |
| Streamlit | Interactive dashboard |
| Power BI | Business dashboard |
| GitHub | Version control |

## 5. Data Cleaning & Preprocessing

### 5.1 Missing Values Handled:
| Column | Missing Count | Method Used |
|--------|--------------|-------------|
| Customer_Age | 50,093 | Mean |
| Final_Amount | 55,697 | Median |
| Delivery_Time_Min | 33,359 | Median |
| Peak_Hour | 32,962 | False |
| Cancellation_Reason | 90,969 | "Not Cancelled" |
| Payment_Mode | 19,911 | Mode |

### 5.2 Outlier Treatment:
- Delivery Time capped at 120 minutes
- Order Value capped at ₹2000
- Ratings clipped between 1 and 5
- Negative Profit Margin set to 0

### 5.3 Feature Engineering:
| New Column | Description |
|-----------|-------------|
| Age_Group | Young/Adult/Middle-Age/Senior |
| Delivery_Performance | Fast/Normal/Slow |
| Profit_Margin_Pct | Profit in percentage |

## 6. Exploratory Data Analysis (EDA)

### Key Findings:
- **Top Cities:** Bangalore leads in number of orders
- **Top Cuisines:** Indian cuisine is most popular
- **Payment Mode:** All modes equally preferred (~20% each)
- **Cancellation:** 90% orders successfully delivered
- **Cancellation Reasons:** Late Delivery, Customer Cancelled,
  Restaurant Issue

## 7. SQL Analytics (15 Queries)

### Customer & Order Analysis:
1. Top 10 spending customers identified
2. Age group vs order value analyzed
3. Weekend vs weekday order patterns studied

### Revenue & Profit Analysis:
4. Monthly revenue trends tracked
5. Discount impact on profit measured
6. High revenue cities identified

### Delivery Performance:
7. Average delivery time by city calculated
8. Distance vs delivery delay analyzed
9. Delivery rating vs delivery time studied

### Restaurant Performance:
10. Top rated restaurants identified
11. Cancellation rate by restaurant analyzed
12. Cuisine-wise performance evaluated

### Operational Insights:
13. Peak hour demand analyzed
14. Payment mode preferences studied
15. Cancellation reasons analyzed

## 8. Dashboard - Streamlit
Interactive web dashboard showing:
- Total Orders: 1,00,000
- Total Revenue
- Average Order Value
- Average Delivery Time
- Cancellation Rate
- Average Delivery Rating
- Profit Margin %

## 9. Dashboard - Power BI
Business intelligence dashboard with:
- City-wise Revenue Bar Chart
- Payment Mode Pie Chart
- Cuisine-wise Orders Chart
- Cancellation Reasons Chart

## 10. Business Recommendations
1. **Reduce Delivery Time:** Focus on cities with high delivery delays
2. **Reduce Cancellations:** Address Late Delivery issues
3. **Promote Top Cuisines:** Focus marketing on Indian cuisine
4. **Peak Hour Planning:** Add more delivery partners during peak hours
5. **Discount Strategy:** Optimize discounts to maintain profit margin

## 11. Challenges & Solutions
| Challenge | Solution |
|-----------|---------|
| Large missing values (50%+) | Used mean/median/mode imputation |
| Outliers in delivery time | Capped at 120 minutes |
| MySQL connection with special characters in password | Used SQLAlchemy URL.create() |
| Power BI personal account issue | Used Microsoft Fabric free account |

## 12. Project Files
| File | Description |
|------|-------------|
| step1_foodproject.py | Data cleaning & EDA |
| step2_sql_connection.py | MySQL upload |
| step3_app.py | Streamlit dashboard |
| queries.sql | 15 SQL queries |
| food_delivery_dashboard.pbix | Power BI dashboard |
| README.md | Project overview |