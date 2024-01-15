def inputNumberStudent():
    numOfStudent = input("Enter number of students:")
    return int(numOfStudent)

def inputOneStudent():
    id = input("Enter student Id")
    name = input("Enter student name")
    dob = input("Enter student Dob")
    student = {
        'id' : id,
        'name' : name,
        'dob' : dob,
    }
    return student

def inputNumberOfCourses ():
    numOfCourse = input("Enter a number of courses")
    return int(numOfCourse)

def inputOneCourse():
    id = input("Enter course Id")
    name = input("Enter course name")
    dob = input("Enter course  Dob")
    course = {
        'id' : id,
        'name' : name,
        'dob' : dob,
    }
    return course

def selectCourseAndInputStudentMarks(course, students):
    print(f"Enter marks for student in course {course['name']}") 
    marks = {}
    for student in students:
        mark = float(input(f"Enter marks for student{student['name']}"))
        studentMark = {
            'studentId': student['id'],
            'marks' : mark
        }
    return course,studentMark
