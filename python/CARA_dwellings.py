# -*- coding: utf-8 -*-
"""
MODEL FOR CENTRAL AMERICA

Parse number of dwellings per buildings class based on census data and mapping schemes.

Make sure the data is stored in an excel file (.xlsx) with at least:
 i)  A sheet with census data for a given administrative level
 ii) A sheet with the mapping scheme
      NOTE: The maping scheme must perfectly match the variables used in the census.
      Check the exmaple data given in "example-data.xlsx"
      
The user can parse information based on two or three variables: 
  var1: in the rows (e.g. floor material)
  var2: in the first column (e.g. wall material)
  var3: in the second column (e.g. type of dwelling)
    
@author: catalinayepes
"""
import os
from parsers_exposure import classes

folder = '/Users/catalinayepes/Google Drive/10_CARA/'
save_folder_name = os.path.join(folder, 'dwellings_v0_Feb2017')

## -----------------------------------------------------------------------------
## PANAMA [PAN]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-Panama-2010.xlsx')    
#num_var = 'three' # Number of variables in the data (small letter)
#country = classes.ReadCensus('pan', file_location, num_var)
#
#mapping_sheet = 'mapping_3var_urb' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, row_var3=12, print_vars=False)
#parse_sheets = 'Corregimiento_Urban'
#admin_level = '3_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_3var_rur' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, row_var3=12, print_vars=False)
#parse_sheets = 'Corregimiento_Rural'
#admin_level = '3_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)

## -----------------------------------------------------------------------------
## NICARAGUA [NIC]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-Nicaragua-2005.xlsx')      
#num_var = 'two' # Number of variables in the data (small letter)
#country = classes.ReadCensus('nic', file_location, num_var)
#
#mapping_sheet = 'mapping_2var_urb' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Municipio_urban'
#admin_level = '2_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_2var_rur' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Municipio_rural'
#admin_level = '2_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)


## -----------------------------------------------------------------------------
## HONDURAS [HND]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-Honduras-2013.xlsx')    
#num_var = 'two' # Number of variables in the data (small letter)
#country = classes.ReadCensus('hnd', file_location, num_var)
#
#mapping_sheet = 'mapping_2var_urb' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Municipio_Urban'
#admin_level = '2_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_2var_rur' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Municipio_Rural'
#admin_level = '2_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)

#mapping_sheet = 'mapping_scheme_2var' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'ind&com'
#admin_level = '2_ind&com'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)

## -----------------------------------------------------------------------------
## EL SALVADOR [SLV]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-Salvador-2007.xlsx')     
#num_var = 'three' # Number of variables in the data (small letter)
#country = classes.ReadCensus('slv', file_location, num_var)
#
#mapping_sheet = 'mapping_3var_urb' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, row_var3=13, print_vars=False)
#parse_sheets = 'Municipio_Urban'
#admin_level = '2_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_3var_rur' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, row_var3=13, print_vars=False)
#parse_sheets = 'Municipio_Rural'
#admin_level = '2_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)

#
## -----------------------------------------------------------------------------
## REP. DOMINICANA [DOM]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-RepDominicana-2010.xlsx')     
#num_var = 'three' # Number of variables in the data (small letter)
#country = classes.ReadCensus('dom', file_location, num_var)
#
#mapping_sheet = 'mapping_urban' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, row_var3=11, print_vars=False)
#parse_sheets = 'Distrito_urban'
#admin_level = '4_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_rural' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, row_var3=11, print_vars=False)
#parse_sheets = 'Distrito_rural'
#admin_level = '4_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#
## -----------------------------------------------------------------------------
## JAMAICA [JAM]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-Jamaica-2011.xlsx')     
#num_var = 'two' # Number of variables in the data (small letter)
#country = classes.ReadCensus('jam', file_location, num_var)
#
#mapping_sheet = 'mapping_urban' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Parish_urban'
#admin_level = '1_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_rural' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Parish_rural'
#admin_level = '1_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#
## -----------------------------------------------------------------------------
## TRINIDAD AND TOBAGO [TTO]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-TTO-2000.xlsx')     
#num_var = 'two' # Number of variables in the data (small letter)
#country = classes.ReadCensus('tto', file_location, num_var)
#
#mapping_sheet = 'mapping_urban' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Municipality_urban'
#admin_level = '1_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_rural' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Municipality_rural'
#admin_level = '1_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#
## -----------------------------------------------------------------------------
## BARBADOS [BRB]
## -----------------------------------------------------------------------------
#file_location = os.path.join(folder, '0_censos_res/Censo-Barbados-2010.xlsx')     
#num_var = 'two' # Number of variables in the data (small letter)
#country = classes.ReadCensus('brb', file_location, num_var)
#
#mapping_sheet = 'mapping' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=False)
#parse_sheets = 'Parish'
#admin_level = '1'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#
# -----------------------------------------------------------------------------
# BELIZE [BLZ]
# -----------------------------------------------------------------------------
file_location = os.path.join(folder, '0_censos_res/Censo-Belize-2010.xlsx')     
num_var = 'two' # Number of variables in the data (small letter)
country = classes.ReadCensus('blz', file_location, num_var)

mapping_sheet = 'mapping' # name or location of mapping matrix
country.mapping_matrix(mapping_sheet, row_var1=2, print_vars=True)
parse_sheets = 'Regions'
admin_level = '1'
country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)


## ------------------------------
## GUATEMALA [GTM]
## ------------------------------
#file_location = os.path.join(folder, '0_censos_res/Guatemala-Censo-2002.xlsx')     
#nickname = 'gtm'  # to add to the saved file
#num_var = 'one' # Number of variables in the data (small letter)
#country = classes.ReadCensus(nickname, file_location, num_var)
#
#mapping_sheet = 'mapping_1var_total' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=1, print_vars=False)
#parse_sheets = 'Municipio_Total' # name or location of sheet to parse (example: 0 or 'Sheet1')
#admin_level = '2'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
## ------------------------------
## CUBA [CUB]
## ------------------------------
#file_location = os.path.join(folder, '0_censos_res/Cuba-Municipios-2012.xlsx')     
#nickname = 'cub'  # to add to the saved file
#num_var = 'one' # Number of variables in the data (small letter)
#country = classes.ReadCensus(nickname, file_location, num_var)
#
#mapping_sheet = 'mapping_1var_urb' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=1, print_vars=True)
#parse_sheets = 'Municipio_Urban' # name or location of sheet to parse (example: 0 or 'Sheet1')
#admin_level = '2_urb'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
#
#mapping_sheet = 'mapping_1var_rur' # name or location of mapping matrix
#country.mapping_matrix(mapping_sheet, row_var1=1, print_vars=True)
#parse_sheets = 'Municipio_Rural' # name or location of sheet to parse (example: 0 or 'Sheet1')
#admin_level = '2_rur'
#country.parse_info(parse_sheets, admin_level, save_folder_name, save_regions=False, save_data=True)
