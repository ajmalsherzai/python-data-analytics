# Python Data Analytics Project
# Created by Ajmal Sherzai

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample business sales dataset
data = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "customer_name": ["John Smith", "Maria Garcia", "David Lee", "Ashley Brown", "Michael Johnson",
                      "Sarah Wilson", "Daniel Kim", "Jessica Davis", "Robert Miller", "Emily Clark"],
    "region": ["West", "West", "North", "South", "East", "West", "North", "South", "East", "West"],
    "product_category": ["Electronics", "Office Supplies", "Furniture", "Electronics", "Furniture",
                         "Office Supplies", "Electronics", "Furniture", "Office Supplies", "Electronics"],
    "quantity": [2, 5, 1, 3, 2, 4, 1, 2, 6, 3],
    "unit_price": [499.99, 12.99, 149.99, 249.99, 199.99, 24.99, 899.99, 179.99, 9.99, 299.99]
}

df = pd.DataFrame(data)

# Add revenue column
df["revenue"] = df["quantity"] * df["unit_price"]

# Display first rows
print("First five rows:")
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Total revenue
total_revenue = df["revenue"].sum()
print("\nTotal Revenue: $", round(total_revenue, 2))

# Average order value
average_order_value = df["revenue"].mean()
print("Average Order Value: $", round(average_order_value, 2))

# Revenue by product category
revenue_by_category = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Product Category:")
print(revenue_by_category)

# Revenue by region
revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(revenue_by_region)

# Best performing product category
top_category = revenue_by_category.idxmax()
print("\nTop Product Category:", top_category)

# Best performing region
top_region = revenue_by_region.idxmax()
print("Top Region:", top_region)

# Chart: Revenue by Product Category
plt.figure(figsize=(8, 5))
revenue_by_category.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Chart: Revenue by Region
plt.figure(figsize=(8, 5))
revenue_by_region.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Business Insights
print("\nBusiness Insights:")
print(f"- Total revenue was ${round(total_revenue, 2)}.")
print(f"- The average order value was ${round(average_order_value, 2)}.")
print(f"- The top product category was {top_category}.")
print(f"- The highest revenue region was {top_region}.")
print("- This analysis can help a business understand product performance, regional sales, and customer purchasing behavior.")
