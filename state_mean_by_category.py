import pandas as pd
import os
import json


def extract_state_data(state, data):
    result = {state: {}}
    for key, value in data.items():
        key_state, category, subcategory = key
        if key_state == state:
            result[state][(category, subcategory)] = value
    return result

def convert_keys_to_strings(data):
    result = {}
    for state, categories in data.items():
        new_categories = {}
        for key, value in categories.items():
            new_key = str(key)
            new_categories[new_key] = value
        result[state] = new_categories
    return result




def state_mean_by_category(Question,State):


 from app import webserver
 data = webserver.data_ingestor.rows_dict_for_category[Question]
 grouped = data.groupby(['LocationDesc', 'StratificationCategory1', 'Stratification1'])
 averages = grouped['Data_Value'].mean()
 
#pd.set_option('display.float_format', lambda x: '%.20f' % x)
#data = pd.read_csv("./nutrition_activity_obesity_usa_subset.csv")

#mask = data['Question'] == 'Percent of adults aged 18 years and older who have an overweight classification'
#rows = data[mask]

#columns = ['LocationDesc', 'Data_Value','Stratification1', 'StratificationCategory1']
#grouped = rows[columns]

#grouped = grouped.groupby(['LocationDesc', 'StratificationCategory1', 'Stratification1'])
#averages = grouped['Data_Value'].mean()

# averages_dict = averages.to_dict()
# averages_dict_str_keys = {str(key): value for key, value in averages_dict.items()}

 data2 = extract_state_data(State, averages)
 new_data = convert_keys_to_strings(data2)
 return new_data

# with open('averages.json', 'w') as f:
#    json.dump(new_data , f) 
  
