from validaciones import validar_ingreso_vacio
from validaciones import validar_numeros_enteros

class Reserva():
    def __init__(self):
        self.numero_reserva = 0
        self.reservas = []

    def consultar_numero_reserva(self):
        numero = validar_numeros_enteros("Ingrese numero de reserva a consultar: ")
        self.consulta_particular(numero, 0, "numero")

    def consultar_apellido_reserva(self):
        apellido_ingresado = validar_ingreso_vacio("Ingrese apellido de reserva a consultar: ")
        self.consulta_particular(apellido_ingresado, 1, "apellido")

    def consulta_particular(self, ingreso, nro, palabra):
        variable = ingreso
        obtenido = False
        for i in self.reservas:
            if variable in self.reservas[nro]:
                print("La reserva se encontro satisfactoriamente. Los datos son: ", self.reservas[i])
                obtenido = True
        if obtenido is False:
            print(f"No se encontró el {palabra} de reserva requerido.")

    def consultar_reserva_semana(self):
        semana = validar_numeros_enteros("Ingrese numero de semana a consultar: ")
        conjunto = []
        obtenido = False
        for i in self.reservas:
            if semana in self.reservas[2]:
                conjunto.append(self.reservas[i])
                obtenido = True
        if obtenido is False:
            print("No se encontraron reservas en la semana requerida.")




