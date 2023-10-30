from time import sleep
from typing import List, Dict, Union
import pyautogui


class Personaje:
    def __init__(self, nombre: str, fuerza: int, agilidad: int):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Agilidad: {self.agilidad})"

    def __add__(self, other):
        nuevo_nombre = f"{self.nombre}-{other.nombre}"
        nueva_fuerza = round(((self.fuerza + other.fuerza) / 2) ** 1.5)
        nueva_agilidad = round(((self.agilidad + other.agilidad) / 2) ** 1.5)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_agilidad)


class Game:
    def __init__(self):
        self.__characters: List[Personaje] = []
        self.__options: Dict[str, Dict[str, str]] = {
            "1": {"option": "Crear personaje"},
            "2": {"option": "Fusionar personajes"},
            "3": {"option": "Mostrar personajes"},
            "4": {"option": "Salir"}
        }

    def start_game(self) -> None:
        print("El juego ha comenzado...\n")
        clear_console()
        self.__main_menu()

    def __main_menu(self) -> None:
        while True:
            for key, value in enumerate(self.__options):
                print(f"{value}: {self.__options[value]['option']}")
            option = input("Selecciona una opcion: ")

            if self.__is_valid_option(option):
                clear_console()
                if option == "1":
                    character = self.__create_character()
                    if character is not None:
                        self.__characters.append(character)
                elif option == "2":
                    clear_console()
                    self.__fusion_characters()
                elif option == "3":
                    clear_console()
                    self.__show_characters()
                else:
                    clear_console()
                    print("El juego ha terminado")
                    break
            else:
                clear_console()
                print("Opción inválida, intenta nuevamente")

    def __is_valid_option(self, option: str) -> bool:
        return option in self.__options

    def __create_character(self) -> Union[Personaje, None]:
        print("Vamos a crear un personaje")
        nombre = input("Ingrese el nombre del personaje: ")
        fuerza = int(input("Ingrese la fuerza del personaje: "))
        agilidad = int(input("Ingrese la agilidad del personaje: "))
        personaje = Personaje(nombre, fuerza, agilidad)
        if self.__check_existing_character(personaje):
            print(f"¡Personaje {personaje} ya existe!\n")
            return None
        else:
            print(f"¡{personaje} creado con éxito!\n")
            return personaje

    def __show_characters(self) -> None:
        if not self.__characters:
            print("Aun no hay personajes\n")
        else:
            print("Personajes disponibles:")
            for i, character in enumerate(self.__characters):
                print(f"{i + 1}: {character}")
            print("\n")

    def __fusion_characters(self):
        if len(self.__characters) < 2:
            print("Necesita al menos 2 personajes para fusionar\n")
        else:
            self.__show_characters()
            option_1 = input("Ingresa el numero del personaje 1: ")
            option_2 = input("Ingresa el numero del personaje 2: ")

            if self.__is_valid_character(option_1) and self.__is_valid_character(option_2):
                personaje_1 = self.__select_character(option_1)
                personaje_2 = self.__select_character(option_2)

                if not(personaje_1.nombre == personaje_2.nombre):
                    personaje_fusionado = personaje_1 + personaje_2

                    if not self.__check_existing_character(personaje_fusionado):
                        self.__characters.append(personaje_fusionado)
                        print(f"¡Fusión exitosa! El nuevo personaje es: {personaje_fusionado}\n")
                    else:
                        print(f"¡La fusión de este personaje ya existe!\n")
                else:
                    print("Seleccion inválida. Asegúrese de elegir personajes validos\n")
            else:
                print("Seleccion inválida. Asegúrese de elegir personajes validos\n")

    def __is_valid_character(self, param: str) -> bool:
        return param.isdigit() and len(self.__characters) >= int(param) > 0

    def __check_existing_character(self, character: Personaje) -> bool:
        return any(
            i.nombre == character.nombre and i.fuerza + i.agilidad == character.fuerza + character.agilidad for i in
            self.__characters)

    def __select_character(self, param):
        return self.__characters[int(param) - 1]


def clear_console():
    sleep(1)
    pyautogui.click(x=1024, y=920)


game = Game()
game.start_game()
