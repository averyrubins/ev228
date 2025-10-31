import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import scipy.stats as stats
import functions as fn

file_path = '/Users/averyrubins/data/ev228_data/'
file_name = 'era5_2mtemp.nc'
column_index = 't2m'

ds_2mtemp = fn.xarray_import_data('/Users/averyrubins/data/ev228_data/', 'era5_2mtemp.nc', 't2m')
print(ds_2mtemp)

stats_2mtemp = fn.descriptive_stats(ds_2mtemp)
print(stats_2mtemp)