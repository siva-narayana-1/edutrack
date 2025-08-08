import os
import sys, json

student_file = "students.json"
student = {}
admin_file = "admin.json"
admin = {}
credential_file = "credential.json"
credential = {}
def load_student_details():
    global student
    try:
        if os.path.exists(student_file):
            with open(student_file, "r") as f:
                student = json.load(f)
        else:
            student = {}
        return student
    except Exception:
        exc_type, exc_msg, exc_line= sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")

def save_student_info_details():
    try:
        with open(student_file, "w") as f:
            json.dump(student, f, indent=4)
    except Exception:
        exc_type, exc_msg, exc_line = sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")


def load_admin_details():
    global admin
    try:
        if os.path.exists(admin_file):
            with open(admin_file, "r") as f:
                admin = json.load(f)
        else:
            admin = {}
        return admin
    except Exception:
        exc_type, exc_msg, exc_line= sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")

def save_admin_info_details():
    try:
        with open(admin_file, "w") as f:
            json.dump(admin, f, indent=4)
    except Exception:
        exc_type, exc_msg, exc_line = sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")


def load_credential_details():
    global credential
    try:
        if os.path.exists(credential_file):
            with open(credential_file, "r") as f:
                credential = json.load(f)
        else:
            credential = {}
        return credential
    except Exception:
        exc_type, exc_msg, exc_line= sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")

def save_credential_details():
    try:
        with open(credential_file, "w") as f:
            json.dump(credential, f, indent=4)
    except Exception:
        exc_type, exc_msg, exc_line = sys.exc_info()
        print(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")