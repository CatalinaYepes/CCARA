# -*- coding: utf-8 -*-
"""
@author: catalinayepes
"""

import os
import pandas as pd
from select_files import select_files
from dwellings_to_buildings import dwellings_to_buildings
from add_Population import add_Population



def add_centroids(data, country):
    '''Add centroids from csv file'''
    centroid_folder = '../1_maps/centroids'
    centroid_file = select_files(centroid_folder, contain= country, end='centroids.csv')
    centroids = pd.read_csv(os.path.join(centroid_folder, centroid_file))
    centroids.X = centroids.X.round(5)
    centroids.Y = centroids.Y.round(5)

    df = pd.merge(data, centroids[['X', 'Y', 'ID_CENSO']], how='left', left_on='id', right_on='ID_CENSO')
    df.drop('ID_CENSO', axis=1, inplace=True)
    df.rename(columns={'X':'lon', 'Y':'lat'}, inplace=True)
    
    return df

dwl_folder = '../dwellings_v0_Feb2017'
dwelling_files = select_files(dwl_folder, contain= '-dwellings', end='.csv')

bdg_folder = '../buildings_v0_Mar2017'
repl_cost_file = os.path.join(bdg_folder,'Replacement_cost_v0.xlsx')

# Population files
pop_files = pd.DataFrame({
"blz":['../0_censos_res/pop-Belize-2010.xlsx', 'Regions-Pop_2010'],
"brb":['../0_censos_res/pop-Barbados-2010.xlsx', 'Parish-pop-2010'],
"cub":['../0_censos_res/pop-Cuba-2012.xlsx', 'Municipio'],
"dom":['../0_censos_res/pop-RepDominicana-2010.xlsx', 'Distrito'],
"gtm":['../0_censos_res/pop-Guatemala-2002.xlsx', 'Municipio'],
"hnd":['../0_censos_res/pop-Honduras-2013.xlsx', 'Municipio'],
"jam":['../0_censos_res/pop-Jamaica-2011.xlsx', 'Parish'],
"nic":['../0_censos_res/pop-Nicaragua-2005.xlsx', 'Municipio'],
"pan":['../0_censos_res/pop-Panama-2010.xlsx', 'Corregimiento'],
"slv":['../0_censos_res/pop-Salvador-2007.xlsx', 'Municipio'],
"tto":['../0_censos_res/pop-TTO-2000.xlsx', 'Municipality'],
})    

# Estimate buildings and population
if isinstance(dwelling_files, str):
    dwelling_files = [dwelling_files]
    
for dwl_file in dwelling_files:
    
    print '\n', dwl_file
    country = dwl_file[:3]    
    dwl_path = os.path.join(dwl_folder, dwl_file)
    
    # Read dwelling file
    dwellings = pd.read_csv(dwl_path)
   
    # ESTIMATE BUILDINGS    
    buildings = dwellings_to_buildings(country, dwellings, repl_cost_file)
    
    # ADD  POPULATION
    population = pd.read_excel(pop_files[country][0], sheetname = pop_files[country][1])
    
    # Identify region (urban/rural/total)
    if dwl_path.find('urb') != -1:
        area = 'Urban'
    elif dwl_path.find('rur') != -1:
        area = 'Rural'
    else:
        area = 'Total'
        
    buildings = add_Population(country, area, population, dwellings)

    # ADD COORDINATES   
    buildings = add_centroids(buildings, country)
    
    # SAVE DATA
    save_as = os.path.join(bdg_folder, dwl_file.replace('dwellings', 'buildings'))
    buildings.to_csv(save_as, index=False)
    print '\n buildings saved in {}'.format(save_as)

# Estimate total exposure (Urban + Rural)
