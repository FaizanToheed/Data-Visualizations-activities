import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'death_valley_2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    try:
        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        name_index = header_row.index('NAME')
    except ValueError:
        print("Missing necessary columns in header!")
        exit() 

    dates, highs, lows = [], [], []
    station_name = ""

    for row in reader:
        if not station_name:
            station_name = row[name_index]

        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title(f"Daily high and low temperatures - 2021\n{station_name}", fontsize=20)

plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
# Optional: Keep the scale consistent if comparing
plt.ylim(0, 130) 

plt.show()