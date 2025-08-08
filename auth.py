from utils import load_admin_details, save_admin_info_details, load_student_details, save_student_info_details, load_credential_details, save_credential_details
import sys
def admin_signup():
    username = input("Choose the username:")
    password = input("Choose the password:")
    try:
        admin_details = load_admin_details()
        if username not in admin_details:
            admin_details[username] = password
            save_admin_info_details()
        else:
            return "username is already taken"
    except Exception:
        exc_type, exc_msg, exc_line = sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")
def admin_login():
    username = input("Enter your username:")
    password = input("Enter your password:")
    try:
        admin_details = load_admin_details()
        if username in admin_details:
            if admin_details[username] == password:
                return username
    except Exception:
        exc_type, exc_msg, exc_line = sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")

def student_signup():
    rollno = input("Enter your rollno:")
    student_details = load_student_details()
    if rollno in student_details:
        credential = load_credential_details()
        password = input("You can choose the password:")
        if rollno not in credential:
            credential[rollno] = password
            save_credential_details()
            return "Student Successfully SignedUp."
        else:
            return f"{rollno} already exist."
    else:
        return "No such Student Found."
