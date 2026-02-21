students = []

#Add a new student
def add_student(name, age, grade):
    student = {
        "name" : name,
        "age" : age,
        "grade" : grade
    }
    students.append(student)
    print("Student added successfully!")

#view all students
def view_student():
    if not students:
        print("No student found!")
    else:
        print("Student List:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

#Search for a student
def search_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            print("Student found:", student)
            return
    print("Student not found!")

#Delete a student
def delete_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")