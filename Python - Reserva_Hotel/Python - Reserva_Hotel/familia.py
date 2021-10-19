from validaciones import validar_ingreso_vacio
from validaciones import validar_numeros_enteros

class Familia():
    def __init__(self):
        self.apellido = []
        self.numero = []
        self.cantidad_mayores = []
        self.cantidad_menores = []

    def nueva_estadia_familia(self):
        print("Ingrese datos de familia: ")
        self.apellido.append(validar_ingreso_vacio("Ingresar apellido de la familia: "))
        self.numero.append(validar_numeros_enteros("Ingresar cantidad de personas de la familia: "))
        self.cantidad_mayores.append(validar_numeros_enteros("Ingresar cantidad de mayores en la familia: "))
        self.cantidad_menores.append(validar_numeros_enteros("Ingresar cantidad de menores en la familia: "))
        return self.apellido[-1],self.numero[-1]

