#List Comprehension Example

#Create squares of numbers
num = [1,2,3,4,5]
squares = [n**2 for n in num]
print("Square numbers:", squares)

#List of even numbers between 1-20
even_num = [n for n in range(1,21) if (n % 2==0)]
print("Even numbers:", even_num)

#Converts words to uppercase 
words = ['python', 'with', 'data', 'science']
uppercase = [word.upper() for word in words]
print("Upper:", uppercase)