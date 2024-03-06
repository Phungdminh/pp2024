import os
import shutil
import bz2

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

def load_data_from_files():
    students = []
    courses = {}
    marks = []

    if os.path.exists("students.dat"):
        # Decompress and load data
        with bz2.BZ2File("students.dat", "rb") as f:
            data = f.read().decode('utf-8').split('\n')
            for line in data:
                if line.startswith("STUDENT"):
                    _, student_id, name, dob = line.split(',')
                    students.append((student_id, name, dob))
                elif line.startswith("COURSE"):
                    _, course_id, name, credits = line.split(',')
                    courses[course_id] = (name, credits)
                elif line.startswith("MARK"):
                    _, student_id, course_id, mark = line.split(',')
                    marks.append((student_id, course_id, mark))
    else:
        print("students.dat doesn't exist. Starting with empty data.")
    
    return students, courses, marks

def write_data_to_files(students, courses, marks):
    # Write student info to students.txt
    with open("students.txt", "w") as f:
        for student in students:
            f.write(",".join(student) + "\n")

    # Write course info to courses.txt
    with open("courses.txt", "w") as f:
        for course_id, (name, credits) in courses.items():
            f.write(f"{course_id},{name},{credits}\n")

    # Write marks to marks.txt
    with open("marks.txt", "w") as f:
        for mark in marks:
            f.write(",".join(mark) + "\n")

def compress_data():
    with open("students.txt", "rb") as f:
        data = f.read()
        with bz2.BZ2File("students.dat", "wb") as compressed_file:
            compressed_file.write(data)

    # Remove the temporary files
    os.remove("students.txt")
    os.remove("courses.txt")
    os.remove("marks.txt")

if __name__ == "__main__":
    students, courses, _ = load_data_from_files()
    school_system = SchoolSystem()

    if not students:
        num_students = input_number_of_students()
        for _ in range(num_students):
            student_id, name, dob = input_one_student()
            students.append((student_id, name, dob))

    if not courses:
        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            course_id, name, credits = input_one_course()
            courses[course_id] = (name, credits)

    # Input marks
    input_marks(students, courses)

    # Write data to files
    write_data_to_files(students, courses, marks)

    # Compress data
    compress_data()