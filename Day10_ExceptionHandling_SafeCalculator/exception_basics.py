#Basic Exception Handling Example

try:
    num = int(input("Enter a number:"))
    res = 100 / num
    print(res)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid value, enter a valid input")

else:
    print("Calculation successfull!")

finally:
    print("Execution completed!")