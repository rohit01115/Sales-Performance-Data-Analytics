
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. Load Dataset
# --------------------------------

df = pd.read_csv("cleaned.csv")

print("Dataset loaded successfully!")

# --------------------------------
# 2. Clean Sales Column
# --------------------------------

df["Sales"] = (
    df["Sales"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# Remove rows with invalid Sales
df = df.dropna(subset=["Sales"])

# --------------------------------
# 3. Graph 1: Sales by Category
# --------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("sales_by_category.png")
plt.show()

# --------------------------------
# 4. Graph 2: Monthly Sales Trend
# --------------------------------

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    format="mixed",
    errors="coerce"
)

date_df = df.dropna(subset=["Order Date"]).copy()

date_df["Month"] = date_df["Order Date"].dt.to_period("M")

monthly_sales = date_df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("monthly_sales_trend.png")
plt.show()

# --------------------------------
# 5. Graph 3: Sales by Region
# --------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("sales_by_region.png")
plt.show()

# --------------------------------
# 6. Graph 4: Top 5 Products
# --------------------------------

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .nlargest(5)
)

plt.figure(figsize=(10, 5))
top_products.plot(kind="bar")

plt.title("Top 5 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.savefig("top_5_products.png")
plt.show()

# --------------------------------
# 7. Print Business Observations
# --------------------------------

# print("\n========== BUSINESS OBSERVATIONS ==========")

# print("\n1. Highest Sales Category:")
# print(category_sales.idxmax())

# print("\n2. Highest Sales Region:")
# print(region_sales.idxmax())

# print("\n3. Top Selling Product:")
# print(top_products.index[0])

# print("\n4. Highest Sales Month:")
# print(monthly_sales.idxmax())

# print("\n5. Total Sales:")
# print(round(df["Sales"].sum(), 2))

# # --------------------------------
# # 8. Save Analysis Results
# # --------------------------------

# category_sales.to_csv("category_sales.csv")
# region_sales.to_csv("region_sales.csv")
# monthly_sales.to_csv("monthly_sales.csv")
# top_products.to_csv("top_5_products.csv")

# print("\nAll graphs and analysis files saved successfully!")
# print("DAY 4 COMPLETED!")
