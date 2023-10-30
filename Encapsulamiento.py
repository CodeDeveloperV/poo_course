class MyCLass:
    def __init__(self):
        self._atributo_privado = "Valor"
        self.__atributo_mas_privado = "Valor"

    def __private_method(self):
        print("Hola, como estas")

objeto = MyCLass()
print(objeto._atributo_privado)
print(objeto._atributo_mas_privado)
objeto.__private_method()