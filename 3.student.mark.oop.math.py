import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course):
        mark = float(input(f"Enter marks for student {self.name} in course {course.name}: "))
        mark = math.floor(mark * 10) / 10  # Round down to 1-digit decimal
        self.marks[course.id] = mark

    def calculate_average_gpa(self, course_credits):
        total_weighted_marks = 0
        total_credits = 0
        for course_id, mark in self.marks.items():
            credit = course_credits.get(course_id, 0)
            total_weighted_marks += mark * credit
            total_credits += credit
        if total_credits == 0:
            return 0
        return total_weighted_marks / total_credits

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = {}
        self.course_credits = {}

    def input_number_of_students(self):
        return int(input("Enter number of students: "))

    def input_one_student(self):
        student_id = input("Enter student Id: ")
        name = input("Enter student name: ")
        dob = input("Enter student Dob: ")
        return Student(student_id, name, dob)

    def input_number_of_courses(self):
        return int(input("Enter a number of courses: "))

    def input_one_course(self):
        course_id = input("Enter course Id: ")
        name = input("Enter course name: ")
        self.course_credits[course_id] = int(input("Enter course credits: "))
        return Course(course_id, name)

    def select_course_and_input_student_marks(self, course):
        print(f"Enter marks for students in course {course.name}")
        for student in self.students:
            student.input_marks(course)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_average_gpa(self.course_credits), reverse=True)

    def display_students_gpa(self):
        for student in self.students:
            print(f"Student {student.name}: GPA - {student.calculate_average_gpa(self.course_credits)}")


# Example usage
school_system = SchoolSystem()

num_students = school_system.input_number_of_students()
for _ in range(num_students):
    student = school_system.input_one_student()
    school_system.students.append(student)

num_courses = school_system.input_number_of_courses()
for _ in range(num_courses):
    course = school_system.input_one_course()
    school_system.courses[course.id] = course

for course in school_system.courses.values():
    school_system.select_course_and_input_student_marks(course)
