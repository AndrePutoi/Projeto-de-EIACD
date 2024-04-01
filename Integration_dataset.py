import pandas as pd


dataset_1 = pd.read_csv('Dataset_raw/kc_house_data.csv', low_memory=False)
dataset_2 = pd.read_csv('Dataset_raw/Zillow_Austin_11-16-22.csv', low_memory=False)


#Ver as variávers de cada dataset

#print(list(dataset_1.columns))
#print(list(dataset_2.columns))



#Ver tamanho das variáveis

#print(len(list(dataset_1.columns)))
#print(len(list(dataset_2.columns)))


#Após escolher as variáveis a juntar, renomeá-las com o mesmo nome


dataset_1 = dataset_1.rename(columns={'bedrooms': 'Bedroom'})
dataset_1 = dataset_1.rename(columns={'sqft_lot': 'BuildingArea'})
dataset_1 = dataset_1.rename(columns={'bathrooms': 'Bathroom'})
dataset_1 = dataset_1.rename(columns={'lat': 'Latitude'})
dataset_1 = dataset_1.rename(columns={'long': 'Longtitude'})
dataset_1 = dataset_1.rename(columns={'price': 'Price'})
dataset_1 = dataset_1.rename(columns={'zipcode': 'Zipcode'})

dataset_2 = dataset_2.rename(columns={'beds': 'Bedroom'})
dataset_2 = dataset_2.rename(columns={'area': 'BuildingArea'})
dataset_2 = dataset_2.rename(columns={'baths': 'Bathroom'})
dataset_2 = dataset_2.rename(columns={'latitude': 'Latitude'})
dataset_2 = dataset_2.rename(columns={'longitude': 'Longtitude'})
dataset_2 = dataset_2.rename(columns={'price': 'Price'})
dataset_2 = dataset_2.rename(columns={'addressZipcode': 'Zipcode'})



#Retirar variáveis a mais
dataset_2 = dataset_2.drop(columns=['unformattedPrice', 'address', 'addressStreet', 'addressCity', 'addressState', 'isZillowOwned', 'variableData', 'badgeInfo', 'pgapt', 'sgapt', 'zestimate', 'info3String', 'brokerName'])
dataset_1 = dataset_1.drop(columns=['id', 'sqft_living', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement', 'yr_renovated', 'sqft_living15', 'sqft_lot15'])


df = pd.concat([dataset_1, dataset_2], ignore_index=True)

file_raw ="Dataset_raw/Dataset_Uncleaned"
df.to_csv(file_raw)