import matplotlib.pyplot as plt

# Sample Data
days = [1, 2, 3, 4, 5]
sales = [100, 150, 200, 180, 220]
profit = [20, 30, 50, 40, 60]

# Line Plot
plt.figure()
plt.plot(days, sales)
plt.title("Sales Over Days")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

# Bar Chart
plt.figure()
plt.bar(days, profit)
plt.title("Profit by Day")
plt.xlabel("Days")
plt.ylabel("Profit")
plt.show()

# Multiple Line Plot
plt.figure()
plt.plot(days, sales, label="Sales")
plt.plot(days, profit, label="Profit")
plt.title("Sales vs Profit")
plt.xlabel("Days")
plt.ylabel("Values")
plt.legend()
plt.show()
