import pandas as pd
import matplotlib.pyplot as plt
import statistics as statts
import numpy as np
from scipy import stats

# Verificar quantas variáveis e quantos valores nulos existem
df_u = pd.read_csv("Uncleaned_Dataset/Dataset_Uncleaned.csv", low_memory=False)
#print(df_u.isnull().sum())
#retirar o 'Unnamed: 0'
df_u.drop('Unnamed: 0', axis=1, inplace=True)

# Se existirem valores nulos, se existe uma razão para isso, relacionado com outra variável

# Como latitude e longitude têm poucos valores nulos, nao iremos compara-los com outras variáveis, e simplesmente apagar as colunas que os mesmos estão presentes na limpeza de dados

# Verificar a distribuição de valores Nan para cada variável

def Comparar_variavel(df_u, variavel):
    head = list(df_u.columns)
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

#Foi verificado que o tipo de distribuição dos valores nulos é aleatória, pois nenhum dos valores nulos tem uma distribuição comparavel a outra variável

#Sendo assim vamos tratar dos valores nulos de 'yearBuilt', 'latitude' e 'longitude', 'bathroom' apagando as linhas onde os mesmos estão presentes

df_u.dropna(subset=['yearBuilt', 'latitude', 'longitude', 'bathrooms', 'bedrooms'], inplace=True)
#Verificar se ainda existem valores nulos em 'yearBuilt', 'latitude' e 'longitude':
#print(df_u['yearBuilt'].isnull().sum())
#print(df_u['latitude'].isnull().sum())
#print(df_u['longitude'].isnull().sum())

# Vamos calcular a media , mediana e moda de 'lotSize'

#print("Media de lotSize: ", statts.mean(df_u['lotSize'].dropna()))
#print("Mediana de lotSize: ", statts.median(df_u['lotSize']))
#print("Moda de lotSize: ", statts.mode(df_u['lotSize']))

#Após ver a media, mediana e moda,para tratar dos nan da variavel 'lotSize' vamos preencher da seguinte forma:
#se livingArea < moda de lotSize, preencher com a moda de lotSize
#se livingArea > moda de lotSize e livingArea < mediana de lotSize, preencher com a mediana de lotSize
#se livingArea > mediana de lotSize, apagar a linha, a media é desproporcionalmente maior que a mediana e moda
lotSize_mode = statts.mode(df_u['lotSize'])
lotSize_mean = statts.mean(df_u['lotSize'])
df_u.loc[(df_u['lotSize'].isnull()==False) & (df_u['livingArea'] < lotSize_mode), 'lotSize'] = lotSize_mode
df_u.loc[(df_u['lotSize'].isnull()==False) & (df_u['livingArea'] > lotSize_mode) & (df_u['livingArea'] < lotSize_mean), 'lotSize'] = lotSize_mean
df_u.dropna(subset=['lotSize'], inplace=True)  # Remover as linhas onde 'lotSize' é nulo após os ajustes

#verificar se ainda existem valores nulos em 'lotSize'
#print(df_u['lotSize'].isnull().sum())

#Fazer o mesmo para 'livingArea'

print("Media de livingArea: ", statts.mean(df_u['livingArea'].dropna()))
print("Mediana de livingArea: ", statts.median(df_u['livingArea']))
print("Moda de livingArea: ", statts.mode(df_u['livingArea']))

#Após ver a media, mediana e moda,para tratar dos nan da variavel 'livingArea' vamos preencher da seguinte forma:
#se lotSize < mediana de livingArea, eliminar a linha
#se lotSize > mediana de livingArea e loSize < moda de livingArea, preencher com a mediana de livingArea
#se lotSize > moda de livingArea e lotSize < media de livingArea, preencher com a moda de livingArea
#se lotSize > moda de livingArea, preencher com a media de livingArea

livingArea_mean = statts.mean(df_u['livingArea'])
livingArea_mode = statts.mode(df_u['livingArea'])
livingArea_median = statts.median(df_u['livingArea'])


df_u.loc[(df_u['livingArea'].isnull()==False) & (df_u['lotSize'] > livingArea_median) & (df_u['lotSize'] < livingArea_mode), 'livingArea'] = livingArea_median
df_u.loc[(df_u['livingArea'].isnull()==False) & (df_u['lotSize'] > livingArea_mode) & (df_u['lotSize'] < livingArea_mean), 'livingArea'] = livingArea_mode
df_u.loc[(df_u['livingArea'].isnull()==False) & (df_u['lotSize'] > livingArea_mean), 'livingArea'] = livingArea_mean
df_u.dropna(subset=['livingArea'], inplace=True)  # Remover as linhas onde 'livingArea' é nulo após os ajustes

#verificar se ainda existem valores nulos em 'livingArea'
#print(df_u['livingArea'].isnull().sum())


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

#col = ['price', 'bedrooms', 'bathrooms', 'livingArea', 'lotSize', 'yearBuilt']
#for i in range(len(col)):
#    for j in range(i+1, len(col)):
#        Grafico_de_disperção(df_u, col[i], col[j])


#Após analisar os graficos de disperção, foi verificado que existem outliers, usaremos o metodo de z-score para remover os outliers

def remove_outliers(df_u, col):
    df_u_sample = df_u.copy()
    df_u_sample = df_u_sample[[col]]
    df_u_sample = df_u_sample.dropna()
    z = np.abs(stats.zscore(df_u_sample))
    threshold = 4
    df_u.drop(df_u[(z > threshold).all(axis=1)].index, inplace=True)

remove_outliers(df_u, 'price')
#remove_outliers(df_u, 'lotSize')
remove_outliers(df_u, 'livingArea')
remove_outliers(df_u, 'bathrooms')
remove_outliers(df_u, 'bedrooms')
remove_outliers(df_u, 'yearBuilt')

#Verificar se ainda existem outliers

#for i in range(len(col)):
#    for j in range(i+1, len(col)):
#        Grafico_de_disperção(df_u, col[i], col[j])

#Apos uma primeira verificação, os outliers foram removidos com sucesso, à exceçao de 'lotSize', pois demasiados dados foram removidos, vamos tentar remover os outliers de 'lotSize' de outra forma, ou ver se a remoção de outliers de outras variáveis afetou 'lotSize'

#Apos verificar os graficos de disperção, os outliers foram removidos com sucesso

#Colocar as datas de venda no formato '%d/%m/%Y'

df_u['dateSold'] = pd.to_datetime(df_u['dateSold'], format='%m/%d/%Y')
df_u['dateSold'] = df_u['dateSold'].dt.strftime('%d/%m/%Y')

#assim o dataset ja foi limpo de Nan data e outliers
df_u.to_csv('Cleaned_Dataset/Dataset_Cleaned.csv', index=False)


