# -*- coding: utf-8 -*-
"""
Estimate the total exposure as: total = urban + rural

Add population to exposure file proportional to the number of dwellings in each region
    
@author: catalinayepes
"""
import pandas as pd

def add_Population(country, area, population, data):
    '''
    :param country:
        country name or id to identify the files        
    :param area:
        'Urban', 'Rural' or 'Total'    
    :param population:
        ExcelFile with columns [id, Region, Urban, Rural, Total]
    :param data:
        DataFramen with at least columns [id, Dwellings]
    
    '''
    print '''\n Adding population in {}-{}\n'''.format(country, area)
    
    data['Population'] = 0
    for row, region in enumerate(population.id):  
#        print row, '-', region
        region_pop = population[area.capitalize()][row]
        
        # skip regions with zero or not population
        if region_pop == '-' or pd.isnull(region_pop) == True or region_pop == 0:
            continue

        dwl = data.Dwellings[data.id == region]
        
        # Check if there are regions not included in the exposure        
        error = 0
        if all(dwl.isnull()):
            error += error + region_pop
            print '''The region {} is not in the {} exposure'''.format(region, area)
            print 'However the population is ', region_pop
            continue
        
        tot_dwl = dwl.sum()    
        values =  region_pop * dwl / tot_dwl

        data.Population[data.id == region] = values
        data.Population[data.id == region] = values # !!!An error occur if I don't duplicate the operation!!!

#        print round(data.Population[data.id == region].sum(), 2)
#        print round(region_pop - error, 2)
        assert (round(data.Population[data.id == region].sum(), 2) == round(region_pop - error, 2)), 'error in #_population'        
                       
    data.Population = data.Population.round(1)
    data.Dwellings = data.Dwellings.round(1)
    
    print 'OK --> population added'
    return data


#%% Run file
#
#country = 'blz'
#dwl_path = '../dwellings_v0_Feb2017/blz-1_urb-dwellings.csv'
#area = 'Urban'
#data = pd.read_csv(dwl_path)
#pop_files = pop_files = pd.DataFrame({"blz":['../0_censos_res/pop-Belize-2010.xlsx', 'Regions-Pop_2010']})
#population = pd.read_excel(pop_files[country][0], sheetname = pop_files[country][1])
#data = add_Population(country, area, population, data)

