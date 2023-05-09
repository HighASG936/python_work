import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    #Get lat, lon and bright indexes
    for index, header in enumerate(header_row):
        if header == 'latitude':
            index_lat = index
        elif header == 'longitude':
            index_lon = index
        elif header == 'brightness':
            index_bright = index
    
    #Fill data info
    lats, lons, brights = [], [], []
    for row in reader:
        try:
            lats.append(float(row[index_lat]))
            lons.append(float(row[index_lon]))
            brights.append(float(row[index_bright]))
        except ValueError:
            print('Missing info')
            continue         

#Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    #'text': hover_texts,
    'marker':{
        'size': [0.032*bright for bright in brights],        
        'color': brights,
        'colorscale': 'Hot',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
        },
    }]
my_layout = Layout(title='Global Fires in 1 Day')
    
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_Fires.html')

