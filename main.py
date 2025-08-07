from auth import admin_login, admin_signup, student_signup
from admindashboard import admin_dashboard
from utils import load_student_details
def main():
    while True:
        choice = input("1.Login\n2.Signup\n")
        if choice == "1":
            admin_session = admin_login()
            # student_details = load_student_details()
            if admin_session:
                username = admin_session
                admin_dashboard(username)
                break
            else:
                print(f"\nadmin not found. recheck once.")
            # print(student_details["218H1A5433"][-1])
        elif choice == "2":
            admin_signup()
        else:
            break
if __name__ == "__main__":
    main()