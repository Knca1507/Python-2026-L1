import math
from domains import Student, Course


def input_students():
    students = []

    number_students = int(
        input("Enter number of students in the class: ")
    )

    for i in range(number_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")

        student = Student(student_id, name, dob)
        students.append(student)

    return students


def input_courses():
    courses = []

    number_courses = int(
        input("\nEnter number of courses: ")
    )

    for i in range(number_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))

        course = Course(course_id, name, credit)
        courses.append(course)

    return courses


def input_marks(students, courses):
    while True:
        course_id = input(
            "\nEnter course ID to input marks "
            "(or '0' to finish): "
        )

        if course_id == "0":
            break

        selected_course = None

        for course in courses:
            if course.id == course_id:
                selected_course = course
                break

        if selected_course is None:
            print("Course not found.")
            continue

        print("\nEnter marks for course:", selected_course.name)

        for student in students:
            mark = float(
                input("Enter mark for " + student.name + ": ")
            )

            mark = math.floor(mark * 10) / 10

            student.add_mark(course_id, mark)