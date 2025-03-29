import pandas as pd
import os
import json



def state_mean(Question,State):


# Read the CSV file
 #from app import webserver
 #df = webserver.data_ingestor.data

# Filter rows for the specific question
# mask = df['Question'] == Question

 #rows = df[mask]
 #mask = rows['LocationDesc'] == State
 #rows = rows[mask]

# Further filter rows based on the year range
 #filtered_df = rows[(rows['YearStart'] >= 2011) & (rows['YearEnd'] <= 2022)]

# Calculate the mean Data_Value for LocationDesc
 #state_averages = filtered_df.groupby('LocationDesc')['Data_Value'].mean().reset_index()
  
 from app import webserver
 rows = webserver.data_ingestor.rows_dict[Question]
 mask = rows['LocationDesc'] == State 
 rows = rows[mask]
  
# Convert the DataFrame to a dictionary
 averages_dict = rows.set_index('LocationDesc')['Data_Value'].to_dict()

 return averages_dict









