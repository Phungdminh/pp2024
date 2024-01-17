class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course):
        mark = float(input(f"Enter marks for student {self.name} in course {course.name}: "))
        self.marks[course.id] = mark


class Course:
    def __init__(self, course_id, name, dob):
        self.id = course_id
        self.name = name
        self.dob = dob


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        num_of_students = int(input("Enter number of students:"))
        return num_of_students

    def input_one_student(self):
        student_id = input("Enter student Id: ")
        name = input("Enter student name: ")
        dob = input("Enter student Dob: ")
        return Student(student_id, name, dob)

    def input_number_of_courses(self):
        num_of_courses = int(input("Enter a number of courses: "))
        return num_of_courses

    def input_one_course(self):
        course_id = input("Enter course Id: ")
        name = input("Enter course name: ")
        dob = input("Enter course Dob: ")
        return Course(course_id, name, dob)

    def select_course_and_input_student_marks(self, course):
        print(f"Enter marks for students in course {course.name}")
        for student in self.students:
            student.input_marks(course)

# Example usage
school_system = SchoolSystem()

num_students = school_system.input_number_of_students()
for _ in range(num_students):
    student = school_system.input_one_student()
    school_system.students.append(student)

num_courses = school_system.input_number_of_courses()
for _ in range(num_courses):
    course = school_system.input_one_course()
    school_system.courses.append(course)

for course in school_system.courses:
    school_system.select_course_and_input_student_marks(course)

# Accessing the data
for student in school_system.students:
    print(f"Student {student.name} marks:")
    for course_id, marks in student.marks.items():
        print(f"Course {course_id}: {marks}")