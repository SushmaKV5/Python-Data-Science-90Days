#Lambda practice example

#Square of a number
square = lambda x:x**2
print("Square of number:", square(10))

#Check odd or even
check_even = lambda x: "Even" if x%2==0 else "Odd"
print("Check number:", check_even(19))

#Maximum of two numbers
max = lambda a, b: a if a>b else b
print("Max of two numbers:", max(10,20))