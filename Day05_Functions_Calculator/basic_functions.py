#Python basic functions

#Functions without parameter
def greet():
    print("Hello from Python function!")

greet()

#Function with parameter
def greet_user(name):
    print(f"Hello {name}, have a great day!")

user_name = "Sushma"
greet_user(user_name)

#Function with return value
def add(a,b):
    return a+b

res=add(68,19)
print("Sum:", res)