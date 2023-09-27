# An empty dictionary to store student data.
student_data = {}


def add_student():
    student_name = input("Enter the name of the student: ")
    no_of_subjects = int(input("Enter the number of subjects: "))

    student_grades = {} # an empty dictionary to store subject-grade pairs for the student

    for i in range(no_of_subjects):
        subject = input(f"Enter subject {i + 1} name: ")
        grade = float(input(f"Enter {subject} grade: "))
        student_grades[subject] = grade  # Store subject-grade pair in the student_grades dictionary

    student_data[student_name] = student_grades  # Store the student's grades in the student_data dictionary
    print(f"{student_name} has been added with grades: {student_grades}")


def calculate_average(student_name):
    # Retrieve the subject-grade dictionary for the given student name
    student_grades = student_data.get(student_name)

    # Calculate the total of all grades and the number of subjects
    if student_grades:
        total = sum(student_grades.values())
        num_subjects = len(student_grades)
        average = total / num_subjects

        return average
    else:
        return None


# Function to display a student's grades and average.

def display_student_info():
    student_name = input("Enter student name to display info: ")
    student_grades = student_data.get(student_name)
    if student_grades:
        print(f"Grades for {student_name}:")
        for subject, grade in student_grades.items():
            print(f"{subject}: {grade}")

        average = calculate_average(student_name)
        print(f"Average grade: {average}")

    else:
        print(f"{student_name} not found!!")


while True:
    print("Press 1 for add student\nPress 2 for display student info\nPress 3 for exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        display_student_info()
    elif choice == 3:
        print("Exiting the Program")
        break
    else:
        print("Invalid Choice!!")
