import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'sitka_weather_07-2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #Extracting the high temperatures and dates
    dates , highs  = [] , []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        dates.append(current_date)
        highs.append(high)

#Plot the high temperature and dates
plt.style.use('seaborn-v0_8')
fig , ax = plt.subplots()
ax.plot(dates , highs , c='red')

#Format plot
plt.title("Daily high temperatures" , fontsize=24)
plt.xlabel("" , fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature(F) ", fontsize=14)
plt.tick_params(axis = 'both' , which='major' , labelsize=16)

plt.show()