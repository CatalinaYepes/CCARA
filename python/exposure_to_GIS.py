# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:36:36 2017

@author: catalinayepes
"""

import os
from parsers_shapefiles import join_to_shape
from select_files import select_files

countries = ['blz', 'brb', 'cub', 'dom', 'gtm', 'hnd', 'jam', 'nic', 'pan', 'slv', 'tto']
#countries = ['blz']

# Data
bdg_folder = '../1_maps/exposure_maps_v0/'
join_data_by = 'id'
cols = ['Buildings', 'Tot_cost', 'Population']

# Shape files
shape_file_folder = '../1_maps/clean_shapes/'
join_shape_by = 'ID_CENSO'   # A check should be added in case the join fields have differente type (int, float or str) 

for country in countries:
    select_data = select_files(bdg_folder, contain= country, end='_tot-buildings.csv')
    data_file = os.path.join(bdg_folder, select_data)
        
    level = select_data[4:5]
    shape_file = os.path.join(shape_file_folder, '{}-l{}.shp'.format(country, level))

    output_file = os.path.join(bdg_folder, '{}-l{}-exposure'.format(country, level))
    
    join_to_shape.join_to_shape(shape_file, data_file, join_shape_by, join_data_by, columns= cols, save_as= output_file)
