import pandas as pd
import os
import json




def mean_by_category(Question):




#pd.set_option('display.float_format', lambda x: '%.20f' % x)
#data = pd.read_csv("./nutrition_activity_obesity_usa_subset.csv")

#mask = data['Question'] == 'Percent of adults aged 18 years and older who have an overweight classification'
#rows = data[mask]

# Assuming df is your DataFrame
#columns = ['LocationDesc', 'Data_Value','Stratification1', 'StratificationCategory1']
#grouped = rows[columns]


 from app import webserver
 data = webserver.data_ingestor.rows_dict_for_category[Question]
 grouped = data.groupby(['LocationDesc', 'StratificationCategory1', 'Stratification1'])
 averages = grouped['Data_Value'].mean()

 #Convert to dictionary
 averages_dict = averages.to_dict()

 averages_dict_str_keys = {str(key): value for key, value in averages_dict.items()}

#with open('averages.json', 'w') as f:
 #   json.dump(averages_dict_str_keys, f)
 return averages_dict_str_keys 
  
