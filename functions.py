import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import scipy.stats as stats

'''functions to import data, create plots and calculate descriptive statistics'''

def import_station(file_path='', var='', time_var=''):
    df = pd.read_csv(file_path)
    df_data = df[var]
    df_time = df[time_var]

    return df_data, df_time

def import_gridded(file_path='', var=''):
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color='#dc6b2b', linewidth=2.5)
    plt.xlabel('years')
    plt.xlim(1892, 2025)
    plt.ylabel('monthly temperature (deg C)')
    plt.title('Saint-Louis Airport, Senegal 1892-2025')
    plt.savefig(out_path + out_name, dpi=400)


def map(in_da, out_path='', out_name=''):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    path = '/Users/averyrubins/data/ev228_data/'
    filename = 'era5_10mwind_1980-1989.nc'
    out_path = '/Users/averyrubins/data//ev228_data/'
    out_filename = 'era5.png'

    da = import_gridded(file_path=path + filename, var='si10')
    da_timemn = da.mean(dim='valid_time')
    da_toplot = da_timemn - 273.15
    map(da_toplot, out_path=out_path, out_name=out_filename)
    plt.savefig(out_path + out_name, dpi=400) 

def descriptive_stats(da):
    mean_var = np.mean(df)
    stdev_var = np.std(df)
    max_var = np.max(df)
    min_var = np.min(df)
    print(mean_var, stdev_var, max_var, min_var)

    return mean_var, stdev_var, max_var, min_var