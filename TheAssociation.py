class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name + " is teaching.")


class Student:
    def __init__(self, name):
        self.name = name

    def learn_from(self, teacher):
        print(self.name + " learns from " + teacher.name + ".")


def main():
    teacher = Teacher("Ms. Santos")
    student = Student("Maria")

    teacher.teach()
    student.learn_from(teacher)


if __name__ == "__main__":
    main()