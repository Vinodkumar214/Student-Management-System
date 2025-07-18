# Student Management System
student_records = {}

def add_student():
    name = input("Enter the student's name: ")
    roll_no = input("Enter the roll number: ")

    if roll_no in student_records:
        print("A student with this roll number already exists.")
        return

    student_records[roll_no] = {
        "name": name,
        "marks": [],
        "attendance": set()
    }
    print(f"Student '{name}' added successfully with roll number {roll_no}.")

def update_student_marks():
    roll_no = input("Enter roll number to update marks: ")

    if roll_no not in student_records:
        print("Student not found.")
        return

    try:
        marks_input = input("Enter marks separated by commas (e.g., 85,90,78): ")
        marks_list = [int(mark.strip()) for mark in marks_input.split(",")]
        student_records[roll_no]["marks"] = marks_list
        print("Marks updated successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

def record_attendance():
    roll_no = input("Enter roll number to mark attendance: ")

    if roll_no not in student_records:
        print("Student not found.")
        return

    date = input("Enter date (YYYY-MM-DD): ")
    student_records[roll_no]["attendance"].add(date)
    print(f"Attendance marked for {date}.")

def show_student_details():
    roll_no = input("Enter roll number to view details: ")

    if roll_no not in student_records:
        print("Student not found.")
        return

    student = student_records[roll_no]
    print("\n Student Details")
    print(f"Name       : {student['name']}")
    print(f"Roll No.   : {roll_no}")
    print(f"Marks      : {student['marks']}")
    print(f"Attendance : {sorted(student['attendance'])}")

    if student["marks"]:
        avg = sum(student["marks"]) / len(student["marks"])
        print(f"Average Marks: {avg:.2f}")

def remove_student():
    roll_no = input("Enter roll number to delete: ")

    if roll_no in student_records:
        del student_records[roll_no]
        print(f" Student with roll number {roll_no} has been removed.")
    else:
        print("Student not found.")

def run_system():
    while True:
        print("\n --- Student Management System ---")
        print("1. Add New Student")
        print("2. Update Marks")
        print("3. Mark Attendance")
        print("4. View Student Details")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student_marks()
        elif choice == "3":
            record_attendance()
        elif choice == "4":
            show_student_details()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            print(" Exiting the system. Have a great day!")
            break
        else:
            print(" Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run_system()
