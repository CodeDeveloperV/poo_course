import pyautogui

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __repr__(self):
        return f"Persona({self.nombre},{self.edad})"

    def __add__(self, other):
        new_value = self.edad + other.edad
        return new_value


alex = Persona("Alex", 22)
pedro = Persona("Pedro", 26)

print()
print(alex + pedro)