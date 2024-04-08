import pandas as pd
from geopy.geocoders import Nominatim

dataset_1 = pd.read_csv('Dataset_1.csv')

# dataset_1 = dataset_1.sample(n=10)          #Se quiser testar com um dataset menor

arr = []
geoLoc = Nominatim(user_agent="GetLoc")
for index, row in dataset_1.iterrows():
   lat = row['latitude']
   lon = row['longitude']
   locname = geoLoc.reverse((lat, lon))
   arr.append(locname.address)
#print(arr)
cities = []
for address in arr:
    address_parts = address.split(',')
    city = address_parts[-5]
    cities.append(city.strip())
#print(cities)
dataset_1['city'] = cities


# Este código funciona mas apenas para uma quantidade menor de dados, pois a API do Nominatim tem um limite de requests por segundo

# Erro apresentado:
# raise GeocoderUnavailable(message)
# geopy.exc.GeocoderUnavailable: HTTPSConnectionPool(host='nominatim.openstreetmap.org', port=443): Max retries exceeded with url: /reverse?lat=47.654&lon=-122.337&format=json&addressdetails=1 (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000016B6C938770>, 'Connection to nominatim.openstreetmap.org timed out. (connect timeout=1)'))