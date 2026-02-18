#map() and filter() task

numbers = [1,2,3,4,5,6,7,8,9]

#Using the map() to double the numbers
doubled = list(map(lambda x: x**2, numbers))
print("Doubled numbers:",doubled)

#Using filter() function to filter even numbers
even_num = list(filter(lambda x: x%2==0, numbers))
print("Even  numbers:", even_num)

#Using map() to square the even numbers
even_square = list(map(lambda x: x**2, even_num))
print("Square of even numbers:", even_square)