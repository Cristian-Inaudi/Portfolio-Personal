def validar_numeros_enteros(texto):
    valido = False
    while (valido == False):
        ingreso = input(texto)
        try:
            posible_ingreso_numero =int(ingreso)
            return posible_ingreso_numero
        except ValueError:
            print("Ingrese caracteres numéricos enteros.")

def validar_numeros_coma(texto):
    valido = False
    while (valido == False):
        ingreso = input(texto)
        try:
            posible_ingreso_numero =float(ingreso)
            return posible_ingreso_numero
        except ValueError:
            print("Ingrese caracteres numéricos.")

def validar_ingreso_vacio(texto):
    valido = False
    while (valido == False):
        ingreso = input(texto)
        if len(ingreso) == 0:
            print("Ingrese algún nombre.")
        else:
            return ingreso

def validar_y_n(texto):
    valido = False
    while (valido == False):
        ingreso = input(texto)
        if ingreso == "y" or ingreso == "n":
            return ingreso
        else:
            print("Ingrese letra válida (y/n).")
