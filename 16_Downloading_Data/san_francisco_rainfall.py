import csv
import matplotlib.pyplot as plt
from datetime import datetime

#filename = 'data/san_francisco_2022_rainfall.csv'
#filename = 'data/las_vegas.csv'
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, header in enumerate(header_row):
        if header == 'NAME':
            index_name = index
        elif header == 'DATE':
            index_date = index
        elif header == 'PRCP':
            index_prcp = index
    
    #Get name of the station
    first_line = next(reader)
    full_name_station = (first_line[index_name]).split(',')
    station = full_name_station[0]
    
    #Get high temperatures from this file
    dates, rainfalls = [], []
    
    for row in reader:
        current_date = datetime.strptime(row[index_date], '%Y-%m-%d')
        try:
            rainfall = float(row[index_prcp])
        except ValueError:
            print(f"Missing info {current_date}")
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)
    
    #Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rainfalls, c='red')
    
    #Format plot.
    ax.set_title(f"Daily Rainfall {station} - 2022", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("PRCP", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
    
    