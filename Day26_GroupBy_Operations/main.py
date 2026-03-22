# Day 26 - GroupBy Operations using Pandas

import pandas as pd

print("=== Loading Dataset ===")
df = pd.read_csv("data.csv")
print(df)

# Group by Department
print("\n=== Group by Department ===")
grouped = df.groupby("Department")
print(grouped)

# Mean salary per department
print("\n=== Average Salary per Department ===")
print(grouped["Salary"].mean())

# Total salary per department
print("\n=== Total Salary per Department ===")
print(grouped["Salary"].sum())

# Count of employees per department
print("\n=== Employee Count per Department ===")
print(grouped["Name"].count())

# Multiple aggregations
print("\n=== Multiple Aggregations ===")
print(grouped["Salary"].agg(["mean", "max", "min"]))

# Group by multiple columns
print("\n=== Group by Department and Age ===")
print(df.groupby(["Department", "Age"])["Salary"].mean())
