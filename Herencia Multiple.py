## Herencia multiple
class Person:
    def __init__(self, first_name: str, last_name: str, age: int, nationality: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality


class Artist:
    def __init__(self, ability: str):
        self.ability = ability

    def show_ability(self):
        return f"Mi habilidad es {self.ability}"


class EmployeeArtist(Person, Artist):
    def __init__(self, first_name, last_name, age, nationality, ability, salary, position):
        Person.__init__(self, first_name, last_name, age, nationality)
        Artist.__init__(self, ability)
        self.salary = salary
        self.position = position

    def present_self(self):
        # super().show_ability() es valido ya que le decimos al metodo present_self que hereda de Artist
        # por ende que tiene el metodo show_ability
        # En cambio self.show_ability() no es valido ya que self no tiene el metodo show_ability
        # pero como el metodo show_ability es heredado de Artist, podemos usarlo
        return f"Hola soy {self.first_name} {self.last_name} soy de {self.nationality}, soy {self.position} y " \
               f"{self.show_ability()}"


robert = EmployeeArtist("Robert", "Gonzalez", 35, "Mexico", "cantar", 1000, "Developer")
print(robert.present_self())

# como saber si la clase es una subclase de otra clase
print(issubclass(EmployeeArtist, Person))
print(issubclass(Artist, Person))

#Para saber si una clase es na instancia de otra clase
print(isinstance(robert, EmployeeArtist))
print(isinstance(robert, Artist))
print(isinstance(robert, Person))