class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    #Getter
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

alex = Persona("Lucas", 21)
nombre = alex.get_nombre()
print(nombre)

alex.set_nombre("Ramiro")
nombre = alex.get_nombre()
print(nombre)
