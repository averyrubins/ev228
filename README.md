# ev228
analysis of environmental data - individual

# individiual data story
project summary: I am studying vegetation type in the Front Range compared to mean 2-meter temperature throughout the region, to hypothesize how vegetation impacts wildfire likelihood.

code index and workflows: 

functions.py contains functions to import .csv and .nc files, as well as create figures from timeseries and gridded data. I need to change the file name/path and title in this index whenever I create a new figure. I did not use generative AI on this code.

individual_vegtype.py is where I generated a map of the Southern Rockies and plotted the ERA5 type of vegetation data over it. First I imported the file and combined the two types of vegetation (low and high) into one variable. I created the basemap using cartopy and created a custom colorbar to represent each vegetation type. I used generative AI to help choose colors for the different vegetation types, in order to find colors that accurately represent vegetation while being colorblind- accessible. I then refined the map using cartopy and matplotlib features. 

individual_2mtemp.py is where I generated a map of the Southern Rockies and plotted the ERA5 2m temperature data over it. I followed a similar workflow to the vegetation type file, but after importing the file I calculated the time mean. I did not have to create custom colors. I did not use generative AI on this code.
