import pandas as pd
import statistics as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go





# Vamos Calcular a média, mediana e moda, desvio padrao e variancia de 'price', 'lotSize', 'livingArea', 'bathrooms', 'bedrooms', 'yearBuilt'

df = pd.read_csv('Cleaned_Dataset/Dataset_Cleaned.csv')

def Estatistica(df, coluna):
    print("Media de ", coluna, ": ", stats.mean(df[coluna]))
    print("Mediana de ", coluna, ": ", stats.median(df[coluna]))
    print("Moda de ", coluna, ": ", stats.mode(df[coluna]))
    print("Desvio Padrao de ", coluna, ": ", stats.stdev(df[coluna]))
    print("Variancia de ", coluna, ": ", stats.variance(df[coluna]))
    print("\n")

#Estatistica(df, 'price')
#Estatistica(df, 'lotSize')
#Estatistica(df, 'livingArea')
#Estatistica(df, 'bathrooms')
#Estatistica(df, 'bedrooms')
#Estatistica(df, 'yearBuilt')


# A partir de analise grafica, analisar a distribuicao de cada variavel



# A partir de analise grafica, verificar se duas variaveis tem correlacao



# Verificar se existem valores unicos em cada variavel
#valores_unicos = df.nunique()
#print(valores_unicos)


# Verificar a correlacao entre as variaveis através de um Mapa de Calor
#df = df.drop(columns=['dateSold', 'state', 'zipcode'])
#matriz_correlação = df.corr()
#plt.figure(figsize=(10, 7))
#sns.heatmap(matriz_correlação, annot=True)
#plt.show()


# Script: Era suposto ser um Histograma que representa a quantidade de imóveis num intervalo de preço, mas acabou por somar todos os preços em cada ano
#df = df[['price']]
#fig = px.histogram(df, x='price', title='Distribuição de Preços')
#fig.show()


# Histograma que representa a quantidade de imóveis com um determinado tamanho em square footage
#df['livingArea'].hist(bins=30)
#plt.xlabel('Tamanho dos imóveis')
#plt.ylabel('Número de imóveis')
#plt.title('Quantidade de imóveis com um determinado tamanho em sqft')
#plt.show()


# Gráfico de barras que representa a quantidade de imóveis com um determinado número de quartos
#data = pd.Series(df['bedrooms'])
#tabela_freq = data.value_counts(sort=False)
#df_freq = pd.DataFrame({'Quartos': tabela_freq.index, 'Frequência': tabela_freq.values})
#plt.bar(df_freq['Quartos'], df_freq['Frequência'], color='skyblue')
#plt.xlabel('Número de Quartos')
#plt.ylabel('Número de Imóveis')
#plt.title('Frequência de Quartos')
#plt.grid(axis='y', linestyle='--', alpha=0.7)
#plt.show()


# Gráfico de barras que representa o preço dos imóveis por ano de construção
#fig = px.bar(df, x='yearBuilt', y='price', title='Preço dos imóveis por ano de construção')
#fig.show()


# Código para saber quantos imóveis foram vendidos em cada ano
#df['dateSold'] = pd.to_datetime(df['dateSold'], format='%d/%m/%Y')
#years = df['dateSold'].dt.year
#df_years = years.value_counts()
#print(df_years)

# Gráfico pie que representa a percentagem de imóveis vendidos em cada ano
#fig = px.pie(values=['14245', '10931', '10244', '6797'], names=['2014', '2021', '2020', '2015'], title='Percentagem de imóveis vendidos em cada ano')
#fig.show()


# Código para saber quantos imóveis existem em cada estado
#df_states = df['state'].value_counts()
#print(df_states)

# Gráfico donut que representa a percentagem de imóveis em cada estado
#fig = px.pie(values=['21175','21042'], names=['Washington', 'Oregon'], title='Percentagem de imóveis em cada estado', hole=.3)
#fig.show()


# Gráfico de barras que representa a quantidade de imóveis com um determinado número de casas de banho
#data = pd.Series(df['bathrooms'])
#tabela_freq = data.value_counts(sort=False)
#df_freq = pd.DataFrame({'Casas de banho': tabela_freq.index, 'Frequência': tabela_freq.values})
#plt.bar(df_freq['Casas de banho'], df_freq['Frequência'], color='skyblue')
#plt.xlabel('Número de Casas de Banho')
#plt.ylabel('Número de Imóveis')
#plt.title('Frequência de Casas de Banhos')
#plt.grid(axis='y', linestyle='--', alpha=0.7)
#plt.show()


# Histograma que representa a quantidade de imóveis construídos num intervalo de tempo
#df = df[['yearBuilt']]
#fig = px.histogram(df, x='yearBuilt', title='Distribuição de Anos de Construção')
#fig.show()


# Gráfico de barras que relaciona as médias do preço com a quantidade de casas de banho
#df_pb = df[['price', 'bathrooms']]
#medias = []
#for i in range(df_pb['bathrooms'].nunique()):
#    dff = df_pb[df_pb['bathrooms'] == i]
#    medias.append(stats.mean(list(dff['price'])))
#fig = go.Figure(
#    data=[go.Bar(y=medias, x=[i for i in range(df_pb['bathrooms'].nunique())])],
#    layout_title_text="Média de Preço por Número de Casas de Banho"
#)
#fig.update_xaxes(title_text="Número de Casas de Banho")
#fig.update_yaxes(title_text="Preço Médio")
#fig.show()


# Gráfico de barras que relaciona as médias do preço com a quantidade de quartos
#df_pq = df[['price', 'bedrooms']]
#medias = []
#for i in range(1,df_pq['bedrooms'].nunique()+1):
#    dff = df_pq[df_pq['bedrooms'] == i]
#    medias.append(stats.mean(list(dff['price'])))
#fig = go.Figure(
#    data=[go.Bar(y=medias, x=[i for i in range(1,df_pq['bedrooms'].nunique()+1)])],
#    layout_title_text="Média de Preço por Número de Quartos"
#)
#fig.update_xaxes(title_text="Número de Quartos")
#fig.update_yaxes(title_text="Preço Médio")
#fig.show()


# Histogramas que representam a distribuição dos preços dos imóveis em Washington e Oregon
#df_ps = df[['price', 'state']]
#df_pw = df_ps[df_ps['state'] == "Washington"]
#df_po = df_ps[df_ps['state'] == "Oregon"]
#price_w = df_pw['price'].tolist()
#price_o = df_po['price'].tolist()
#fig = go.Figure()
#fig.add_trace(
#    go.Histogram(
#        x=price_w,
#        name='Washington'
#    ))
#fig.add_trace(
#    go.Histogram(
#        x=price_o,
#        name='Oregon'
#    ))
#fig.update_layout(
#    title='Distribuição dos preços dos imóveis em Washington e Oregon',
#    xaxis_title='Preço',
#    yaxis_title='Frequência'
#)
#fig.show()


#relacionar a media do preço com o ano de construção de uma casa
#df_py = df[['price', 'yearBuilt']]
#medias = []
#for i in df_py['yearBuilt'].unique():
#    dff = df_py[df_py['yearBuilt'] == i]
#    medias.append(stats.mean(list(dff['price'])))
#fig = go.Figure(
#    data=[go.Bar(y=medias, x=[i for i in df_py['yearBuilt'].unique()])],
#    layout_title_text="Média de Preço por Ano de Construção"
#)
#fig.update_layout(
#    title='Média de Preço por Ano de Construção',
#    xaxis_title='Anos de Construção',
#    yaxis_title='Preço Médio')
#fig.show()


# Gráfico de barras que relacionar o preço com o ano de venda
#df['dateSold'] = pd.to_datetime(df['dateSold'], format='%d/%m/%Y')
#years = list(df['dateSold'].dt.year)
#years = list(set(years))
#def BubbleSortv1(arr):
#    Ex_trade = True
#    while Ex_trade:
#        Ex_trade = False
#        for i in range(1,len(arr)):
#            if arr[i-1]>arr[i]:
#                aux = arr[i-1]
#                arr[i-1]= arr[i]
#                arr[i]= aux
#                Ex_trade = True
#    return arr
#years = BubbleSortv1(years)
#df_py = df[['price', 'dateSold']]
#medias = []
#for i in years:
#    dff = df_py[df_py['dateSold'].dt.year == i]
#    medias.append(stats.mean(list(dff['price'])))
#fig = go.Figure(
#    data=[go.Bar(y=medias, x=years)],
#    layout_title_text="Média de Preço por Ano de Venda"
#)
#fig.update_layout(
#    xaxis_title='Anos de Venda',
#    yaxis_title='Preço Médio'
#)
#fig.show()