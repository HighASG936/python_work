import csv
import matplotlib.pyplot as plt
from datetime import datetime

|filename = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get high temperatures from this file
    dates, rainfalls = [], []
    for row in reader:
        current_day = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])       
        dates.append(current_day)
        rainfalls.append(rainfall)
    
    #Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rainfalls, c='red')
    
    #Format plot.
    ax.set_title("Daily Rainfall - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("PRCP", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
    
    