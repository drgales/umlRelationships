class Printer {
    void print(String message) {
        System.out.println(message);
    }
}

class Report {
    void generate(Printer printer) {
        String content = "Monthly Report Generated.";
        printer.print(content);
    }
}

public class Main {
    public static void main(String[] args) {
        Printer printer = new Printer();
        Report report = new Report();

        report.generate(printer);
    }
}