import pandas as pd
from geopy.geocoders import Nominatim   #ou Photon

dataset_1 = pd.read_csv('Dataset_1.csv')

dataset_1 = dataset_1.assign(city=None)
dataset_1 = dataset_1.sample(n=10)
def get_city(lat, lon):
   geolocator = Nominatim(user_agent="geoapiExercises")   #ou Photon(user_agent="geoapiExercises")
   location = geolocator.reverse((lat, lon))
   return location.raw['address']

data = {'latitude': dataset_1['latitude'], 'longitude': dataset_1['longitude']}
df = pd.DataFrame(data)
df['city'] = df.apply(lambda x: get_city(x['latitude'], x['longitude']), axis=1)
dataset_1['city'] = df['city']

print(dataset_1['city'])


# Possível resultado:
# 3146     {'house_number': '1416', 'road': '19th Avenue'...
# 1633     {'house_number': '10417', 'road': 'Northeast 1...
# 7529     {'house_number': '1628', 'road': '9th Avenue W...
# 711      {'house_number': '27220', 'road': '42nd Place ...
# 14442    {'house_number': '2610', 'road': '43rd Avenue ...
# 13286    {'house_number': '26719', 'road': 'Southeast 2...
# 10892    {'house_number': '14918', 'road': '27th Place ...
# 15714    {'house_number': '10838', 'road': 'Southeast 3...
# 4069     {'house_number': '508', 'road': '20th Avenue E...
# 15300    {'house_number': '15835', 'road': 'Northeast 1...
# Name: city, dtype: object

# Inicialmente este código estáva correto mas ocorreu o erro AdapterHTTPError.
# Tentamos corrigir alterando o módulo Nominatim para o Photon mas apresentou o mesmo erro.
