from habitacion import Habitacion
from familia import Familia
from semana import Semana
from tarifa import Tarifa
from reserva import Reserva

class Hotel():
    def __init__(self):
        self.habitacion = Habitacion()
        self.familia = Familia()
        self.semana = Semana()
        self.tarifa = Tarifa()
        self.reserva = Reserva()

    def inicio_programa(self):
        ejecucion = True
        while ejecucion:
            text = """Menu principal:
            1 - Cargar datos gerencia
            2 - Cargar reservas
            3 - Consultar reservas
            4 - Salir"""

            opcion = self.menu(text)
            if opcion == 1:
                self.cargar_datos()
            if opcion == 2:
                self.cargar_reservas()
            if opcion == 3:
                self.consultar_reserva()
            if opcion == 4:
                print("Hasta la proxima")
                break
            else:
                print("Ingrese opcion valida")

    def menu(self, texto):
        print(texto)
        opcion = int(input("Elija opcion a ingresar: " ))
        return opcion

    def cargar_datos(self):
        ejecucion = True
        while True:
            texto = """Menu de carga: 
            1 - Cargar Habitaciones
            2 - Cargar Semanas
            3 - Cargar Tarifas
            4 - Volver a Menu Principal"""
            opcion = self.menu(texto)

            if opcion == 1:
                self.habitacion.cargar_habitacion()
            if opcion == 2:
                self.semana.cargar_semana()
            if opcion == 3:
                self.tarifa.cargar_tarifa()
            if opcion == 4:
                break
            else:
                print("Ingrese opcion valida")

    def cargar_reservas(self):
        nueva_semana = self.semana.nueva_estadia_semana()
        if nueva_semana == 0:
            print("La semana no esta disponible, intente en otra fecha.")
            self.cargar_reservas()
        apellido, cantidad_familia = self.familia.nueva_estadia_familia()
        nueva_habitacion = self.habitacion.nueva_estadia_habitacion(cantidad_familia)
        if nueva_habitacion == 0:
            self.cargar_reservas()
        else:
            self.reserva.numero_reserva += 1
            nueva_reserva = [self.reserva.numero_reserva, apellido, nueva_semana, nueva_habitacion]
            print("Has registrado la siguiente reserva: ", nueva_reserva)
            self.reserva.reservas.append(nueva_reserva)

    def consultar_reserva(self):
        ejecucion = True
        while ejecucion:
            texto = """Menu de consultas:
            1 - Numero de Reserva
            2 - Apellido Familia
            3 - Reservas semana
            4 - Salir"""
            opcion = self.menu(texto)

            if opcion == 1:
                self.reserva.consultar_numero_reserva()
            if opcion == 2:
                self.reserva.consultar_apellido_reserva()
            if opcion == 3:
                self.reserva.consultar_reserva_semana()
            if opcion == 4:
                break
            else:
                print("Ingrese opcion valida")



if __name__ == '__main__':
    lg = Hotel()
    lg.inicio_programa()
