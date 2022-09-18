from typing import Any

import numpy as np
import pandas as pd
# Loading the dataset
data = pd.read_csv ( 'datasets/kc_house_data.csv')

#1-	How many properties are available to buy? - strategy: select the id column and count the number of unique values
print (len ( data ['id'].unique()))
#other possibility
print (len (data ['id'].drop_duplicates()))

#2-	How many characteristics do the properties possess? - strategy: assumptions 'id' and 'date' are not characteristics
print (len (data.drop( ['id' , 'date'], axis=1 ).columns))

#3-	Which are those characteristics? (Number of bedrooms, number of garages, m², site, etc.) - strategy: assumptions
# 'id' and 'date' are not characteristics
print ( data.drop( ['id' , 'date'], axis=1 ).columns.tolist())

#4-	 Which is the most expansive property? (The property with the bigger price)
print (data[['id', 'price']].sort_values('price', ascending=False).reset_index(drop=True).loc[0, 'id'])

#5-	Which is the property with the bigger number of bedrooms?
print (data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False).reset_index(drop=True).loc[0, 'id'])

#6-	What is the total of bedrooms in the dataset?
print (data ['bedrooms'].sum())

#7-	How many houses have two bathrooms? strategy: filter only the 'id' where the column 'bathroom' is equal to 2
houses =len ( data.loc[data['bathrooms'] == 2, [ 'id', 'bathrooms']])
print ('The number of houses with 2 bathrooms are {}'.format( houses ))

#8- What is the average price of all houses in the dataset? strategy: check if price is a float and not an object
#than take the mean with a round with two decimal places after the point
print (np.round( data['price'].mean(), 2 ))
