import pandas as pd
import numpy as np

print("Loading dataset...")

df = pd.read_csv("cleaned.csv")


print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nRows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nPython analysis completed!")

# Basic data exploration

print("\nTotal number of rows:")
print(len(df))

print("\nDataset shape:")
print(df.shape)

print("\nColumn data types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe())

print("\nLast 5 rows:")
print(df.tail())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Sales by Category

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

top_5_products = df.groupby("Product Name")["Sales"].sum().nlargest(5)
print("\nTop 5 Products by Sales:")
print(top_5_products)

monthly_sales = df.groupby("Order Date")["Sales"].sum().resample("M").sum()
print("\nMonthly Sales:")   
print(monthly_sales)

# Clean and convert Sales column into numbers

# df["Sales"] = (
#     df["Sales"]
#     .astype(str)
#     .str.replace("$", "", regex=False)
#     .str.replace(",", "", regex=False)
#     .str.strip()
# )

# df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# Convert Order Date into datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d-%m-%Y"
)

# Extract month
df["Month"] = df["Order Date"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)