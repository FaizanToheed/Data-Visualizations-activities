from die import Die
from plotly.graph_objs import Bar , Layout
from plotly import offline

die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(50000):
    result = die1.roll_die() + die2.roll_die()
    results.append(result)
    
frequencies = []
for f in range(2 , die1.num_sides + die2.num_sides + 1):
    freq = results.count(f)
    frequencies.append(freq)
    
x_values = list(range(2 , die1.num_sides + die2.num_sides + 1))
data = [Bar(x=x_values , y=frequencies)]

x_axis_config = {'title' : 'Result' , 'dtick' : 1}
y_axis_config = {'title' : 'Frequency of result'}

my_layout = Layout(title = 'Result of rolling D6 and D10 over 50000 times' , xaxis = x_axis_config
                   , yaxis = y_axis_config)
offline.plot({'data' : data , 'layout' : my_layout} , filename='d6_d10.html')