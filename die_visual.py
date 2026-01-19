from die import Die
from plotly.graph_objs import Bar , Layout
from plotly import offline

die = Die()

results = []
for roll_num in range(100):
    result = die.roll_die()
    results.append(result)
    

frequencies = []
for f in range(1, die.num_sides + 1):
    freq = results.count(f)
    frequencies.append(freq)
    
x_values = list(range(1 , die.num_sides + 1))
data = [Bar(x = x_values , y = frequencies)]

x_axis_config = {'title' : 'Result'}
y_axis_config = {'title' : 'Frequency of result'}

my_layout = Layout(title='Result of rolling one D6 over 100 times' , xaxis=x_axis_config , yaxis=y_axis_config)
offline.plot({'data' : data , 'layout' : my_layout}, filename='d6.html')