import os
import bz2
import pickle
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = {}
        self.course_credits = {}
        self.lock = threading.Lock()

    def select_course_and_input_student_marks(self, course):
        messagebox.showinfo("Info", f"Enter marks for students in course {course.name}")
        # Add GUI interaction for entering marks

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_average_gpa(self.course_credits), reverse=True)

def load_data_from_file():
    if os.path.exists("students.dat"):
        with bz2.BZ2File("students.dat", "rb") as f:
            data = f.read()
            return pickle.loads(data)
    else:
        messagebox.showinfo("Info", "students.dat doesn't exist. Starting with empty data.")
        return [], {}, []

def save_data_to_file(data):
    with bz2.BZ2File("students.dat", "wb") as f:
        f.write(pickle.dumps(data))

def background_save_data(school_system):
    while True:
        # Acquire lock to prevent conflicts with main thread
        with school_system.lock:
            save_data_to_file((school_system.students, school_system.courses, []))
        # Sleep for some time before next save
        time.sleep(60)  # Adjust the time interval as needed

def on_exit():
    if messagebox.askyesno("Exit", "Do you want to exit the application?"):
        root.destroy()

if __name__ == "__main__":
    students, courses, marks = load_data_from_file()
    school_system = SchoolSystem()

    # Create the main window
    root = tk.Tk()
    root.title("School System")

    # Create command result text area
    command_result = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    command_result.pack(padx=5, pady=5)

    # Start background thread for saving data
    save_thread = threading.Thread(target=background_save_data, args=(school_system,))
    save_thread.daemon = True
    save_thread.start()
