import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import functions as fn

file_path = '/Users/averyrubins/data/ev228_data/SGM00061600_temp_189201-202508.csv'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = '4-SGM.png'
data_var = 'metANN'
time_var = 'YEAR'

df_data, df_time = fn.import_station(file_path, data_var, time_var)
filter_data = df_data[df_data != 999.9]
filter_year = df_time[df_data != 999.9]

print(filter_data)
print(df_time) 

mean_var = np.mean(filter_data)
stdev_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
print(mean_var, stdev_var, max_var, min_var)

fn.timeseries(filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name)