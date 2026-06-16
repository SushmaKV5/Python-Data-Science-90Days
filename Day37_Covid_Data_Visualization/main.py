import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("covid_data.csv")

print("=== Dataset ===")
print(df)

# Set style
sns.set()

# 1. Barplot - Confirmed Cases
plt.figure()
sns.barplot(x="Country", y="Confirmed", data=df)
plt.title("Confirmed Cases by Country")
plt.xticks(rotation=30)
plt.show()

# 2. Barplot - Deaths
plt.figure()
sns.barplot(x="Country", y="Deaths", data=df)
plt.title("Deaths by Country")
plt.xticks(rotation=30)
plt.show()

# 3. Scatter Plot - Confirmed vs Deaths
plt.figure()
sns.scatterplot(x="Confirmed", y="Deaths", data=df)
plt.title("Confirmed vs Deaths")
plt.show()

# 4. Correlation Heatmap
plt.figure()
corr = df[["Confirmed", "Recovered", "Deaths"]].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
