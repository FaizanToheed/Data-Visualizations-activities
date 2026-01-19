from die import Die
from plotly.graph_objs import Bar , Layout
from plotly import offline

die1 = Die(8)
die2 = Die(8)

results = [die1.roll_die() + die2.roll_die() for _ in range(1000)]

frequencies = [results.count(f) for f in range(2 , die1.num_sides + die2.num_sides + 1 )]

x_values = list(range(2 , die1.num_sides + die2.num_sides + 1))
data = [Bar(x=x_values , y=frequencies)]

x_axis_config = {'title' : 'Value' , 'dtick' : 1}
y_axis_config = {'title' : 'Frequencies of value'}

my_layout = Layout(title='Frequencies of rolling two D8 over 1000 times', xaxis=x_axis_config , yaxis=y_axis_config)
offline.plot({'data':data , 'layout':my_layout} , filename='d8_d8.html')