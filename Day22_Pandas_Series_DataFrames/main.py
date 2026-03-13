import pandas as pd
import numpy as np

print("=== Creating Pandas Series ===")

data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Series:")
print(series)

print("\n=== Accessing Elements ===")
print("First element:", series[0])
print("Last element:", series[4])

print("\n=== Creating Series with Labels ===")

series2 = pd.Series(data, index=["A", "B", "C", "D", "E"])
print(series2)

print("\nValue with label C:", series2["C"])


print("\n=== Creating DataFrame ===")

data_dict = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [23, 25, 22, 24],
    "Score": [85, 90, 78, 88]
}

df = pd.DataFrame(data_dict)

print(df)


print("\n=== Accessing Columns ===")
print(df["Name"])


print("\n=== Accessing Rows ===")
print(df.loc[0])
print(df.loc[2])


print("\n=== Basic DataFrame Info ===")
print("Shape:", df.shape)
print("Columns:", df.columns)


print("\n=== Statistical Summary ===")
print(df.describe())
