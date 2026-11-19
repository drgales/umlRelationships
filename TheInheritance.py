class Animal:
    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Dog is barking.")


def main():
    dog = Dog()

    dog.eat()   # Inherited from Animal
    dog.bark()  # Defined in Dog


if __name__ == "__main__":
    main()