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