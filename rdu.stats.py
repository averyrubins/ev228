import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import linregress

import functions as fn

# file path and variable names
file_path = '/Users/averyrubins/data/ev228_data/KRDU_temp_188708-202508.csv'
fig_path = '/Users/averyrubins/data/ev228_data/'
fig_name = 'KRDU.png'
data_var = 'metANN'
time_var = 'YEAR'

# importing data and filtering out missing values, using importing station data function from functions.py
df_data, df_time = fn.import_station(file_path, data_var, time_var)
filter_data = df_data[df_data != 999.9]
filter_year = df_time[df_data != 999.9]

# calculating descriptive statistics
slope, y_int, r_value, p_value, std_err = stats.linregress(filter_year, filter_data)
print(slope, y_int, r_value, p_value, std_err)

# creating timeseries plot with linear regression line
plt.scatter(filter_year, filter_data, color='hotpink', label='Annual Mean Temperature')
plt.plot(filter_year, y_int + slope * filter_year, color='blue', linewidth=2.5, label='Linear Fit')
plt.xlabel('Years')
plt.xlim(1887, 2026)
plt.ylabel('Annual Mean Temperature (°C)')
plt.title('Raleigh-Durham International Airport Annual Mean Temperature 1887-2025')
plt.legend()
plt.show()