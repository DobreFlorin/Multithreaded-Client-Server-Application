import pandas as pd
import os
import json


def diff_from_mean(Question):
#pd.set_option('display.float_format', lambda x: '%.20f' % x)
#df = pd.read_csv("./nutrition_activity_obesity_usa_subset.csv")
#mask = df['Question'] == 'Percent of adults aged 18 years and older who have an overweight classification'

#rows = df[mask]
#filtered_df = rows[(rows['YearStart'] >= 2011) & (rows['YearEnd'] <= 2022)]
#mean_value = filtered_df['Data_Value'].mean()

#state_averages = filtered_df.groupby('LocationDesc')['Data_Value'].mean().reset_index()
 
#state_averages['Difference'] = mean_value - state_averages['Data_Value']

# Convert DataFrame to dictionary

#result = state_averages.set_index('LocationDesc')['Difference'].to_dict()
#print(result)
 from app import webserver
 rows = webserver.data_ingestor.averages[Question]
 mean_value = rows['Data_Value'].mean()
 
 averages = webserver.data_ingestor.rows_dict[Question]
 averages['Difference'] = mean_value - averages['Data_Value']
  
 #Convert DataFrame to dictionary

 result = averages.set_index('LocationDesc')['Difference'].to_dict()

 return result

 
 
 
 

