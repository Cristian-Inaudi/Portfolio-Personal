from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Crea un dado de 6 caras y otro de 10.
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analizar los resultados.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualizar los resultados.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Resultado', 'dtick': 1}
y_axis_config = {'title': 'Frecuencia de resultado'}
my_layout = Layout(title='Resultado de rodar un dado de 6 caras y otro de 10 caras, 50000 veces', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
