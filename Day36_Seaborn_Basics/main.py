import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset
df = sns.load_dataset("tips")

print("=== Dataset Preview ===")
print(df.head())

# 1. Scatter Plot (Total Bill vs Tip)
plt.figure()
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total Bill vs Tip")
plt.show()

# 2. Histogram (Distribution)
plt.figure()
sns.histplot(df["total_bill"], bins=10)
plt.title("Distribution of Total Bill")
plt.show()

# 3. Boxplot (Outliers + Spread)
plt.figure()
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Total Bill by Day")
plt.show()

# 4. Barplot (Average values)
plt.figure()
sns.barplot(x="day", y="total_bill", data=df)
plt.title("Average Bill per Day")
plt.show()
