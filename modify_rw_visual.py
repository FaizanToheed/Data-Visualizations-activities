from modified_random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5000)
    
    rw.fill_walk()
    
    plt.style.use('classic')
    fig , ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values , rw.y_values , c=point_numbers , cmap=plt.cm.Blues , s=1)
    
    ax.scatter(0 , 0 , c='green' , edgecolors='None' , s=100)
    ax.scatter(rw.x_values[-1] , rw.y_values[-1] , c='red' , edgecolors='None' , s=100)
    
    #Set the axis invisible
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    keep_running = input("You want to generate it again(y/n) : ")
    if keep_running == 'n':
        break