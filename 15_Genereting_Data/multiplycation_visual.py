from die import Die
from  plotly.graph_objs import Bar, Layout
from  plotly import offline

#Create a D6.
die_1 = Die(6)
die_2 = Die(6)

#Make some rolls, and store results in a list
results = []
for roll in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#Analize the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of results'}
my_layout = Layout(title='Result of rolling a D6 and a D10 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_multiplication.html')


