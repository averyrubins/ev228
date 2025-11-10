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

file_path = '/Users/averyrubins/data/ev228_data/era5_t2m_2000-2025.nc'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = 'era5_t2m.png'
data_var = 't2m'

# importing data and calculating time mean
da_t2m = fn.import_gridded(file_path, var=data_var)
da_t2m_timemn = da_t2m.mean(dim='valid_time')

out_path = file_path
out_name = fig_name

# creating map of 2m temperature time mean with functions.py
fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection = ccrs.PlateCarree())
da_t2m_timemn.plot.pcolormesh(
    x = 'longitude',
    y = 'latitude',
    ax = ax,
    transform = ccrs.PlateCarree(),
)
    # setting map extent
ax.set_extent([-110, -101, 34, 44], crs=ccrs.PlateCarree())
# adding map features through cartopy.cfeature
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.STATES, edgecolor='black', linewidth=0.5)
ax.add_feature(cfeature.RIVERS, facecolor='blue', linewidth=1)

plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('2m temperature in Southern Rocky Mountains, 2000-2025 mean')
plt.show()

# plt.savefig(out_path + out_name, dpi=400) 