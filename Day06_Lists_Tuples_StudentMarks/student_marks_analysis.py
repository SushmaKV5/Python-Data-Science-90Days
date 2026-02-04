#Student's marks analysis using Lists

student_name = input("Enter the student name:")

subjects =["English", "History", "Maths", "Science", "Computer"]
marks = []

for subject in subjects:
    score = int(input())
    marks.append(score)

total_score = sum(marks)
average_score = total_score/len(marks)
highest_score = max(marks)
lowest_score = min(marks)

print("\nStudent marks analysis:\n")
print("Student name:", student_name)
print("Subject wise marks:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]}")
print("Total marks:", total_score)
print("Average marks:", average_score)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

#Grade logic
if average_score>=90:
    grade ="A+"
elif average_score>=80:
    grade="A"
elif average_score>=70:
    grade="B"
elif average_score>=60:
    grade="C"
else:
    grade = "Fail"

print("Grade:", grade)