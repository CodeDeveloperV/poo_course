from abc import ABC, abstractmethod


class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def present_self(self):
        print("Hola, me llamo {} y tengo {} años".format(self.nombre, self.edad))


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando en el rubro de {self.actividad}")


dalto = Estudiante("Dalto", 25, "M", "programación")
dalto.present_self()
dalto.hacer_actividad()

pedro = Trabajador("Pedro", 36, "M", "programación")
pedro.present_self()
pedro.hacer_actividad()