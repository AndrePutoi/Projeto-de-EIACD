import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats


# Verificar quantas variáveis e quantos valores nulos existem
df_u = pd.read_csv("Uncleaned_Dataset/Dataset_Uncleaned.csv", low_memory=False)
#print(df_u.isnull().sum())

# Se existirem valores nulos, se existe uma razão para isso, relacionado com outra variável

# Como latitude e longitude têm poucos valores nulos, nao iremos compara-los com outras variáveis, e simplesmente apagar as colunas que os mesmos estão presentes na limpeza de dados

# Verificar a distribuição de valores Nan para cada variável

def Comparar_variavel(df_u, variavel):
    head = list(df_u.columns)
    head.pop(0)  # Eliminar 'Unnamed: 0'
    head.remove(variavel)
    missing_inc = df_u[variavel].isnull()
    df_miss = df_u[missing_inc]
    df_not_miss = df_u[missing_inc == False]

    for col in head:
        fig = plt.figure()
        ax1 = fig.add_subplot(1,2,1)
        ax1 = plt.hist(df_miss[col])
        ax2 = fig.add_subplot(1,2,2)
        ax2 = plt.hist(df_not_miss[col])
        fig.suptitle(col, fontsize=16)
        plt.show()

#Comparar_variavel(df_u, 'lotSize')
#Comparar_variavel(df_u, 'bedrooms')
#Comparar_variavel(df_u, 'bathrooms')
#Comparar_variavel(df_u, 'livingArea')

#Foi verificado que o tipo de distribuição dos valores nulos é aliatória, pois nenhum dos valores nulos tem uma distribuição comparavel a outra variável

#Sendo assim vamos tratar dos valores nulos de 'yearBuilt', 'latitude' e 'longitude' apagando as linhas onde os mesmos estão presentes

df_u.dropna(subset=['yearBuilt', 'latitude', 'longitude'], inplace=True)
#Verificar se ainda existem valores nulos em 'yearBuilt', 'latitude' e 'longitude':
#print(df_u['yearBuilt'].isnull().sum())
#print(df_u['latitude'].isnull().sum())
#print(df_u['longitude'].isnull().sum())

# Vamos calcular a media , mediana e moda de 'lotSize'

#print("Media de lotSize: ", stats.mean(df_u['lotSize'].dropna()))
#print("Mediana de lotSize: ", stats.median(df_u['lotSize']))
#print("Moda de lotSize: ", stats.mode(df_u['lotSize']))

#Após ver a media, mediana e moda,para tratar dos nan da variavel 'lotSize' vamos preencher da seguinte forma:
#se livingArea < moda de lotSize, preencher com a moda de lotSize
#se livingArea > moda de lotSize e livingArea < mediana de lotSize, preencher com a mediana de lotSize
#se livingArea > mediana de lotSize, apagar a linha, a media é desproporcionalmente maior que a mediana e moda
lotSize_mode = stats.mode(df_u['lotSize'])
lotSize_median = stats.median(df_u['lotSize'])
df_u.loc[(df_u['lotSize'].isnull()==False) & (df_u['livingArea'] < lotSize_mode), 'lotSize'] = lotSize_mode
df_u.loc[(df_u['lotSize'].isnull()==False) & (df_u['livingArea'] > lotSize_mode) & (df_u['livingArea'] < lotSize_median), 'lotSize'] = lotSize_median
df_u.dropna(subset=['lotSize'], inplace=True)  # Remover as linhas onde 'lotSize' é nulo após os ajustes

#verificar se ainda existem valores nulos em 'lotSize'
#print(df_u['lotSize'].isnull().sum())

#Fazer o mesmo para 'livingArea'

print("Media de livingArea: ", stats.mean(df_u['livingArea'].dropna()))
print("Mediana de livingArea: ", stats.median(df_u['livingArea']))
print("Moda de livingArea: ", stats.mode(df_u['livingArea']))

#Após ver a media, mediana e moda,para tratar dos nan da variavel 'livingArea' vamos preencher da seguinte forma:
#se lotSize < mediana de livingArea, eliminar a linha
#se lotSize > mediana de livingArea e loSize < moda de livingArea, preencher com a mediana de livingArea
#se lotSize > moda de livingArea e lotSize < media de livingArea, preencher com a moda de livingArea
#se lotSize > moda de livingArea, preencher com a media de livingArea

livingArea_mean = stats.mean(df_u['livingArea'])
livingArea_mode = stats.mode(df_u['livingArea'])
livingArea_median = stats.median(df_u['livingArea'])


df_u.loc[(df_u['livingArea'].isnull()==False) & (df_u['lotSize'] > livingArea_median) & (df_u['lotSize'] < livingArea_mode), 'livingArea'] = livingArea_median
df_u.loc[(df_u['livingArea'].isnull()==False) & (df_u['lotSize'] > livingArea_mode) & (df_u['lotSize'] < livingArea_mean), 'livingArea'] = livingArea_mode
df_u.loc[(df_u['livingArea'].isnull()==False) & (df_u['lotSize'] > livingArea_mean), 'livingArea'] = livingArea_mean
df_u.dropna(subset=['livingArea'], inplace=True)  # Remover as linhas onde 'livingArea' é nulo após os ajustes

#verificar se ainda existem valores nulos em 'livingArea'
#print(df_u['livingArea'].isnull().sum())

#Agora para os valores nulos de 'bedrooms' e 'bathrooms', apagandos os nans, vamos verificar se existe uma boa regressao entre as variáveis, e sendo assim preencher os valores nulos de 'bedrooms' e 'bathrooms' com base na regressao

df_u_sample = df_u.copy()
df_u_sample = df_u_sample[['bedrooms', 'bathrooms']]
df_u_sample = df_u_sample.dropna()
X = list(df_u_sample['bedrooms'])
y = list(df_u_sample['bathrooms'])
plt.scatter(X, y)
plt.show()

#(duvida)...

#Descoberta e remoção de outliers
#comparaçao entre duas variaveis visualmente num grafico de disperção

def Grafico_de_disperção(df_u,val1, val2):
    df_u_sample = df_u.copy()
    df_u_sample = df_u_sample[[val1, val2]]
    df_u_sample = df_u_sample.dropna()
    X = list(df_u_sample[val1])
    y = list(df_u_sample[val2])
    plt.xlabel(val1)
    plt.ylabel(val2)
    plt.scatter(X, y)
    plt.show()

#Grafico_de_disperção(df_u, 'price', 'lotSize')
#Grafico_de_disperção(df_u, 'price', 'livingArea')
#Grafico_de_disperção(df_u, 'price', 'bathrooms')
#Grafico_de_disperção(df_u, 'price', 'bedrooms')
#Grafico_de_disperção(df_u, 'price', 'yearBuilt')
#Grafico_de_disperção(df_u, 'price', 'latitude')
#Grafico_de_disperção(df_u, 'price', 'longitude')

#Grafico_de_disperção(df_u, 'lotSize', 'livingArea')
#Grafico_de_disperção(df_u, 'lotSize', 'bathrooms')
#Grafico_de_disperção(df_u, 'lotSize', 'bedrooms')
#Grafico_de_disperção(df_u, 'lotSize', 'yearBuilt')
#Grafico_de_disperção(df_u, 'lotSize', 'latitude')
#Grafico_de_disperção(df_u, 'lotSize', 'longitude')

#Grafico_de_disperção(df_u, 'livingArea', 'bathrooms')
#Grafico_de_disperção(df_u, 'livingArea', 'bedrooms')
#Grafico_de_disperção(df_u, 'livingArea', 'yearBuilt')
#Grafico_de_disperção(df_u, 'livingArea', 'latitude')
#Grafico_de_disperção(df_u, 'livingArea', 'longitude')

#Grafico_de_disperção(df_u, 'bathrooms', 'bedrooms')
#Grafico_de_disperção(df_u, 'bathrooms', 'yearBuilt')
#Grafico_de_disperção(df_u, 'bathrooms', 'latitude')
#Grafico_de_disperção(df_u, 'bathrooms', 'longitude')

#Grafico_de_disperção(df_u, 'bedrooms', 'yearBuilt')
#Grafico_de_disperção(df_u, 'bedrooms', 'latitude')
#Grafico_de_disperção(df_u, 'bedrooms', 'longitude')

#Grafico_de_disperção(df_u, 'yearBuilt', 'latitude')
#Grafico_de_disperção(df_u, 'yearBuilt', 'longitude')

#Grafico_de_disperção(df_u, 'latitude', 'longitude')

#Após


