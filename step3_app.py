import streamlit as st
import pandas as pd
import plotly.express as px

# =============================
# LOAD & CLEAN DATA
# =============================
df = pd.read_csv("data/ONLINE_FOOD_DELIVERY_ANALYSIS.csv")

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
# DASHBOARD TITLE
# =============================
st.set_page_config(page_title="Food Delivery Dashboard", page_icon="🍔", layout="wide")
st.title("🍔 Online Food Delivery Dashboard")

# =============================
# KPI METRICS
# =============================
st.subheader("📊 Key Performance Indicators")

col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", f"{len(df):,}")
col2.metric("Total Revenue", f"₹{df['Final_Amount'].sum():,.0f}")
col3.metric("Avg Order Value", f"₹{df['Order_Value'].mean():.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Avg Delivery Time", f"{df['Delivery_Time_Min'].mean():.2f} min")
col5.metric("Cancellation Rate", f"{(df['Order_Status']=='Cancelled').mean()*100:.2f}%")
col6.metric("Avg Delivery Rating", f"{df['Delivery_Rating'].mean():.2f}")

col7, col8 = st.columns(2)
col7.metric("Profit Margin %", f"{df['Profit_Margin'].mean()*100:.2f}%")
col8.metric("Avg Restaurant Rating", f"{df['Restaurant_Rating'].mean():.2f}")

# =============================
# CHARTS
# =============================
st.subheader("📈 Visual Analysis")

# Chart 1 - Top Cities
fig1 = px.bar(df['City'].value_counts().head(5).reset_index(),
              x='City', y='count',
              title="Top 5 Cities by Orders",
              color='count', color_continuous_scale='Oranges')
st.plotly_chart(fig1, use_container_width=True)

# Chart 2 - Top Cuisines
fig2 = px.bar(df['Cuisine_Type'].value_counts().head(5).reset_index(),
              x='Cuisine_Type', y='count',
              title="Top 5 Cuisines",
              color='count', color_continuous_scale='Greens')
st.plotly_chart(fig2, use_container_width=True)

# Chart 3 - Payment Mode
fig3 = px.pie(df, names='Payment_Mode',
              title="Payment Mode Preference")
st.plotly_chart(fig3, use_container_width=True)

# Chart 4 - Order Day
fig4 = px.bar(df['Order_Day'].value_counts().reset_index(),
              x='Order_Day', y='count',
              title="Weekend vs Weekday Orders",
              color='count', color_continuous_scale='Blues')
st.plotly_chart(fig4, use_container_width=True)

# Chart 5 - Cancellation Reasons
fig5 = px.bar(df['Cancellation_Reason'].value_counts().head(5).reset_index(),
              x='Cancellation_Reason', y='count',
              title="Top Cancellation Reasons",
              color='count', color_continuous_scale='Reds')
st.plotly_chart(fig5, use_container_width=True)
