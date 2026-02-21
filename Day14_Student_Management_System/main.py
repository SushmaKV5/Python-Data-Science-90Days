#import the student_manager.py
from student_manager import add_student, view_student, search_student, delete_student

def main():
    while True:
        print("\n====Student Management System====")
        print("1. Add student")
        print("2. View student")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        choice = int(input("Enter your choice(1-5):"))

        if choice == 1:
            name = input("Enter student's name:")
            age = int(input("Enter student's age:"))
            grade = input("Enter student's grade:")
            add_student(name, age, grade)
        elif choice == 2:
            view_student()
        elif choice == 3:
            name = input("Enter the student's name:")
            search_student(name)
        elif choice == 4:
            name = input("Enter the student's name:")
            delete_student(name)
        elif choice == 5:
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice...Try again")

#Run the program
main()