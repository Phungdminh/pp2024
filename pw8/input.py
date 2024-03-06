import math

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_one_student():
    student_id = input("Enter student Id: ")
    name = input("Enter student name: ")
    dob = input("Enter student Dob: ")
    return student_id, name, dob

def input_number_of_courses():
    return int(input("Enter a number of courses: "))

def input_one_course():
    course_id = input("Enter course Id: ")
    name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    return course_id, name, credits

def input_marks(students, courses):
    for course_id, course_name in courses.items():
        with open(f'marks.txt', 'a') as f:
            for student_id, student_name, _ in students:
                mark = float(input(f"Enter marks for student {student_name} in course {course_name}: "))
                mark = math.floor(mark * 10) / 10  # Round down to 1-digit decimal
                f.write(f"{student_id},{course_id},{mark}\n")