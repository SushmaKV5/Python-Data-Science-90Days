import pandas as pd

print("=== Loading Dataset ===")
df = pd.read_csv("data.csv")
print(df)

# Detect missing values
print("\n=== Checking Missing Values ===")
print(df.isnull())

# Count missing values
print("\n=== Count Missing Values ===")
print(df.isnull().sum())

# Drop rows with missing values
print("\n=== Dropping Missing Values ===")
df_dropped = df.dropna()
print(df_dropped)

# Fill missing values
print("\n=== Filling Missing Values ===")

# Fill Age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill City with 'Unknown'
df["City"].fillna("Unknown", inplace=True)

# Fill Score with 0
df["Score"].fillna(0, inplace=True)

print(df)

# Forward fill method
print("\n=== Forward Fill ===")
print(df.fillna(method='ffill'))
