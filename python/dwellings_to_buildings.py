# -*- coding: utf-8 -*-
"""
@author: catalinayepes
"""
import pandas as pd

def dwellings_to_buildings(name, info, repl_cost_file):
    '''
    Function to convert the Dwellings into Buildings and the associated
    replacement cost, based on data specified in the excel file.
    
        dwl_file:
            csv file with columns ['id', 'Region', 'Taxonomy', 'Dwellings']
            
        repl_cost_file:
            Excel file with 3 sheets: 'dwl_to_bdg', 'dwl_area' and 'dwl_repl_cost'
    '''
    print ('... parsing Dwellings to Buildings for {} ...').format(name.capitalize())

    #Read Replacement cost file
    dwl_to_bdg = pd.read_excel(repl_cost_file, sheetname='dwl_to_bdg', skiprows= 1, index_col= 0)
    dwl_area = pd.read_excel(repl_cost_file, sheetname='dwl_area', skiprows= 1, index_col= 0)
    repl_cost = pd.read_excel(repl_cost_file, sheetname='dwl_repl_cost', skiprows= 1, index_col= 0)
    
    # Add columns to 'info' to add information
    info['Buildings'] = 0
    info['Tot_cost'] = 0
    info['Repl_cost_USD/bdg'] = 0
    info['No_of_storeys'] = 0
    info['Dwl_per_storey'] = 0
    info['Dwl_area_m2'] = 0

    for i, taxo in enumerate(info.Taxonomy):
        info.loc[i,'No_of_storeys'] = dwl_to_bdg.Number_of_storeys[taxo]
        info.loc[i,'Dwl_per_storey'] = dwl_to_bdg.Dwellings_per_storey[taxo]
        info.loc[i,'Dwl_area_m2'] = dwl_area.loc[taxo, name] 
        
        dwl_per_bdg = dwl_to_bdg.Dwellings_per_building[taxo]
        cost = repl_cost.loc[taxo, name] * info.loc[i,'Dwl_area_m2'] * dwl_per_bdg

        info.loc[i,'Buildings'] = round(info.loc[i,'Dwellings'] / dwl_per_bdg, 1)
        info.loc[i,'Repl_cost_USD/bdg'] = cost
        info.loc[i, 'Tot_cost'] = info.loc[i,'Buildings'] * info.loc[i,'Repl_cost_USD/bdg']
    
    return info
    
#dwl_file = '../dwellings_v0_Feb2017/brb-1-dwellings.csv'
#info = pd.read_csv(dwl_file)
#repl_cost_file = '../buildings_v0_Mar2017/Replacement_cost_v0 (1).xlsx'
#info = dwellings_to_buildings('brb', dwl_file, repl_cost_file)