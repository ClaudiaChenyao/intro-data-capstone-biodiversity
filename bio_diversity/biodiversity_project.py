import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

# Loading the Data
species = pd.read_csv('species_info.csv')
# print species.head()
print(species.head())

#number of different species
species_count = species.scientific_name.nunique()
print('The number of different species in the DataFrame is ' +str(species_count))
print('\n\n')

#species types
species_type = species.category.unique()
print('The species types include: ')
print(species_type)
print('\n\n')

#conservation statues
conservation_statuses = species.conservation_status.unique()
print(conservation_statuses)
print('\n\n')


conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print('The conservation_status counts')
print(conservation_counts)
print('\n\n')

#fixed conservation statues
species.fillna('No Intervention', inplace = True)
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print('The fixed conservation_status counts')
print(conservation_counts_fixed)