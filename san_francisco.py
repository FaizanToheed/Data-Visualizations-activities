import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'san_francisco_2023.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates , highs , lows = [] , [] , []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {date}.")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
        
#Ploting the dates , highs and low temperature from the data
plt.style.use('classic')
fig , ax = plt.subplots()
ax.plot(dates , highs , c='red' , alpha=0.5)
ax.plot(dates , lows, c='blue', alpha=0.5)
ax.fill_between(dates , highs , lows , facecolor='grey' , alpha=0.5)

#Formating the plot
plt.title('Daily high and low temperatures', fontsize=24)
plt.xlabel('' , fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperatures(F)' , fontsize=14)
plt.tick_params(axis='both' , which='major' , labelsize=13)

#Set the limit for y axis
plt.ylim(0, 130)

plt.show()