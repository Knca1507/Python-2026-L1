import numpy as np


def list_courses(courses):
    print("\nCOURSE LIST")

    for course in courses:
        print(
            "ID:", course.id,
            "| Name:", course.name,
            "| Credit:", course.credit
        )


def list_students(students):
    print("\nSTUDENT LIST")

    for student in students:
        print(
            "ID:", student.id,
            "| Name:", student.name,
            "| DoB:", student.dob
        )


def show_marks(students, courses):
    course_id = input("\nEnter course ID: ")

    selected_course = None

    for course in courses:
        if course.id == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    print("\nCourse:", selected_course.name)

    print("\nSTUDENT MARKS")

    for student in students:
        mark = student.get_mark(course_id)

        if mark is None:
            print(
                "ID:", student.id,
                "| Name:", student.name,
                "| No mark"
            )
        else:
            print(
                "ID:", student.id,
                "| Name:", student.name,
                "| Mark:", mark
            )


def calculate_gpa(student, courses):
    marks_array = []
    credits_array = []

    for course in courses:
        mark = student.get_mark(course.id)

        if mark is not None:
            marks_array.append(mark)
            credits_array.append(course.credit)

    if len(marks_array) == 0:
        return 0

    marks_array = np.array(marks_array)
    credits_array = np.array(credits_array)

    weighted_sum = np.sum(marks_array * credits_array)
    total_credits = np.sum(credits_array)

    return weighted_sum / total_credits


def show_gpa(students, courses):
    student_id = input("\nEnter student ID: ")

    for student in students:
        if student.id == student_id:
            gpa = calculate_gpa(student, courses)

            print(
                "Student:", student.name,
                "| GPA:", gpa
            )

            return

    print("Student not found.")


def sort_students_by_gpa(students, courses):
    students_with_gpa = []

    for student in students:
        gpa = calculate_gpa(student, courses)

        students_with_gpa.append(
            (student, gpa)
        )

    students_with_gpa.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\nSTUDENTS SORTED BY GPA")

    for student, gpa in students_with_gpa:
        print(
            "ID:", student.id,
            "| Name:", student.name,
            "| GPA:", gpa
        )