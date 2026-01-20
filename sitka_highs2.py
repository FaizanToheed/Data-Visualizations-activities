import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    reader_row = next(reader)
    #Get the high temperaturs
    dates , highs = [] , []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        dates.append(date)
        highs.append(high)

#Ploting the dates and high temperatures
plt.style.use('classic')
fig , ax = plt.subplots()
ax.plot(dates , highs , c='red')

#Format plot
plt.title("Daily high temperatures" , fontsize=24)
plt.xlabel("" , fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)" , fontsize=14)
plt.tick_params(axis='both' , which='major' , labelsize=16)

plt.show()