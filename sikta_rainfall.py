import csv
from datetime import datetime 
import matplotlib.pyplot as plt
filename = 'sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates , rainfalls = [] , []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[5])
        dates.append(date)
        rainfalls.append(rainfall)

#Plotting the rainfalls
plt.style.use('classic')
fig , ax = plt.subplots()
ax.plot(dates , rainfalls , c='black')

#Format the plot
plt.title('Rainfalls in stika 2021', fontsize=24)
plt.xlabel('' , fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Rainfalls', fontsize=14)
plt.tick_params(axis='both' , which='major' , labelsize=16)


plt.show()