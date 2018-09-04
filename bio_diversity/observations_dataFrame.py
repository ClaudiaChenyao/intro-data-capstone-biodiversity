import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'
print(species)

#read observations
observations = pd.read_csv('observations.csv')

species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)

species_is_sheep = species[species.is_sheep]
print(species_is_sheep)

#get the real sheep info
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
print(sheep_species)

#merge two tables
sheep_observations = pd.merge(sheep_species,observations)
print(sheep_observations.head())

#get the number of sheep observed by park
obs_by_park = sheep_observations.groupby(sheep_observations.park_name).observations.sum().reset_index()
print(obs_by_park)