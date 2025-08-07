from utils import load_student_details, save_student_info_details

def add_student(studentname, age, branch, sem, rollno):
    student_details = load_student_details()
    if rollno not in student_details:
        student_details[rollno] = [studentname,age,branch,sem,]
        save_student_info_details()
        return "Students added successfully"
    else:
        return "Rollno already exist."