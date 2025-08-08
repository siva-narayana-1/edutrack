from student import add_student,load_student_details
def admin_dashboard(username):
    print(f"This is a admin dashboard!.")
    print(f"Welcome{username}")
    while True:
        choice = input("1.Add student\n2.View Student\nempty space\n")
        print("We will add new features soon")
        if choice == "1":
            studentname = input("Enter student name:")
            age = int(input("Enter the student age:"))
            branch = input("Enter the branch name of the student:")
            sem = input("Enter the semister of the student:")
            rollno = input("Enter student Rollnumber:")
            message = add_student(studentname, age, branch, sem, rollno)
            print(f"{message}")
        elif choice == "2":
            branch = input("Enter a branch name:").upper()
            student_details = load_student_details()
            counts = {}
            for i in student_details:
                if student_details[i][2] == branch:
                    print(f"{i} {student_details[i][0]} {student_details[i][2]}")
                    if student_details[i][2] in counts:
                        counts[student_details[i][2]] +=1
                    else:
                        counts[student_details[i][2]] = 1
                elif branch == "ALL":
                    print(f"{i} {student_details[i][0]} {student_details[i][2]}")
                    if student_details[i][2] in counts:
                        counts[student_details[i][2]] +=1
                    else:
                        counts[student_details[i][2]] = 1
            for j in counts:
                print(f"{j}  {counts[j]}")
            print(f"Total Students:{len(student_details)}")
        elif choice == " ":
            break