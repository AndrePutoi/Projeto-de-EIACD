import pandas as pd
import statistics as stats

# Vamos Calcular a média, mediana e moda, desvio padrao e variancia de 'price', 'lotSize', 'livingArea', 'bathrooms', 'bedrooms', 'yearBuilt'

df_u = pd.read_csv('Cleaned_Dataset/Dataset_Cleaned.csv')

def Estatistica(df_u, coluna):
    print("Media de ", coluna, ": ", stats.mean(df_u[coluna]))
    print("Mediana de ", coluna, ": ", stats.median(df_u[coluna]))
    print("Moda de ", coluna, ": ", stats.mode(df_u[coluna]))
    print("Desvio Padrao de ", coluna, ": ", stats.stdev(df_u[coluna]))
    print("Variancia de ", coluna, ": ", stats.variance(df_u[coluna]))
    print("\n")

Estatistica(df_u, 'price')
Estatistica(df_u, 'lotSize')
Estatistica(df_u, 'livingArea')
Estatistica(df_u, 'bathrooms')
Estatistica(df_u, 'bedrooms')
Estatistica(df_u, 'yearBuilt')


# A partir de analise grafica, analisar a distribuicao de cada variavel



# A partir de analise grafica, verificar se duas variaveis tem correlacao