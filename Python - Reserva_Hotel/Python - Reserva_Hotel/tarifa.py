from validaciones import validar_numeros_coma
from validaciones import validar_y_n

class Tarifa():
    def __init__(self):
        self.precio_noche = None
        self.precio_semana = None

    def cargar_tarifa(self):
        carga = True
        while carga:
            self.precio_noche =  validar_numeros_coma("Ingrese el precio por noche: $")
            self.precio_semana = validar_numeros_coma("Ingrese el precio por semana: $")

            nueva_carga = validar_y_n("Desea realizar otra carga y/n? ")
            if nueva_carga == "n":
                carga = False

