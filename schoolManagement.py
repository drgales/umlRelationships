class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}"
    
class Student(Person): 
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


    def teach(self):
        print(f"{self.name} is teaching.")

person1 = Person("John Doe", 30)
print(person1.get_details())
student1 = Student("Alice", 22, "S123")
student1.study()
teacher1 = Teacher("Mr. Smith", 40)
print(teacher1.get_details())
teacher1.teach()