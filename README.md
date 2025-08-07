# 🎓 Student Management CLI System

A modular Python-based command-line app to manage student and admin records using JSON files. Built for clarity, simplicity, and easy expansion — ideal for small school/college systems.

---

## 📂 Project Overview

### ✅ Core Features Implemented

- **Admin System**
  - Admin signup & login with credential storage in `admins.json`.

- **Student System**
  - Admin can add student details.
  - Students can sign up by setting a password if their roll number exists.
  - Password field supports optional setting during student creation.

- **Data Handling**
  - All data persisted using `students.json` and `admins.json`.
  - Robust exception handling using `sys.exc_info()` for line-level debugging.

---

## 🧩 Modules & Responsibilities

| File         | Purpose                                 |
|--------------|------------------------------------------|
| `main.py`    | CLI loop for login/signup               |
| `auth.py`    | Admin login/signup logic                |
| `student.py` | Functions like `add_student()` and `student_signup()` |
| `utils.py`   | Load/save helper functions for JSON     |
| `students.json` | Auto-generated storage for student data |
| `admins.json`   | Auto-generated storage for admin data   |

---

## 🧠 Function Reference

### 🔧 `add_student(name, age, branch, sem, rollno, password=None)`
> Adds a new student. Password is optional during creation.

Example structure (in JSON):

```json
"218H1A5433": {
  "name": "Siva Narayana",
  "age": 23,
  "branch": "CSE",
  "sem": "4-1",
  "rollno": "218H1A5433",
  "password": null
}
