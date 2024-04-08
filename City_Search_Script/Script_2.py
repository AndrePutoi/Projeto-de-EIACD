import pandas as pd
import geocoder

dataset_1 = pd.read_csv('Dataset_1.csv')


arr = []
dataset_1 = dataset_1.sample(n=25)
for index, row in dataset_1.iterrows():
  lat = row['latitude']
  lon = row['longitude']
  g = geocoder.osm([lat, lon], method='reverse')
  arr.append(g.city)
print(arr)


# Possível resultado:
# ['Seattle', None, None, None, 'Seattle', 'Seattle', None, None, None, None, 'Seattle', 'Seattle', None, None, 'Seattle', None, None, 'Seattle', 'Seattle', 'Seattle', None, None, None, 'Seattle', None]