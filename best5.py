import pandas as pd
import os
import json




def is_string_in_list(input_string, list_to_check):
    if input_string in list_to_check:
        return True
    else:
        return False

def best5(Question):

# Set display option to show all decimals
 #pd.set_option('display.float_format', lambda x: '%.20f' % x)

# Read the CSV file
 #from app import webserver 
 #df = webserver.data_ingestor.data

# Filter rows for the specific question
 #mask = df['Question'] == Question
 #rows = df[mask]

# Further filter rows based on the year range
 #filtered_df = rows[(rows['YearStart'] >= 2011) & (rows['YearEnd'] <= 2022)]

# Calculate the mean Data_Value for each LocationDesc
 #state_averages = filtered_df.groupby('LocationDesc')['Data_Value'].mean().reset_index()

# Sort the averages in ascending order
 from app import webserver
 averages = webserver.data_ingestor.rows_dict[Question]
 webserver.data_ingestor.sorted_averages[Question] = averages.sort_values(by='Data_Value')

# Select the last 5 rows and convert to a dictionary
 if is_string_in_list(Question, webserver.data_ingestor.questions_best_is_max):
  bottom_five_dict = webserver.data_ingestor.sorted_averages[Question].tail(5).set_index('LocationDesc')['Data_Value'].to_dict()
  bottom_five_dict = {k: bottom_five_dict[k] for k in reversed(list(bottom_five_dict.keys()))}
 else:
  bottom_five_dict = webserver.data_ingestor.sorted_averages[Question].head(5).set_index('LocationDesc')['Data_Value'].to_dict() 

 return bottom_five_dict
