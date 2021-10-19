import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Seguir creando nuevos caminos random, mientras el programa siga activo.
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Plotear los puntos en el camino.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #Resaltar el primer y ultimo punto.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remover los ejes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Crear un nuevo camino? (y/n): ")
    if keep_running == 'n':
        break
