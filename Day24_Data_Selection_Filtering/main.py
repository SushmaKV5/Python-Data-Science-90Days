import pandas as pd

print("=== Loading Dataset ===")
df = pd.read_csv("data.csv")
print(df)

# Select a single column
print("\n=== Select Name Column ===")
print(df["Name"])

# Select multiple columns
print("\n=== Select Name and Score Columns ===")
print(df[["Name", "Score"]])

# Filter rows where Score > 85
print("\n=== Students with Score > 85 ===")
high_scores = df[df["Score"] > 85]
print(high_scores)

# Filter rows where Age < 24
print("\n=== Students with Age < 24 ===")
young_students = df[df["Age"] < 24]
print(young_students)

# Filter students from Bangalore
print("\n=== Students from Bangalore ===")
bangalore_students = df[df["City"] == "Bangalore"]
print(bangalore_students)

# Multiple conditions
print("\n=== Students with Score > 85 and Age > 24 ===")
filtered = df[(df["Score"] > 85) & (df["Age"] > 24)]
print(filtered)

# Sorting data by Score
print("\n=== Sorted by Score (Descending) ===")
sorted_df = df.sort_values(by="Score", ascending=False)
print(sorted_df)
