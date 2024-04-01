import statistics
import pandas as pd

# Verificar quantas variáveis e quantos valores nulos existem
df_u = pd.read_csv("Dataset_raw/Dataset_Uncleaned", low_memory=False)
dataset_1 = pd.read_csv('Dataset_raw/kc_house_data.csv', low_memory=False)
dataset_2 = pd.read_csv('Dataset_raw/Zillow_Austin_11-16-22.csv', low_memory=False)
dataset_1 = dataset_1.drop(
    columns=['id', 'sqft_living', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement',
             'yr_renovated', 'sqft_living15', 'sqft_lot15'])
dataset_2 = dataset_2.drop(
    columns=['unformattedPrice', 'address', 'addressStreet', 'addressCity', 'addressState', 'isZillowOwned',
             'variableData', 'badgeInfo', 'pgapt', 'sgapt', 'zestimate', 'info3String', 'brokerName'])
print(dataset_2.isnull().sum())
print(dataset_1.isnull().sum())