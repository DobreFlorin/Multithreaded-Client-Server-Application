"""Module for calculating the difference between state values and mean values."""
import pandas as pd
import os
import json



def state_diff_from_mean(question, state):
    """
    Calculate the difference between the mean value and a specific state's value.

    Args:
        question (str): The question/measurement to analyze
        state (str): The state to calculate the difference for

    Returns:
        dict: Dictionary containing the state and its difference from the mean
    """
    from app import webserver

    rows = webserver.data_ingestor.averages[question]
    mean_value = rows['Data_Value'].mean()
    
    averages = webserver.data_ingestor.rows_dict[question]
    state_value = averages.loc[averages['LocationDesc'] == state, 'Data_Value'].values[0]
    
    state_value = mean_value - state_value
    
    result_dict = {state: state_value}
    return result_dict
