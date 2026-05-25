USE food_delivery_db;

-- =============================
-- CUSTOMER & ORDER ANALYSIS
-- =============================

-- 1. Top 10 Spending Customers
SELECT Customer_ID, SUM(Final_Amount) AS Total_Spent
FROM food_delivery
GROUP BY Customer_ID
ORDER BY Total_Spent DESC
LIMIT 10;

-- 2. Age Group vs Order Value
SELECT 
    CASE 
        WHEN Customer_Age <= 25 THEN 'Young'
        WHEN Customer_Age <= 35 THEN 'Adult'
        WHEN Customer_Age <= 50 THEN 'Middle-Age'
        ELSE 'Senior'
    END AS Age_Group,
    AVG(Order_Value) AS Avg_Order_Value
FROM food_delivery
GROUP BY Age_Group
ORDER BY Avg_Order_Value DESC;

-- 3. Weekend vs Weekday Orders
SELECT Order_Day, COUNT(*) AS Total_Orders
FROM food_delivery
GROUP BY Order_Day
ORDER BY Total_Orders DESC;

-- =============================
-- REVENUE & PROFIT ANALYSIS
-- =============================

-- 4. Monthly Revenue
SELECT 
    MONTH(Order_Date) AS Month,
    SUM(Final_Amount) AS Total_Revenue
FROM food_delivery
GROUP BY Month
ORDER BY Month;

-- 5. Impact of Discount on Profit
SELECT 
    CASE 
        WHEN Discount_Applied = 0 THEN 'No Discount'
        ELSE 'Discount Applied'
    END AS Discount_Status,
    AVG(Profit_Margin) AS Avg_Profit
FROM food_delivery
GROUP BY Discount_Status;

-- 6. High Revenue Cities
SELECT City, SUM(Final_Amount) AS Total_Revenue
FROM food_delivery
GROUP BY City
ORDER BY Total_Revenue DESC
LIMIT 5;

-- =============================
-- DELIVERY PERFORMANCE
-- =============================

-- 7. Avg Delivery Time by City
SELECT City, AVG(Delivery_Time_Min) AS Avg_Delivery_Time
FROM food_delivery
GROUP BY City
ORDER BY Avg_Delivery_Time;

-- 8. Distance vs Delivery Time
SELECT 
    CASE 
        WHEN Distance_km <= 3 THEN 'Short'
        WHEN Distance_km <= 7 THEN 'Medium'
        ELSE 'Long'
    END AS Distance_Category,
    AVG(Delivery_Time_Min) AS Avg_Delivery_Time
FROM food_delivery
GROUP BY Distance_Category;

-- 9. Delivery Rating vs Delivery Time
SELECT 
    ROUND(Delivery_Rating) AS Rating,
    AVG(Delivery_Time_Min) AS Avg_Delivery_Time
FROM food_delivery
GROUP BY Rating
ORDER BY Rating;

-- =============================
-- RESTAURANT PERFORMANCE
-- =============================

-- 10. Top Rated Restaurants
SELECT Restaurant_Name, AVG(Restaurant_Rating) AS Avg_Rating
FROM food_delivery
GROUP BY Restaurant_Name
ORDER BY Avg_Rating DESC
LIMIT 10;

-- 11. Cancellation Rate by Restaurant
SELECT Restaurant_Name,
    COUNT(CASE WHEN Order_Status='Cancelled' THEN 1 END) * 100.0 / COUNT(*) AS Cancel_Rate
FROM food_delivery
GROUP BY Restaurant_Name
ORDER BY Cancel_Rate DESC
LIMIT 10;

-- 12. Cuisine wise Performance
SELECT Cuisine_Type,
    COUNT(*) AS Total_Orders,
    AVG(Restaurant_Rating) AS Avg_Rating,
    SUM(Final_Amount) AS Total_Revenue
FROM food_delivery
GROUP BY Cuisine_Type
ORDER BY Total_Revenue DESC;

-- =============================
-- OPERATIONAL INSIGHTS
-- =============================

-- 13. Peak Hour Demand
SELECT Peak_Hour, COUNT(*) AS Total_Orders
FROM food_delivery
GROUP BY Peak_Hour;

-- 14. Payment Mode Preference
SELECT Payment_Mode, COUNT(*) AS Total_Orders
FROM food_delivery
GROUP BY Payment_Mode
ORDER BY Total_Orders DESC;

-- 15. Cancellation Reasons
SELECT Cancellation_Reason, COUNT(*) AS Count
FROM food_delivery
GROUP BY Cancellation_Reason
ORDER BY Count DESC;