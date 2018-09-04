import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)

#select the protected items
species['is_protected'] = species.conservation_status != 'No Intervention'

#get the category counts
category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()

#get the category pivot
category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()
  
 #reset the colums
category_pivot.columns = ['category', 'not_protected', 'protected']

#get the precentage
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

print(category_pivot)