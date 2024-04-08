import pandas as pd
import geocoder

dataset_1 = pd.read_csv('Dataset_1.csv')


dataset_1 = dataset_1.sample(n=10)
city = []
for index, row in dataset_1.iterrows():
   lat = row['latitude']
   lon = row['longitude']
   g = geocoder.google([lat, lon], method='reverse')
   city.append(g.city)

print(city)


# Possível resultado:
# [None, None, None, None, None, None, None, None, None, None]