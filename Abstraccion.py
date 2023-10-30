class Auto:
    def __init__(self):
        self.estado = "apagado"

    def enceder(self):
        self.estado = "encendido"
        print("El auto se encendió")

    def conducir(self):
        if self.estado == "apagado":
            self.enceder()
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()