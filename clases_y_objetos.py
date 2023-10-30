class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def get_info(self):
        print(f"{self.marca} - {self.modelo}")

    def call(self):
        print("Estas haciendo una llamada")

    def cutoff(self):
        print("Cortaste la llamada")


celular1 = Celular("Samsung", "Galaxy S21", "48MP")
celular2 = Celular("Apple", "iPhone 13", "12MP")
celular3 = Celular("Huawei", "P40", "12MP")


print(celular1.call())



