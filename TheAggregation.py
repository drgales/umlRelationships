class Student:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, student):
        self.student = student

    def show_student(self):
        print("Department has student:", self.student.name)


def main():
    student = Student("Alex")

    department = Department(student)
    department.show_student()

    # Student still exists independently.
    print("Student:", student.name)


if __name__ == "__main__":
    main()