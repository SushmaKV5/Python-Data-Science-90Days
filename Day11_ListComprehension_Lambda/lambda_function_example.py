# Lambda function examples

# Simple addition
add = lambda a, b: a + b
print("Addition:", add(5, 3))

# Using map() with lambda
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares using map:", squares)

# Using filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)
