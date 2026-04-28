import matplotlib.pyplot as plt

# Sample Data
days = [1, 2, 3, 4, 5]
sales_2024 = [100, 150, 200, 180, 220]
sales_2025 = [120, 170, 210, 190, 250]

# 1. Line Chart Comparison
plt.figure()
plt.plot(days, sales_2024, marker='o', label="Sales 2024")
plt.plot(days, sales_2025, marker='o', label="Sales 2025")

plt.title("Sales Comparison (2024 vs 2025)")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.grid()

plt.show()


# 2. Bar Chart Comparison
x = range(len(days))

plt.figure()
plt.bar(x, sales_2024, width=0.4, label="2024")
plt.bar([i + 0.4 for i in x], sales_2025, width=0.4, label="2025")

plt.title("Sales Comparison (Bar Chart)")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.xticks([i + 0.2 for i in x], days)
plt.legend()

plt.show()


# 3. Horizontal Bar Chart
products = ["Laptop", "Phone", "Tablet"]
profits = [12000, 10000, 5000]

plt.figure()
plt.barh(products, profits)

plt.title("Profit by Product")
plt.xlabel("Profit")
plt.ylabel("Products")

plt.show()
