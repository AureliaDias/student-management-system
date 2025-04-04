
import numpy as np

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average(self):
        return np.mean(self.grades)

    def to_string(self):
        return f"{self.name},{self.age},{'|'.join(map(str, self.grades))}"

    @staticmethod
    def from_string(data):
        name, age, grades = data.strip().split(',')
        grades = list(map(int, grades.split('|')))
        return Student(name, int(age), grades)


def save_student(student, filename='students.txt'):
    try:
        with open(filename, 'a') as file:
            file.write(student.to_string() + '\n')
    except Exception as e:
        print("Error saving student:", e)


def load_students(filename='students.txt'):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                students.append(Student.from_string(line))
    except FileNotFoundError:
        pass
    return students


def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for student in students:
        print(f"Name: {student.name}, Age: {student.age}, Average Grade: {student.calculate_average():.2f}")


def search_student(name):
    students = load_students()
    found = False
    for student in students:
        if student.name.lower() == name.lower():
            print(f"\nFound: Name: {student.name}, Age: {student.age}, Grades: {student.grades}, "
                  f"Average: {student.calculate_average():.2f}")
            found = True
    if not found:
        print("Student not found.")


def add_student():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        if age < 0:
            raise ValueError("Age cannot be negative!")

        grades_input = input("Enter grades (comma separated): ")
        grades = list(map(int, grades_input.split(',')))

        student = Student(name, age, grades)
        save_student(student)
        print("Student added successfully!")

    except ValueError as ve:
        print("Invalid input:", ve)


# ---- Main Program ----
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            name = input("Enter the name to search: ")
            search_student(name)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
