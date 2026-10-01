from input import input_students, input_courses, input_marks
from output import (
    list_courses,
    list_students,
    show_marks,
    show_gpa,
    sort_students_by_gpa
)


def main():
    students = input_students()

    courses = input_courses()

    input_marks(students, courses)

    while True:
        print("\n==============================")
        print(" STUDENT MARK MANAGEMENT")
        print("==============================")
        print("1. List courses")
        print("2. List students")
        print("3. Show student marks")
        print("4. Show student GPA")
        print("5. Sort students by GPA")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_courses(courses)

        elif choice == "2":
            list_students(students)

        elif choice == "3":
            show_marks(students, courses)

        elif choice == "4":
            show_gpa(students, courses)

        elif choice == "5":
            sort_students_by_gpa(students, courses)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()