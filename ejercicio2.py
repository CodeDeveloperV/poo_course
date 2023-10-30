# HERENCIA SIMPLE
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Soy {self.name} y mi edad es {self.age}"


class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade

    def get_grade(self):
        return f"Mi grado es {self.grade}"


pedro = Student("Pedro", 25, 10)
print(pedro.get_info())
print(pedro.get_grade())


# HERENCIA MULTIPLE

class Animal:
    def eat(self):
        print("Estoy comiendo")


class Mammal(Animal):
    def suckle(self):
        print("Estoy amamantando")


class Bird(Animal):
    def fly(self):
        print("Estoy volando")


class Bat(Mammal, Bird):
    pass

batman = Bat()
batman.eat()
batman.fly()
batman.suckle()

print(Bat.mro())