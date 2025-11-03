import matplotlib.pyplot as plt
import pandas as pd
import functions as fn

file_path = '/Users/averyrubins/data/ev228_data/era5_10mwind_1980-1989.nc'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = 'era5_10mwind.png'
data_var = 'si10'


da_10mwind = fn.import_gridded(file_path, var=data_var)
da_10mwind_timemn = da_10mwind.mean(dim='valid_time')

fn.map(da_10mwind_timemn, fig_path, fig_name)