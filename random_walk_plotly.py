from randomwalk import RandomWalk
from plotly.graph_objs import Scatter, Layout
from plotly import offline

# 1. Generate the data
rw = RandomWalk(5000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))

# 2. Define the data trace (Using Scatter from graph_objs)
# We define the marker style (size, color, colorscale) inside a dictionary
data = [Scatter(
    x=rw.x_values,
    y=rw.y_values,
    mode='markers',
    marker=dict(
        size=3,
        color=point_numbers,      # Color varies by step number
        colorscale='Blues',       # The color map
        showscale=True            # Show the sidebar legend
    )
)]

# 3. Define the layout (Hide axes)
my_layout = Layout(
    title='Random Walk with Plotly',
    xaxis=dict(visible=False),
    yaxis=dict(visible=False)
)

# 4. Plot to HTML
offline.plot({'data': data, 'layout': my_layout}, filename='rw_plotly.html')