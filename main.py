class Student:
    def __init__(self, roll, name, subjects):
        self.roll = roll
        self.name = name
        self.subjects = subjects
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        total = sum(self.grades.values())
        return total / len(self.grades)

class StudentRecordSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, roll, name, subjects):
        self.students[roll] = Student(roll, name, subjects)

    def get_student(self, roll):
        return self.students.get(roll)

    def add_grade(self, roll, subject, grade):
        student = self.get_student(roll)
        if student:
            student.add_grade(subject, grade)
        else:
            print("Student not found!")

if __name__ == "__main__":
    record_system = StudentRecordSystem()

    while True:
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Get Student Info")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            roll = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            subjects = input("Enter Subjects (comma-separated): ").split(", ")
            record_system.add_student(roll, name, subjects)
            print("Student added successfully!")

        elif choice == 2:
            roll = int(input("Enter Roll Number: "))
            subject = input("Enter Subject: ")
            grade = float(input("Enter Grade: "))
            record_system.add_grade(roll, subject, grade)
            print("Grade added successfully!")

        elif choice == 3:
            roll = int(input("Enter Roll Number: "))
            student = record_system.get_student(roll)
            if student:
                print(f"Name: {student.name}")
                print("Subjects:", ", ".join(student.subjects))
                print("Grades:", student.grades)
                print("Average Grade:", student.get_average_grade())
            else:
                print("Student not found!")

        elif choice == 4:
            break

        else:
            print("Invalid choice. Please try again.")
