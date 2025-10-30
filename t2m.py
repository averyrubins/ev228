import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

ds=xr.open_dataset('/Users/averyrubins/data/ev228_data/era5_2mtemp.nc')
da=ds['t2m']
print(da)

da.plot(); plt.show()