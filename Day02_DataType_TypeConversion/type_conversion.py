#Type conversion example

#User input(input is always a string)
num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

print("\nBefore conversion:")
print("Num1:", num1, type(num1))
print("Num2:", num2, type(num2))

#Convert string to input
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2

print("\nAfter conversion")
print("Sum:", sum, type(sum))

#Other conversion
price = 99.45
price_int = int(price)

age = 21
age_str = str(age)

print("Other conversion")
print("Float to integer:", price_int, type(price_int))
print("Integer to string:", age_str, type(age_str))