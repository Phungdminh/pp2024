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


school_system = SchoolSystem()

num_students = input_number_of_students()
for _ in range(num_students):
    student_id, name, dob = input_one_student()
    student = Student(student_id, name, dob)
    school_system.students.append(student)

num_courses = input_number_of_courses()
for _ in range(num_courses):
    course_id, name, credits = input_one_course()
    course = Course(course_id, name)
    school_system.courses[course.id] = course
    school_system.course_credits[course_id] = credits

for course in school_system.courses.values():
    school_system.select_course_and_input_student_marks(course)

school_system.sort_students_by_gpa()

display_students_gpa(school_system.students)