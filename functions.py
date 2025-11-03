import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import scipy.stats as stats

'''functions to import data, create plots and calculate descriptive statistics'''

def import_station(file_path='', var=''):
    df = pd.read_csv(file_path)
    df_data = df[var]
    df_yr = df['YEAR']

    return df_data, df_yr

def import_gridded(file_path='', var=''):
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    fig = plt.figure()
    ax = fig.add_subplot(111)

def map(in_da, out_path='', out_name=''):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

def descriptive_stats(da):
    mean_var = np.mean(df)
    stdev_var = np.std(df)
    max_var = np.max(df)
    min_var = np.min(df)
    print(mean_var, stdev_var, max_var, min_var)

    return mean_var, stdev_var, max_var, min_var