import pandas as pd
import matplotlib as plt

print("Loading dataset...")
sales_df = pd.reas_csv("sales_data.csv")
print(sales_df)

#Total sales by category
print("\n=== Total Sales by Category ===")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

# Total Profit by Category
print("\n=== Total Profit by Category ===")
category_profit = df.groupby("Category")["Profit"].sum()
print(category_profit)

# Top Selling Product
print("\n=== Top Selling Product ===")
top_product = df.loc[df["Sales"].idxmax()]
print(top_product)

# Visualization - Sales by Category
plt.figure()
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Visualization - Profit by Category
plt.figure()
category_profit.plot(kind="bar")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()
