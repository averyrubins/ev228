import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as fn 

# file path and variable names
file_path = '/Users/averyrubins/data/ev228_data/ASM00094998_temp_194804-202508.csv'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = 'ASM.png'
data_var = 'metANN'
time_var = 'YEAR'

# importing data and filtering out missing values, using importing station data function from functions.py
df_data, df_time = fn.import_station(file_path, data_var, time_var)
filter_data = df_data[df_data != 999.9]
filter_year = df_time[df_data != 999.9]

print(filter_data)
print(df_time) 

# calculating descriiptive statistics
mean_var = np.mean(filter_data)
stdev_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
print(mean_var, stdev_var, max_var, min_var)

# creating time series plot using timeseries function from functions.py
# need to change labels and title in functions.py to match data being plotted
fn.timeseries(filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name)

