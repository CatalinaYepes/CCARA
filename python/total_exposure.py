# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:39:13 2017

@author: catalinayepes
"""
import pandas as pd
import os
from select_files import select_files

def compute_total(country, bdg_folder, save_folder, flag='Total'):
    df_files = select_files(bdg_folder, contain= country, end='.csv')
    
    if isinstance(df_files, str):
       df_files = [df_files]
       
    for file_name in df_files:
        print file_name
        if file_name.find('urb') != -1:
            urban = pd.read_csv(os.path.join(bdg_folder, file_name))
        elif file_name.find('rur') != -1:
            rural = pd.read_csv(os.path.join(bdg_folder, file_name))
        elif file_name.find('tot') != -1:
            print 'Replacing total existing file'
        else:
            total = pd.read_csv(os.path.join(bdg_folder, file_name))

    save_as = file_name[:5] + '_tot-buildings.csv'
    
    try:
        urban
        print ('\n... computing total exposure {} ...').format(country)
        total = pd.concat([urban, rural])
        assert (round(urban.Buildings.sum() + rural.Buildings.sum(),4) == round(total.Buildings.sum(),4)), 'error in #_buildings = Urban & Rural'
    except NameError:
        print 'Total exposure provided. Replacing existing one'

    # Compute the total exposure: total = urban + rural and re-arrange columns      
    if flag == 'Total':
        # For total exposure
        total = total.groupby(['id', 'Region', 'Taxonomy', 'Repl_cost_USD/bdg', 'lon', 'lat'], as_index=False).sum()
        total = total[['lon', 'lat', 'id', 'Region', 'Taxonomy', 'Dwellings', 'Buildings', 'Population', 'Tot_cost']] 
    elif flag == 'Maps':
        # For plots in QGIS
        total = total.groupby(['id', 'Region', 'lon', 'lat'], as_index=False).sum()
        total = total[['lon', 'lat', 'id', 'Region', 'Dwellings', 'Buildings', 'Population', 'Tot_cost']]
    
    total.to_csv(os.path.join(save_folder, save_as), index=False) 
    print 'Total buildings saved for ', country
    
    return total
#%% to test
countries = ['blz', 'brb', 'cub', 'dom', 'gtm', 'hnd', 'jam', 'nic', 'pan', 'slv', 'tto']
#countries = 'blz'

bdg_folder = '../buildings_v0_Mar2017'
maps_folder = '../1_maps/exposure_maps_v0/'

for country in countries: 
    bdg_maps = compute_total(country, bdg_folder, maps_folder, flag='Maps')
    
    bdg_total = compute_total(country, bdg_folder, bdg_folder, flag='Total')
