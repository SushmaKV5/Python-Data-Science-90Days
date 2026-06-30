import numpy as np

# Example 1: Coin Toss Simulation
print("=== Coin Toss Simulation ===")

tosses = np.random.choice(['Head', 'Tail'], size=1000)

# Count occurrences
heads = np.sum(tosses == 'Head')
tails = np.sum(tosses == 'Tail')

print("Heads:", heads)
print("Tails:", tails)

print("Probability of Heads:", heads / 1000)
print("Probability of Tails:", tails / 1000)


# Example 2: Dice Roll Simulation
print("\n=== Dice Roll Simulation ===")

rolls = np.random.randint(1, 7, 1000)

# Probability of getting a 6
prob_6 = np.sum(rolls == 6) / 1000

print("Probability of getting 6:", prob_6)


# Example 3: Simple Probability Calculation

# Probability formula: P(A) = Favorable Outcomes / Total Outcomes
print("\n=== Manual Probability ===")

favorable = 1   # rolling a 3
total = 6       # dice outcomes

print("Probability of getting 3 on dice:", favorable / total)
