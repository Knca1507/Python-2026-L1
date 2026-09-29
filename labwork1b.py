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

for course in courses:
    print("\nEnter marks for course:", course["name"])

    for student in students:
        mark = float(input(
            "Enter mark for " + student["name"] + ": "
        ))

        if course["id"] not in marks:
            marks[course["id"]] = {}

        marks[course["id"]][student["id"]] = mark

#lisr function
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
        print("\nCourse:", course["name"])
    
     if course_id not in marks:
            print("Course not found.")
            return

     if course_id in marks:
        print("\n STUDENT MARKS ")

        for student in students:
            print(  "ID:", student["id"]," Name:", student["name"]," Mark:", marks[course_id][student["id"]]
        )

list_courses()    
list_student()   
show_marks()     



