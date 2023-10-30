class A:
    def talk(self):
        print("Hola desde A")


class B(A):
    def talk(self):
        print("Hola desde B")


class C(A):
    def talk(self):
        print("Hola desde C")


class D(C):
    def talk(self):
        print("Hola desde D")


d = D()
d.talk()

#Check MRO
print(D.mro())

#Llamar metodo de una clase padre a través de una clase hija
A.talk(d)

