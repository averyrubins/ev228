import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import functions as fn

#file path to import data

file_path = '/Users/averyrubins/data/ev228_data/era5_vegtype_2000-2025.nc'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = 'era5_vegtype.png'
data_var = 'tvh' 
# tvh means type of high vegetation
# data_var = 'tvl' '''tvl means type of low vegetation'''

# importing data and calculate time mean'''

da_vegtype = fn.import_gridded(file_path, var=data_var)
da_vegtype_timemn = da_vegtype.mean(dim='valid_time')

#create map of high vegetation type averaged per year

fn.map(da_vegtype_timemn, fig_path, fig_name)