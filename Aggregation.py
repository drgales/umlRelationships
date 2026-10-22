class Student {
    String name;

    Student(String name) {
        this.name = name;
    }
}

class Department {
    private final Student student;

    Department(Student student) {
        this.student = student;
    }

    void showStudent() {
        System.out.println(
            "Department has student: " + student.name
        );
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student("Alex");

        Department department = new Department(student);
        department.showStudent();

        // Student still exists independently.
        System.out.println("Student: " + student.name);
    }
}