# -*- coding: utf-8 -*-
"""
Distribute dwellings for Urban and Rural areas based on population data

@author: catalinayepes
"""

import pandas as pd
import numpy as np
    
def map_proportions(dwl, population, mapping):
    '''Map proportions based on population distribution.
        Assumption: Some taxonomies ONLY exist in urban areas
    '''
    area_dwl = pd.DataFrame(columns=['id', 'Region', 'Taxonomy', 'Dwellings', 'urban'])
    
    for row, region_id in enumerate(population.id):
        print region_id, population.Region[row]
        
        urban_fraction = population.urb_fraction.iloc[row]

        data = dwl[dwl.id == region_id]
        data = pd.merge(mapping, dwl[dwl.id == region_id], how='inner', on='Taxonomy')
        tot_dwl = data.Dwellings.sum()
        data['urban'] = 0 
        
        # only taxonomies in URBAN areas
        values_1 = data[data.only_urban == 1]
        values_1['urban'] = values_1.Dwellings
        
        # the other taxonomies (urban or rural areas)
        urb_dwl = tot_dwl * urban_fraction
        new_urb_fraction = (urb_dwl - values_1.urban.sum()) / (tot_dwl - values_1.urban.sum())
        
        values_2 = data[data.only_urban != 1] 
        values_2['urban'] = values_2.Dwellings * new_urb_fraction
        
        # check that the tot number of buildings and fractions are consistent       
        assert(round(data.Dwellings.sum(), 4) == round(values_1.Dwellings.sum() + values_2.Dwellings.sum(), 4)), 'Error when distributin buildings \n'

        if tot_dwl == 0:
            fraction = 0
        else:
            fraction = (values_1.urban.sum() + values_2.urban.sum()) / tot_dwl

        assert(round(fraction, 5) == round(urban_fraction, 5)), 'Different fractions \n'
        
        # add data to dataframe        
        area_dwl = area_dwl.append(values_1[['id', 'Region', 'Taxonomy', 'Dwellings', 'urban']])
        area_dwl = area_dwl.append(values_2[['id', 'Region', 'Taxonomy', 'Dwellings', 'urban']])
        
    area_dwl['rural'] = area_dwl['Dwellings'] - area_dwl['urban']
    print '''OK ---> Dwelling fractions for Urban/Rural areas have been computed.
    Total dwellings = {}
    Urban dwellings = {}
    Rural dwellings = {}'''.format(round(dwl.Dwellings.sum(),1), round(area_dwl.urban.sum(),1), round(area_dwl.rural.sum(),1))
    
    
    return area_dwl


def save_by_area(dist_dwl, dwl_file):    
    for area in ['urban', 'rural']:
        data = dist_dwl[['id', 'Region', 'Taxonomy', area]]
        data.rename(columns={area:'Dwellings'}, inplace=True)
        
        data = data[data.Dwellings != 0]
        data.Dwellings = data.Dwellings.round(1)
        data.reset_index(inplace= True, drop=True)
        
        save_as = dwl_file[:-14] + '_' + area[:3] + '-dwellings.csv'
        data.to_csv(save_as, index=False)            
        print '\n {} information exported as {}\n'.format(area, save_as)
    

# %%

# Population of BELIZE
dwl_file = '../dwellings_v0_Feb2017/total_dwellings/blz-1-dwellings.csv'
pop_file = '../0_censos_res/pop-Belize-2010.xlsx'
pop_sheet = 'Regions-Pop_2010'

## Population of GUATEMALA
#dwl_file = '../dwellings_v0_Feb2017/total_dwellings/gtm-1-dwellings.csv'
#pop_file = '../0_censos_res/pop-Guatemala-2002.xlsx'
#pop_sheet = 'Municipio'

taxonomy_file = '../dwellings_v0_Feb2017/UrbanRural-dwl.csv'

dwl = pd.read_csv(dwl_file)
mapping = pd.read_csv(taxonomy_file)

population = pd.read_excel(pop_file, sheetname= pop_sheet)
population['urb_fraction'] = population.Urban / population.Total
population.replace(np.inf, 0, inplace=True) # To avoid errors when regions have no population

dist_dwl = map_proportions(dwl, population, mapping)
save_by_area(dist_dwl, dwl_file)