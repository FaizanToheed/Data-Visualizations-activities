from randomwalk import RandomWalk
import matplotlib.pyplot as plt
while True:
    rw = RandomWalk(500)
    
    rw.fill_walk()

    plt.style.use('classic')
    fig , ax = plt.subplots(figsize=(10,6) , dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values , rw.y_values , linewidth=3)
    
    #Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='None', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='None', s=100)

    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break