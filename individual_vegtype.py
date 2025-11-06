import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import xarray as xr
import functions as fn
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# importing data and calculating time mean
file_path = '/Users/averyrubins/data/ev228_data/era5_vegtype_2000-2025.nc'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = '2-era5_vegtype.png'
data_var = 'tvl' 
# tvh means type of high vegetation, and tvl means type of low vegetation
da_vegtype = fn.import_gridded(file_path, var=data_var)
da_vegtype_timemn = da_vegtype.mean(dim='valid_time')

# cartopy plot of vegetation type over time mean
# code adapted with help from Theo
fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection = ccrs.PlateCarree())
da_vegtype_timemn.plot.pcolormesh(
    x = 'longitude',
    y = 'latitude',
    ax = ax,
    transform = ccrs.PlateCarree(),
    cmap = mpl.cm.viridis,
    cbar_kwargs = {'label': 'Vegetation Type'},
    extend = 'both',
    add_colorbar=True
)
ax.set_extent([-108, -103, 35, 42], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND)
plt.show()

# need to write code to plot vegetation type from ERA5 data onto map, can use matplotlib website for instructions