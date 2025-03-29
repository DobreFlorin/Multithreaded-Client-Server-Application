import pandas as pd
import os
import json


def states_mean(Question):
# Set display option to show all decimals
# pd.set_option('display.float_format', lambda x: '%.20f' % x)

# Read the CSV file
 #from app import webserver
# df = webserver.data_ingestor.data

# Filter rows for the specific question
 #mask = df['Question'] == 'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)'

 #rows = df[mask]

# Further filter rows based on the year range
# filtered_df = rows[(rows['YearStart'] >= 2011) & (rows['YearEnd'] <= 2022)]

# Calculate the mean Data_Value for each LocationDesc
# state_averages = filtered_df.groupby('LocationDesc')['Data_Value'].mean().reset_index()

# Sort the averages in ascending order
 from app import webserver
 sorted_averages = webserver.data_ingestor.rows_dict[Question].sort_values(by='Data_Value')

# Convert the DataFrame to a dictionary
 averages_dict = sorted_averages.set_index('LocationDesc')['Data_Value'].to_dict()
 
 return averages_dict
 




