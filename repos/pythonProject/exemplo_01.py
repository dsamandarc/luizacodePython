#carregue o conjunto de dados chamado kc_house_data.csv do HD para a memória
import pandas as pd

data = pd.read_csv ( 'datasets/kc_house_data.csv' )

print ( data.head())