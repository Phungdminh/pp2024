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