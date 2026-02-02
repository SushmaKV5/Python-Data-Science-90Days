#Multiplication table using loops

n = int(input("Enter a number:"))

print("Multiplication table using while loop")
i = 1
while i<=10:
    print(f"{n} X {i} = {n*i}")
    i +=1

print("\nMultiplication table using for loop")
for i in range (1,11):
    print(f"{n} X {i} = {n*i}")