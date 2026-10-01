
import math
import numpy as np


students = []
courses = []
marks = {}


#Student
number_students = int(input("Enter number of student in the class : "))
for i in range(number_students):
    Student_Id = (input("Enter student id: "))
    Student_Name = (input("Enter student name: "))
    DoB = (input("Enter student DoB: "))

    student = {"id": Student_Id, "name":Student_Name,"dob":DoB}

    students.append(student)

#Course
number_courses = int(input("\nEnter number of courses: "))
for i in range(number_courses):
    Course_Id = (input("Enter the Course id: "))
    Course_Name = (input("Enter the Course name: "))
    Course_Credit = int(input("Enter the Course credit: "))

    course = {"id": Course_Id,"name": Course_Name, "credit": Course_Credit}

    courses.append(course)

#Marks
while True:
    course_id = input("\nEnter course ID to input marks (enter '0' when finish): ")

    if course_id == "0":
        break

    for course in courses:
        if course["id"] == course_id:
            print("\nEnter marks for course:", course["name"])

            marks[course_id] = {}

            for student in students:
                mark = float(input(
                    "Enter mark for " + student["name"] + ": "
                ))

                mark=math.floor(mark*10)/10

                marks[course_id][student["id"]] = mark

            break
    else:
        print("Course not found.")

#list function
def list_courses():
    print("\n COURSE LIST ")

    for course in courses:
        print("ID:", course["id"], "| Name:", course["name"],"Credit:", course["credit"])




def list_student():
    print("\n STUDENT LIST ")

    for student in students:
        print(" ID: ", student["id"]," Name: ", student["name"], " Dob: ", student["dob"]
              )
    


def show_marks():
    course_id = input("\nEnter course ID: ")

    for course in courses:
        if course["id"] == course_id:
            print("\nCourse:", course["name"])

            if course_id not in marks:
                print("No marks have been entered for this course.")
                return

            print("\nSTUDENT MARKS")

            for student in students:
                print(
                    "ID:", student["id"],
                    "Name:", student["name"],
                    "Mark:", marks[course_id][student["id"]]
                )

            return

    print("Course not found.")

def calculate_gpa(student_id):
    marks_array = []
    credits_array = []

    for course in courses:
        course_id = course["id"]

        if course_id in marks:
            if student_id in marks[course_id]:
                marks_array.append(marks[course_id][student_id])
                credits_array.append(course["credit"])

    if len(marks_array) == 0:
        return 0

    marks_array = np.array(marks_array)
    credits_array = np.array(credits_array)

    weighted_sum = np.sum(marks_array * credits_array)
    total_credits = np.sum(credits_array)

    return weighted_sum / total_credits


def show_gpa():
    student_id = input("\nEnter student ID: ")

    for student in students:
        if student["id"] == student_id:
            gpa = calculate_gpa(student_id)

            print(
                "Student:",
                student["name"],
                "| GPA:",
                gpa
            )

            return

    print("Student not found.")

def sort_students_by_gpa():
    students_with_gpa = []

    for student in students:
        gpa = calculate_gpa(student["id"])

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
            "ID:", student["id"],
            "| Name:", student["name"],
            "| GPA:", gpa
        )

list_courses()    
list_student()   
show_marks()     
show_gpa()


