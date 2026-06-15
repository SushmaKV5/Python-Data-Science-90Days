import matplotlib.pyplot as plt
import numpy as np

# Sample Data
np.random.seed(42)

# Study hours vs scores
study_hours = np.random.randint(1, 10, 20)
scores = study_hours * 10 + np.random.randint(-5, 5, 20)

print("Study Hours:", study_hours)
print("Scores:", scores)

# 1. Basic Scatter Plot
plt.figure()
plt.scatter(study_hours, scores)

plt.title("Study Hours vs Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")

plt.show()


# 2. Scatter Plot with Multiple Variables
hours_group1 = np.random.randint(1, 10, 15)
scores_group1 = hours_group1 * 9 + np.random.randint(-5, 5, 15)

hours_group2 = np.random.randint(1, 10, 15)
scores_group2 = hours_group2 * 11 + np.random.randint(-5, 5, 15)

plt.figure()
plt.scatter(hours_group1, scores_group1, label="Group 1")
plt.scatter(hours_group2, scores_group2, label="Group 2")

plt.title("Comparison of Two Groups")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.legend()

plt.show()
