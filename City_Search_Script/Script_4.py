import pandas as pd
import geocoder
import geopy.distance

dataset_1 = pd.read_csv('Dataset_1.csv')

dataset_1 = dataset_1.sample(n=10)
dataset_1 = dataset_1.assign(city=None)
arr = []
for index, row in dataset_1.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    g = geocoder.osm([lat, lon], method='reverse')
    if g is not None and g.city is not None:
        arr.append(g.city)
    else:
        nearest_city = None
        min_distance = float('inf')
        for index2, row2 in dataset_1.iterrows():
            lat2 = row2['latitude']
            lon2 = row2['longitude']
            if lat != lat2 and lon != lon2:
                coords_1 = (lat, lon)
                coords_2 = (lat2, lon2)
                distance = geopy.distance.geodesic(coords_1, coords_2).kilometers
                if distance < min_distance:
                    if row2['city'] != None:
                        min_distance = distance
                        nearest_city = row2['city']
        arr.append(nearest_city)
print(arr)


# Possível resultado:
# [None, 'Bellevue', None, 'Bellevue', 'Seattle', None, 'Seattle', None, None, None]