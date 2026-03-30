import pandas as pd

print("=== Loading Dataset ===")
df = pd.read_csv("data.csv")
print(df)

# 1. Average salary per department
print("\n=== Average Salary per Department ===")
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

# 2. Total salary per department
print("\n=== Total Salary per Department ===")
total_salary = df.groupby("Department")["Salary"].sum()
print(total_salary)

# 3. Highest salary employee
print("\n=== Highest Salary Employee ===")
highest_salary = df.loc[df["Salary"].idxmax()]
print(highest_salary)

# 4. Lowest score employee
print("\n=== Lowest Score Employee ===")
lowest_score = df.loc[df["Score"].idxmin()]
print(lowest_score)

# 5. Department with highest average score
print("\n=== Department with Highest Average Score ===")
avg_score = df.groupby("Department")["Score"].mean()
top_dept = avg_score.idxmax()
print("Top Department:", top_dept)
print("Average Score:", avg_score[top_dept])

# 6. Count employees per department
print("\n=== Employee Count per Department ===")
count = df["Department"].value_counts()
print(count)

# 7. Top 3 performers based on score
print("\n=== Top 3 Performers ===")
top_performers = df.sort_values(by="Score", ascending=False).head(3)
print(top_performers)
