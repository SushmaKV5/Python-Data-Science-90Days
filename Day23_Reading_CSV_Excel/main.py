import pandas as pd

print("=== Reading CSV File ===")

df = pd.read_csv("data.csv")
print("\nDataset:")
print(df)

print("\n=== First 3 Rows ===")
print(df.head(3))

print("\n=== Last 2 Rows ===")
print(df.tail(2))

print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Statistical Summary ===")
print(df.describe())

print("\n=== Column Names ===")
print(df.columns)

print("\n=== Access Specific Column ===")
print(df["Name"])

print("\n=== Access Multiple Columns ===")
print(df[["Name", "Score"]])
