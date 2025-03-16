#!/usr/bin/env python3
# Author ID: tgupta25

class Student:

    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure number is stored as a string
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average (GPA)
    def displayGPA(self):
        if len(self.courses) == 0 or sum(self.courses.values()) == 0:  # Avoid ZeroDivisionError
            return f"GPA of student {self.name} is 0.0"

        gpa = sum(self.courses.values()) / len(self.courses)
        return f"GPA of student {self.name} is {gpa:.1f}"

    # Return a list of courses that the student passed (grades > 0.0)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses  # Matches expected list output

if __name__ == '__main__':
    # Create first student object and add grades
    student1 = Student('John', '013454900')  # Fixed student number format
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)  # Failed course

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())  # Matches expected format
    print()

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())  # Matches expected format
