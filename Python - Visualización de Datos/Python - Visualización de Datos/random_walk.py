from random import choice

class RandomWalk:
    """Una clase para generar caminos random."""

    def __init__(self, num_points=5000):
        """Inicializar los atributos para un camino."""
        self.num_points = num_points

        #Todos los caminos comienzan en (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcular todos los puntos en el camino."""

        #Seguir tomando caminos hasta que se alcance la cantidad establecida.
        while len(self.x_values) < self.num_points:

            #Decidir cual direccion tomar y cuan lejos ir hacia esa direccion.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Ignorar movimientos nulos.
            if x_step == 0 and y_step == 0:
                continue

            #Calcular la nueva posicion.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
