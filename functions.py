import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import scipy.stats as stats

def xarray_import_data(file_path, file_name, column_index):
    ds = xr.open_dataset(file_path + file_name)
    da = ds[column_index]
    print(da)
    return da

def descriptive_stats(da):
    dict_stat = {
        'mean' : da.mean(),
        'maximum' : da.max(),
        'minimum' : da.min(),
        'standard deviation' : da.std(),
        'variance' : da.var()
        }
    return dict_stat