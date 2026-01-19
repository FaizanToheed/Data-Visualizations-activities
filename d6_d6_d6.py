from die import Die
from plotly.graph_objs import Bar , Layout
from plotly import offline

die1 = Die()
die2 = Die()
die3 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll_die() + die2.roll_die() + die3.roll_die()
    results.append(result)
    
frequencies = []
for f in range(3 , die1.num_sides + die2.num_sides + die3.num_sides + 1):
    freq = results.count(f)
    frequencies.append(freq)

x_values = list(range(3 , die1.num_sides + die2.num_sides + die3.num_sides + 1))
data = [Bar(x=x_values , y=frequencies)]

x_axis_config = {'title' : 'Value' , 'dtick' : 1}
y_axis_config = {'title' : 'Frequencies of value'}

my_layout = Layout(title='Frequencies of rolling three D6 over 1000 times', xaxis=x_axis_config , yaxis=y_axis_config)
offline.plot({'data':data , 'layout':my_layout} , filename='d6_d6_d6.html')