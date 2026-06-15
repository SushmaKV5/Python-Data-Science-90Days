import matplotlib.pyplot as plt
import numpy as np

# Generate data
np.random.seed(42)

days = np.arange(1, 11)
sales = np.random.randint(100, 300, 10)
profit = np.random.randint(20, 80, 10)
customers = np.random.randint(50, 200, 10)

# Create figure
plt.figure()

# 1. Line Plot (Sales Trend)
plt.subplot(2, 2, 1)
plt.plot(days, sales, marker='o')
plt.title("Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")

# 2. Bar Chart (Profit)
plt.subplot(2, 2, 2)
plt.bar(days, profit)
plt.title("Daily Profit")
plt.xlabel("Days")
plt.ylabel("Profit")

# 3. Histogram (Customers Distribution)
plt.subplot(2, 2, 3)
plt.hist(customers, bins=8)
plt.title("Customer Distribution")
plt.xlabel("Customers")
plt.ylabel("Frequency")

# 4. Scatter Plot (Sales vs Profit)
plt.subplot(2, 2, 4)
plt.scatter(sales, profit)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

# Overall title
plt.suptitle("Business Dashboard Analysis")

# Fix layout
plt.tight_layout()

plt.show()
