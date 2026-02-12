import csv

#Reading CSV file

with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV file content:")
    for row in reader:
        print(row)

#Writing CSV file
data = [
    ['Name', 'Age', 'Course'],
    ['Arjun', 23, 'Machine Learning'],
    ['Meena', 22, 'Data Analytics']
]

with open("new_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("new_data.csv created successfully!")