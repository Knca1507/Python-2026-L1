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

    course = {"id": Course_Id,"name": Course_Name}

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

                marks[course_id][student["id"]] = mark

            break
    else:
        print("Course not found.")

#list function
def list_courses():
    print("\n COURSE LIST ")

    for course in courses:
        print("ID:", course["id"], "| Name:", course["name"])




def list_student():
    print("\n STUDENT LIST ")

    for student in students:
        print(" ID: ", student["id"]," Name: ", student["name"], " Dob: ", student["dob"])
    


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

list_courses()    
list_student()   
show_marks()     



