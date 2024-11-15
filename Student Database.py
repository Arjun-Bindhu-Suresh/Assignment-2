# Student Name: Arjun Bindhu Suresh
# Student ID: 100990351
# Date: 2024-11-15

import json
import os
from datetime import datetime

# File to store student data
STUDENT_DATA_FILE = "students_data.json"

# Load existing students data from the file
def load_students():
    if os.path.exists(STUDENT_DATA_FILE):
        with open(STUDENT_DATA_FILE, 'r') as file:
            return json.load(file)
    return []  # If file does not exist, return an empty list

# Save students data to the file
def save_students(students):
    with open(STUDENT_DATA_FILE, 'w') as file:
        json.dump(students, file, indent=4)

# Function to add a new student
def add_student(students):
    # Taking input from the user
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Student's Name: ")
    marks = input("Enter Marks: ")

    # Get today's date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Creating a dictionary
    student = {'Roll Number': roll_number, 'Name': name, 'Marks': marks, 'Date Added': current_date}

    # Adding data
    students.append(student)

    # Save data
    save_students(students)

    print(f"Student {name} with Roll Number {roll_number} has been added successfully!")

# Function to view all students
def view_all_students(students):
    if not students:
        print("No students found.")
    else:
        print("\nAll Students:")
        for student in students:
            print(f"Roll Number: {student['Roll Number']}, Name: {student['Name']}, Marks: {student['Marks']}, Date Added: {student['Date Added']}")

# Function to search for a student by roll number
def search_student_by_roll_number(students):
    roll_number = input("Enter Roll Number to search: ")

    # Searching for the student by roll number
    for student in students:
        if student['Roll Number'] == roll_number:
            print(f"Student Found: Roll Number: {student['Roll Number']}, Name: {student['Name']}, Marks: {student['Marks']}, Date Added: {student['Date Added']}")
            return
    
    print("Student not found.")

# Main function 
def main():
    students = load_students()  # Load existing students when the program starts
    
    while True:
        print("\nStudent Database System")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Exit")
        
        # Taking user choice 
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            search_student_by_roll_number(students)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
