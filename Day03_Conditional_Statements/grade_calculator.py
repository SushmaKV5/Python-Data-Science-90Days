#Grade calculator based on marks

num = int(input("Enter the marks(0-100):"))

if num>=90:
    grade ='A+'
elif num>=80:
    grade='A'
elif num>=70:
    grade='B'
elif num>=60:
    grade='C'
elif num>=50:
    grade="D"
else:
    grade='Fail'

print(f"The grade is {grade}")