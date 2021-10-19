from validaciones import validar_ingreso_vacio
from validaciones import validar_numeros_enteros
from validaciones import validar_y_n

class Habitacion():
    def __init__(self):
         self.nombre = []
         self.capacidad = []
         self.camas_matrimoniales = []
         self.camas_simples = []
         self.cocina = []
         self.cantidad_banos = []

    def cargar_habitacion(self):
        carga = True
        while carga:
             self.nombre.append(validar_ingreso_vacio("Ingrese nombre habitacion: "))
             self.capacidad.append(validar_numeros_enteros("Ingrese capacidad de habitacion: "))
             self.camas_matrimoniales.append(validar_numeros_enteros("Ingrese cantidad de camas matrimoniales: "))
             self.camas_simples.append(validar_numeros_enteros("Ingrese cantidad de camas individuales: "))
             self.cantidad_banos.append(validar_numeros_enteros("Ingrese cantidad de baños: "))
             cocina = validar_y_n("Posee cocina? y/n ")
             if cocina == "y":
                 self.cocina.append(True)
             else:
                 self.cocina.append(False)

             print(self.capacidad[-1])
             nueva_carga = validar_y_n("Desea realizar otra carga y/n? ")
             if nueva_carga == "n":
                 carga = False

    def nueva_estadia_habitacion(self,cantidad_familia):
        print("Habitacion a asignar: ")
        print("Cantidad familia: " ,cantidad_familia)
        print("Habitaciones disponibles acorde a la capacidad: ")
        alternativas = []
        for i in range (len(self.capacidad)):
            if self.capacidad[i] >= cantidad_familia:
                alternativas.append(self.nombre[i])
        print(alternativas)

        if len(alternativas) > 0:
            bucle = True
            eleccion = ""
            while bucle:
                eleccion = validar_ingreso_vacio("Ingrese nombre de alternativa seleccionada (presione '-1' si desea cancelar y retornar a menu anterior): ")
                if eleccion in alternativas:
                    break
                else:
                    if eleccion in self.nombre:
                        print("Alternativa no disponible")
                    if eleccion == -1:
                        eleccion = 0
                    else:
                        print("Nombre invalido")
            return eleccion
        else:
            print("No hay alternativa de habitacion disponible para el grupo familiar ingresado.")
            eleccion = 0
            return eleccion


