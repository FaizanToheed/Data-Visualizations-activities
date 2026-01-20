import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    reader_row = next(reader)
    #Get the date , low and high temperaturs
    dates , highs , lows = [] , [] , []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(date)
        highs.append(high)
        lows.append(low)

#Ploting the dates , low and high temperatures
plt.style.use('classic')
fig , ax = plt.subplots()
ax.plot(dates , highs , c='red' , alpha=0.5)
ax.plot(dates , lows , c='blue' , alpha=0.5)
ax.fill_between(dates , highs , lows , facecolor='grey' , alpha=0.5)

#Format plot
plt.title("Daily high and low temperatures" , fontsize=24)
plt.xlabel("" , fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)" , fontsize=14)
plt.tick_params(axis='both' , which='major' , labelsize=16)

plt.show()