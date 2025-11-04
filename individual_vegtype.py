import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import functions as fn
from mpl_toolkits.basemap import Basemap

# code adapted from https://matplotlib.org/basemap/stable/users/mill.html 
# change latitude and longitude, llcrnrlat means lower left corner latitute
m = Basemap(projection='mill',llcrnrlat=34,urcrnrlat=42,\
            llcrnrlon=-102,urcrnrlon=-108,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua') 
plt.title("Miller Cylindrical Projection")
plt.show()
# sys.stop()

# need to write code to plot vegetation type from ERA5 data onto map, can use matplotlib website for instructions

#file path to import data

file_path = '/Users/averyrubins/data/ev228_data/era5_vegtype_2000-2025.nc'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = '2-era5_vegtype.png'
data_var = 'tvl' 
# tvh means type of high vegetation, and tvl means type of low vegetation

# importing data and calculate time mean
da_vegtype = fn.import_gridded(file_path, var=data_var)
da_vegtype_timemn = da_vegtype.mean(dim='valid_time')

#create map of high vegetation type averaged per year
fn.map(da_vegtype_timemn, fig_path, fig_name)