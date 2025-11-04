import matplotlib.pyplot as plt
import pandas as pd
import functions as fn

file_path = '/Users/averyrubins/data/ev228_data/era5_10mwind_1980-1989.nc'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = 'era5_10mwind.png'
data_var = 'si10'


da_10mwind = fn.import_gridded(file_path, var=data_var)
da_10mwind_timemn = da_10mwind.mean(dim='valid_time')


path = '/Users/averyrubins/data/ev228_data/'
filename = 'era5_10mwind_1980-1989.nc'
out_path = '/Users/averyrubins/data//ev228_data/'
out_name = 'era5_10mwind.png'

da = fn.import_gridded(file_path=path + filename, var='si10')
da_timemn = da.mean(dim='valid_time')
da_toplot = da_timemn - 273.15
plt.savefig(out_path + out_name, dpi=400) 
fn.map(da_toplot, out_path=out_path, out_name=out_name)