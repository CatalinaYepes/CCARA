# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:13:36 2017

@author: catalinayepes
"""
import os
import pandas as pd
from select_files import select_files


def taxonomy_summary(folder, files_contain, summarise):
    
    # Read dwelling files in folder
    files = select_files(folder, contain= files_contain)
    
    # Create empty file for taxonomy summary
    taxo_summary = pd.DataFrame(columns={'Taxonomy'})
    
    for file_name in files:
        name = file_name[:-14]
        print name
        
        # Estimate total number of dwellings
        dwellings = pd.read_csv(os.path.join(folder, file_name))
        tot_dwl = dwellings[['Taxonomy', summarise]].groupby('Taxonomy').sum().reset_index()
        tot_dwl.rename(columns={summarise : name}, inplace=True)
        # Add data to taxonomy summary
        taxo_summary = pd.merge(taxo_summary, tot_dwl, how='outer', on=['Taxonomy'])
        taxo_summary.sort(columns=['Taxonomy'], inplace=True)
        
    return taxo_summary

#folder = '../dwellings_v0_Feb2017'
#files_contain = '-dwellings.csv'
#summarise = 'Dwellings'

folder = '../buildings_v0_Mar2017'
files_contain = '-buildings.csv'
summarise = 'Population'

summary = taxonomy_summary(folder, files_contain, summarise)

save_as = os.path.join(folder, summarise + '_Summary-all.csv')
summary.to_csv(save_as, index=False)
print '\n Summary saved in {}'.format(save_as)