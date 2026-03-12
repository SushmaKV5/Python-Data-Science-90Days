import numpy as np

print("Weather Data Analysis\n")

#Load the weather data
data = np.loadtxt("weather_data.txt")
print("Temperature data:\n", data)

#Basic statistics
print("\n===Basic Statistics===")
print("Average temperature:", np.mean(data))
print("Minimum temperature:", np.min(data))
print("Maximum temperature:", np.max(data))

#Standard Deviation
print("\n===Temperature Variation===")
print("Standard Deviation:", np.std(data))

#Days hotter than average
print("\nDays hotter than average===")
average = np.mean(data)
hot_days = data[data>average]
print("Temperature above average:", hot_days)

#Sorting temperature
print("\nSorted Temperature===")
print(np.sort(data))
