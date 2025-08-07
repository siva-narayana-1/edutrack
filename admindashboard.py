from student import add_student
def admin_dashboard(username):
    print(f"This is a admin dashboard!.")
    print(f"Welcome{username}")
    while True:
        choice = input("1.Add student\nempty space\n")
        print("We will add features soon")
        if choice == "1":
            studentname = input("Enter student name:")
            age = int(input("Enter the student age:"))
            branch = input("Enter the branch name of the student:")
            sem = input("Enter the semister of the student:")
            rollno = input("Enter student Rollnumber:")
            message = add_student(studentname, age, branch, sem, rollno)
            print(f"{message}")
        elif choice == " ":
            break