import os
import bz2
import pickle

from input import *
from output import display_students_gpa
from domains.student import Student
from domains.course import Course

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = {}
        self.course_credits = {}

    def select_course_and_input_student_marks(self, course):
        print(f"Enter marks for students in course {course.name}")
        for student in self.students:
            student.input_marks(course)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_average_gpa(self.course_credits), reverse=True)

def load_data_from_file():
    if os.path.exists("students.dat"):
        with bz2.BZ2File("students.dat", "rb") as f:
            data = f.read()
            return pickle.loads(data)
    else:
        print("students.dat doesn't exist. Starting with empty data.")
        return [], {}, []

def save_data_to_file(data):
    with bz2.BZ2File("students.dat", "wb") as f:
        f.write(pickle.dumps(data))

if __name__ == "__main__":
    students, courses, marks = load_data_from_file()
    school_system = SchoolSystem()

    if not students:
        num_students = input_number_of_students()
        for _ in range(num_students):
            student_id, name, dob = input_one_student()
            students.append(Student(student_id, name, dob))

    if not courses:
        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            course_id, name, credits = input_one_course()
            courses[course_id] = Course(course_id, name)

    # Input marks
    input_marks(students, courses)

    # Save data to file
    save_data_to_file((students, courses, marks))