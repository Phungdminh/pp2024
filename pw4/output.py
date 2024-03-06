def display_students_gpa(students):
    for student in students:
        print(f"Student {student.name}: GPA - {student.calculate_average_gpa(course_credit)}")