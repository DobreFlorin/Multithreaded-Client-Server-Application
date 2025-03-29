import pandas as pd
import os
import json


def global_mean(Question):
 


# Set display option to show all decimals
 #pd.set_option('display.float_format', lambda x: '%.20f' % x)

# from app import webserver
 #df = webserver.data_ingestor.data

# Filter rows for the specific question
# mask = df['Question'] == Question
 #rows = df[mask]

# Further filter rows based on the year range

 #filtered_df = rows[(rows['YearStart'] >= 2011) & (rows['YearEnd'] <= 2022)]


# Computing the mean
 #mean_value = filtered_df['Data_Value'].mean()
 from app import webserver
 filtered_df = webserver.data_ingestor.averages[Question]
 mean_value = filtered_df['Data_Value'].mean()


# Create a dictionary with the value
 global_mean_dict = {'global_mean': mean_value}


 return global_mean_dict 



