# 🍔 Online Food Delivery Analysis

## Project Overview
Analysis of 1,00,000 online food delivery orders to extract
business insights on customer behavior, delivery performance,
and revenue trends.

## Project Structure
- `step1_foodproject.py` - Data Cleaning & EDA
- `step2_sql_connection.py` - MySQL Database Upload
- `step3_app.py` - Streamlit Dashboard
- `queries.sql` - SQL Analytics Queries
- `food_delivery_dashboard.pbix` - Power BI Dashboard

## Tools Used
- Python (Pandas, Matplotlib, Seaborn, Plotly)
- MySQL
- Streamlit
- Power BI

## Key KPIs
- Total Orders: 1,00,000
- Data Cleaning: Missing values handled using Mean/Median/Mode
- Outlier Treatment: Delivery Time capped at 120 mins
- Feature Engineering: Age Group, Delivery Performance

## How to Run
1. Install libraries: pip install pandas matplotlib seaborn plotly streamlit sqlalchemy pymysql
2. Run EDA: python step1_foodproject.py
3. Upload to MySQL: python step2_sql_connection.py
4. Run Dashboard: streamlit run step3_app.py