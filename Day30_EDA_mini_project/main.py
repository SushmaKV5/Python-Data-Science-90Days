import pandas as pd
import matplotlib.pyplot as plt

print("=== Loading Dataset ===")
df = pd.read_csv("data.csv")

# 1. Basic Info
print("\n=== Dataset Info ===")
print(df.info())

print("\n=== First 5 Rows ===")
print(df.head())

# 2. Statistical Summary
print("\n=== Statistical Summary ===")
print(df.describe())

# 3. Check Missing Values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# 4. Group Analysis
print("\n=== Average Salary by Department ===")
print(df.groupby("Department")["Salary"].mean())

print("\n=== Average Score by Department ===")
print(df.groupby("Department")["Score"].mean())

# 5. Top Performers
print("\n=== Top 3 Performers ===")
print(df.sort_values(by="Score", ascending=False).head(3))

# 6. Visualization - Salary Distribution
plt.figure()
plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# 7. Visualization - Average Score by Department
dept_score = df.groupby("Department")["Score"].mean()

plt.figure()
dept_score.plot(kind="bar")
plt.title("Average Score by Department")
plt.xlabel("Department")
plt.ylabel("Score")
plt.show()
