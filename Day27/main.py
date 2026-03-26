# Day 27 - Sorting & Ranking using Pandas

import pandas as pd

print("=== Loading Dataset ===")
df = pd.read_csv("data.csv")
print(df)

# Sort by Salary (Ascending)
print("\n=== Sort by Salary (Ascending) ===")
print(df.sort_values(by="Salary"))

# Sort by Salary (Descending)
print("\n=== Sort by Salary (Descending) ===")
print(df.sort_values(by="Salary", ascending=False))

# Sort by multiple columns
print("\n=== Sort by Department and Score ===")
print(df.sort_values(by=["Department", "Score"], ascending=[True, False]))

# Top 3 highest salaries
print("\n=== Top 3 Highest Salaries ===")
top_salary = df.sort_values(by="Salary", ascending=False).head(3)
print(top_salary)

# Bottom 2 scores
print("\n=== Bottom 2 Scores ===")
print(df.nsmallest(2, "Score"))

# Ranking based on Score
print("\n=== Ranking by Score ===")
df["Rank"] = df["Score"].rank(ascending=False)
print(df)

# Dense ranking (no gaps)
print("\n=== Dense Ranking ===")
df["Dense Rank"] = df["Score"].rank(method="dense", ascending=False)
print(df)

# Rank within each department
print("\n=== Rank within Department ===")
df["Dept Rank"] = df.groupby("Department")["Score"].rank(ascending=False)
print(df)
