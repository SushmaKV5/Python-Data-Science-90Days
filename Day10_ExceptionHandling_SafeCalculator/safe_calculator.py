#Safe calculator using Exception handling

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Safe Calculator:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

try:
    choice = int(input("Choose operation(1-4):"))
    num1 = float(input())
    num2 = float(input())

    if choice == 1:
        print("Result:", add(num1, num2))

    elif choice == 2:
        print("Result:", subtract(num1, num2))

    elif choice == 3:
        print("Result:", multiply(num1, num2))

    elif choice == 4:
        print("Result:", divide(num1, num2))

    else:
        print("Invalid operation selected!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

except Exception as e:
    print("Error: e")

finally:
    print("Execution completed successfully!")