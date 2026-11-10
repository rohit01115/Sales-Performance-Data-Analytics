Create database sales_analytics;
use sales_analytics;
CREATE TABLE sales (
    `Row ID` INT,
    `Order ID` VARCHAR(50),
    `Order Date` VARCHAR(20),
    `Ship Date` VARCHAR(20),
    `Ship Mode` VARCHAR(50),
    `Customer ID` VARCHAR(50),
    `Customer Name` VARCHAR(100),
    `Segment` VARCHAR(50),
    `Country` VARCHAR(100),
    `City` VARCHAR(100),
    `State` VARCHAR(100),
    `Postal Code` VARCHAR(20),
    `Region` VARCHAR(50),
    `Product ID` VARCHAR(50),
    `Category` VARCHAR(50),
    `Sub-Category` VARCHAR(50),
    `Product Name` VARCHAR(255),
    `Sales` VARCHAR(30)
);
SELECT * FROM sales LIMIT 10;
select * from sales;
CREATE VIEW sales_clean AS
SELECT
    `Row ID`,
    `Order ID`,
    STR_TO_DATE(`Order Date`, '%d-%m-%Y') AS Order_Date,
    STR_TO_DATE(`Ship Date`, '%d-%m-%Y') AS Ship_Date,
    `Ship Mode`,
    `Customer ID`,
    `Customer Name`,
    Segment,
    Country,
    City,
    State,
    Region,
    `Product ID`,
    Category,
    `Sub-Category`,
    `Product Name`,
    CAST(
        REPLACE(
            REPLACE(Sales, '$', ''),
            ',', ''
        ) AS DECIMAL(12,2)
    ) AS Sales
FROM sales;

SELECT * FROM sales_clean LIMIT 10;
SELECT SUM(Sales) AS Total_Sales
FROM sales_clean;
SELECT AVG(Sales) AS Average_Sales
FROM sales_clean;

SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM sales_clean
GROUP BY Category
ORDER BY Total_Sales DESC;

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM sales_clean
GROUP BY Region
ORDER BY Total_Sales DESC;

SELECT
    `Product Name`,
    SUM(Sales) AS Total_Sales
FROM sales_clean
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT
    Region,
    SUM(sales)AS total_sales
FROM sales_clean
GROUP BY Region
ORDER BY total_sales DESC;

SELECT
    SUBSTR("Order Date", 4, 7) AS month,
    SUM(sales) AS monthly_sales
FROM sales_clean
GROUP BY month
ORDER BY SUBSTR("Order Date", 7, 4),
         SUBSTR("Order Date", 4, 2);
         
select * from sales_clean where category= 'Technology';
select sum(sales) from sales_clean where category= 'Technology';

select Region, sum(sales) as total_sales from sales_clean group by Region having total_sales> 5000;

select count(distinct "Customer ID")as unique_customer from sales_clean;
select Region, count(distinct "OrderID") as total_orders from sales_clean group by Region;
SELECT
    "Product Name",
    SUM(sales) AS total_sales
FROM sales_clean
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 1;

select sum(sales)from sales_clean where category='Furniture';
select city,sum(sales)as total_sales from sales_clean group by city order by total_sales desc limit 5;

CREATE TABLE customers AS
SELECT DISTINCT
    "Customer ID",
    "Customer Name",
    Segment,
    Region
FROM sales;

DROP TABLE IF EXISTS customers;

CREATE TABLE customers AS
SELECT DISTINCT
    `Customer ID`,
    `Customer Name`,
    Segment,
    Region
FROM sales_clean;

SELECT
    c.`Customer ID`,
    c.`Customer Name`,
    s.`Order ID`,
    s.`Product Name`,
    s.Sales
FROM customers AS c
LEFT JOIN sales_clean AS s
    ON c.`Customer ID` = s.`Customer ID`;
    
    SHOW TABLES;
    
    SELECT
    c.`Customer ID`,
    c.`Customer Name`,
    s.`Order ID`,
    s.`Product Name`,
    s.Sales
FROM customers AS c
right JOIN sales_clean AS s
    ON c.`Customer ID` = s.`Customer ID`;
    
      SELECT
    c.`Customer ID`,
    c.`Customer Name`,
    s.`Order ID`,
    s.`Product Name`,
    s.Sales
FROM customers AS c
inner JOIN sales_clean AS s
    ON c.`Customer ID` = s.`Customer ID`;
    
    SELECT
    "Product Name",
    Sales
FROM sales
WHERE sales >
(
    SELECT AVG(sales)
    FROM sales_clean
);

