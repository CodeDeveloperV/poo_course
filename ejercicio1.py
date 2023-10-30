class Student:
    def __init__(self, name: str, age: int, level: str):
        self.name = name
        self.age = age
        self.level = level

    def study(self):
        print(f"El estudiante {self.name} está estudiando")

    def get_info(self):
        print(f"""
            DATOS DE ESTUDIANTE: \n\n
            Nombre: {self.name} \n
            Edad: {self.age} \n
            Nivel: {self.level} \n
        """)


def create_student():
    name = input("Ingresa tu nombre: ")
    age = int(input("Ingresa tu edad: "))
    level = input("Ingresa tu nivel: ")
    return Student(name, age, level)


student1: Student = create_student()
student1.get_info()

while True:
    activity: str = input().lower()
    if activity == "estudiar":
        print(f"El estudiante {student1.name} está estudiando")
