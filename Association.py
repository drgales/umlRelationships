class Teacher {
    String name;

    Teacher(String name) {
        this.name = name;
    }

    void teach() {
        System.out.println(name + " is teaching.");
    }
}

class Student {
    String name;

    Student(String name) {
        this.name = name;
    }

    void learnFrom(Teacher teacher) {
        System.out.println(
            name + " learns from " + teacher.name + "."
        );
    }
}

public class Main {
    public static void main(String[] args) {
        Teacher teacher = new Teacher("Ms. Santos");
        Student student = new Student("Maria");

        teacher.teach();
        student.learnFrom(teacher);
    }
}