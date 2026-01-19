import matplotlib.pyplot as plt
from die import Die

die1 = Die()
die2 = Die()


results = [die1.roll_die() + die2.roll_die() for _ in range(1000)]

possible_results = range(2 , die1.num_sides + die2.num_sides + 1)
frequencies = [results.count(f) for f in possible_results]

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10,6))

bars = ax.bar(possible_results, frequencies, color='blue', edgecolor='black')

ax.set_title("Results of rolling of two D6 Dice", fontsize=24) 

ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of result", fontsize=14)

ax.set_xticks(possible_results)

ax.bar_label(bars)

plt.show()