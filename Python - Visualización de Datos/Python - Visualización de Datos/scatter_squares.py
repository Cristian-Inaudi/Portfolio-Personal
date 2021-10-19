import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [pow(x,2) for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#Definir estilo de titulo y estiquetas de los ejes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Definir rango de cada eje.
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot2.png', bbox_inches='tight')
