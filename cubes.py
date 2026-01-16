import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig , ax = plt.subplots()
ax.scatter(x_values , y_values , c=y_values, cmap=plt.cm.Greens, s=10)

ax.set_title("Cubic Growth", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic Value", fontsize=14)

ax.axis([0, 5100 , 0 , 125_000_000_000])
plt.show()