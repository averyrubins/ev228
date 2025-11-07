import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap, BoundaryNorm
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
# code adapted from https://cartopy.readthedocs.io/stable/reference/projections.html#cartopy-projections with help from Theo
fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection = ccrs.PlateCarree())
da_vegtype_timemn.plot.pcolormesh(
    x = 'longitude',
    y = 'latitude',
    ax = ax,
    transform = ccrs.PlateCarree(),
# create discrete color bar assigned to specific values
# code adapted from https://gis.stackexchange.com/questions/444791/discrete-colours-in-geopandas-map 
    cmap = mpl.colors.ListedColormap(
# set colors with a list, each color corresponds to a veg type value
# for colors that don't correspond to a veg type value, set color to 'gray'
        colors=["purple", "darkorange", "gray", "gray", "gray", "gray", "orange", "gray", "green", "fuchsia", "moccasin", "gray", "papayawhip", "gray", "gray", "springgreen", "white", "gray", "gray"]
        # cbar_kwargs = {'label': 'Vegetation Type'},
        # extend = 'both',
        # add_colorbar=True,
    ))
# setting map extent
ax.set_extent([-114, -101, 34, 46], crs=ccrs.PlateCarree())
# adding map features through cartopy.cfeature
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.STATES, edgecolor='black', linewidth=0.5)
ax.add_feature(cfeature.RIVERS, facecolor='blue', linewidth=1)

plt.show()

# need to write code to plot vegetation type from ERA5 data onto map, can use matplotlib website for instructions