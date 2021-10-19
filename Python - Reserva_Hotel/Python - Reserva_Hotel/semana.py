from validaciones import validar_numeros_enteros
from validaciones import validar_y_n

class Semana():
    def __init__(self):
        self.numero_semana = []
        self.cantidad_dias_semana = []
        self.dias_calendario = []

    def cargar_semana(self):
        carga = True
        while carga:
            self.numero_semana.append(validar_numeros_enteros("Ingrese numero de semana: "))
            self.cantidad_dias_semana.append(validar_numeros_enteros("Ingrese cantidad dias de la semana: "))
            dia_semana = []
            for dia in range(self.cantidad_dias_semana[-1]):
                dia_semana.append(validar_numeros_enteros("Ingrese dias (numero) calendario de semana: "))
            self.dias_calendario.append(dia_semana)

            nueva_carga = validar_y_n("Desea realizar otra carga y/n? ")
            if nueva_carga == "n":
                carga = False

    def nueva_estadia_semana(self):
        nuevo_numero_semana = validar_numeros_enteros("Ingrese numero de semana a reservar: ")
        if len(self.numero_semana) == 0:
            print("No hay datos cargados sobre semanas disponibles")
            nuevo_numero_semana = 0
            return nuevo_numero_semana
        else:
            for i in range(len(self.numero_semana)):
                if nuevo_numero_semana == self.numero_semana[i]:
                    return nuevo_numero_semana
                else:
                    print("Ingrese numero de semana valido.")
                    self.nueva_estadia_semana()
