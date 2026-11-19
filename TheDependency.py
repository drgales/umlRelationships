class Printer:
    def print_message(self, message):
        print(message)


class Report:
    def generate(self, printer):
        content = "Monthly Report Generated."
        printer.print_message(content)


def main():
    printer = Printer()
    report = Report()

    report.generate(printer)


if __name__ == "__main__":
    main()