
#++++++++++++++++++++
#Como converter os tipos de variáveis
#++++++++++++++++++++

#carregar um arquivo do disco rígido para a memória
# #toda função tem parâmetros de entrada e ela me da um resultado (saída). A função é uma sequência de comandos, que a gente
# #não precisa saber quais são, mais precisamos saber o que ela faz
#
# #a função é guardada dentro de uma biblioteca, a biblioteca armazena várias funções. Como as biblios as vezes tem
# #nomes muito grandes a gente coloca um apelido, no caso da pandas é pd
#
# import pandas as pd
#
# data = pd.read_csv('datasets/kc_house_data.csv')
# #posso também já alterar o formato das datas com data = pd.read_csv('datasets/kc_house_data.csv', parse_dates=['date'])
#
# #mostrar na tela as primeiras 6 linhas
# print(data.head())
#
# #função que mostra na tela os tipos de variáveis em cada coluna
# print( data.dtypes )
#
# #função que converte de object (string) para date
# data['date'] = pd.to_datetime(data['date'])
#
# #função que mostra na tela os tipos de variáveis em cada coluna
# print( data.dtypes )
#
# #conversões entre variáveis:
# #inteiro para float
# data['bedrooms'] = data['bedrooms'].astype(float)
# print( data.dtypes )
#
# #float para inteiro
# data['bedrooms'] = data['bedrooms'].astype(int)
# print( data.dtypes )
#
# #inteiro para string
# data['bedrooms'] = data['bedrooms'].astype(str)
# print( data.dtypes )
#
# #string para inteiro
# import numpy as np
# data['bedrooms'] = data['bedrooms'].astype(np.int64)
# print ( data.dtypes)
#
# #string para date
# data['date'] = pd.to_datetime(data['date'])
# print ( data.dtypes)

#++++++++++++++++++
#Criando novas variáveis
#++++++++++++++++++
# import pandas as pd
# import numpy as np
# data = pd.read_csv('datasets/kc_house_data.csv')
#
# #Vou chamar minha variável de Amanda, quero criar uma coluna com meu nome. Como eu atribuo uma
# #string que é essa união de letras, dentro de uma coluna. Eu faço isso pelo operador atribuição
# #que é o igual, ele é uma atribuição.
#
# data['nome_da_amanda'] = "amanda"
# print (data.columns)
#
# #selecionar a coluna
# print(data[['id', 'date', 'nome_da_amanda']])
#
# #Posso criar um string e depois converter ou já na formação eu consigo converter para o tipo que eu quero
# data['data_de_aniversario'] = pd.to_datetime('1993-05-14')
# print (data.dtypes)

#++++++++++++++++++
#Deletar variáveis
#++++++++++++++++++
# #quando você usa o comando drop que você faz o delete, é preciso determinar também um sentido
# #quando eu faço um delete eu posso fazer isso no sentido das linhas ou das colunas
# print(data.columns)
# #data = data.drop('nome_da_amanda', axis=1)
# print(data.columns)
# #quando eu tenho várias colunas para deletar eu posso passar uma lista, é uma estrutura de dados
# #onde você guarda variáveis, é tudo o que estiver entre colchetes
#
# data = data.drop(['nome_da_amanda', 'data_de_aniversario'], axis=1)
# print(data.columns)
# #outra opção é determinar uma variável chamada colunas e coloca suas variáveis de interesse e
# #depois coloca a lista para a função
# cols = ['nome_da_amanda', 'data_de_aniversario']
# data = data.drop(cols , axis=1)

#++++++++++++++++++
#Selecionar variáveis
#++++++++++++++++++
import pandas as pd
import numpy as np
data = pd.read_csv('datasets/kc_house_data.csv')

#Selecionar direto pelo nome das colunas:
print( data['price'])
#Se eu quiser selecionar mais colunas de uma vez eu não posso fazer assim
# print (data ['price', 'id', 'date']), porque isso ['price', 'id', 'date'] é uma lista, eu tenho
# que passar isso dentro de uma lista
cols = ['price', 'id', 'date']
print (data[cols])
#posso também colocar duplo colchetes para colocar a lista
print (data[['price', 'id', 'date']])

#Selecionar pelos índices das linhas e colunas: toda coluna e toda linha elas têm um índice
#esse índice é o índice incremental, então, primeira linha é zero, segunda é 1, etc. Então,
#se eu não souber o nome das colunas eu posso selecionar pelos índices dela
#Então eu tenho os meus dados e sempre eles no formato do pandas, o dataframe ele sempre vem no
#formato [linhas,colunas]. Sempre que eu vou usar o índex eu tenho que lembrar que todo número
#no colchete o primeiro é linhas e o segundo depois da linha é coluna.
#por exemplo se eu quiser pegar a linha zero até a dez e a coluna zero até a 3, vai ficar assim
#[0:10, 0:3].
#Se eu rodar print (data [0:10, 0:3]) isso dá um erro, porque eu não tenho uma função aqui
#toda vez que você não sabe o nome da coluna o pandas também não sabe, então você tem que passar
#o index para ele, então quando você não sabe o nome das colunas você tem que usar uma função
#que se chama iloc. Se você quiser todas as linhas é só colocas [: , 0:5]
print (data.iloc[0:10, 0:3])

#SElecionar pelos índices das linhas e nome das colunas
#Ele vai dar um erro mesmo se você usar a função iloc: print (data.iloc[0:10, 'price']), então
#tem que ser a função .loc, que seria um 'localize para mim pelo nome das colunas'
print (data.loc[0:10, 'price'])
print (data.loc[0:10, ['price', 'id', 'date']])

#Selecionar pelos índices Booleanos: 1 ou 0, true or false. Eu vou pegar a minha lista de colunas
#e colocar true para as que eu quero e false para as que não. O mesmo número de true or false, tem
#que ser igual ao de colunas. E eu uso a função loc, pq não são índex.

cols = [True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
print(data.loc[0:10, cols])