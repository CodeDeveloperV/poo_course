class Person:
    def __init__(self, first_name: str, last_name: str, age: int, nationality: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality


class Employee(Person):
    def __init__(self, first_name: str, last_name: str, age: int, nationality: str, position: str, salary: float):
        super().__init__(first_name, last_name, age, nationality)
        self.salary = salary
        self.position = position


roberto = Employee("Roberto", "Gonzalez", 35, "Mexico", "Developer", 1000)

