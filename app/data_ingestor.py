import pandas as pd


class DataIngestor:
    """Class for ingesting and processing data from a CSV file.

    Attributes:
        sorted_averages (dict): Stores sorted averages for best5 and worst5.
        averages (dict): Stores averages for global mean.
        columns (list): List of columns used for mean_by_category.
        mean_by_category (dict): Stores mean values by category.
    """
    sorted_averages = {}  # for best5 and worst5
    averages = {}         # for global mean
    # for mean_by_category
    columns = ['LocationDesc', 'Data_Value', 'Stratification1', 'StratificationCategory1']
    mean_by_category = {}

    def __init__(self, csv_path: str):
        """Initialize the DataIngestor with a path to a CSV file.

        Args:
            csv_path (str): The path to the CSV file to be ingested.
        """
        pd.set_option('display.float_format', lambda x: '%.20f' % x)
        self.data = pd.read_csv(csv_path)
        self.questions_best_is_min = [
            'Percent of adults aged 18 years and older who have an overweight classification',
            'Percent of adults aged 18 years and older who have obesity',
            'Percent of adults who engage in no leisure-time physical activity',
            'Percent of adults who report consuming fruit less than one time daily',
            'Percent of adults who report consuming vegetables less than one time daily'
        ]
        self.questions_best_is_max = [
            'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic physical activity and engage in muscle-strengthening activities on 2 or more days a week',
            'Percent of adults who achieve at least 300 minutes a week of moderate-intensity aerobic physical activity or 150 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who engage in muscle-strengthening activities on 2 or more days a week',
        ]
        unique_questions = self.data['Question'].unique()

        self.rows_dict = {}
        self.rows_dict_for_category = {}
        for question in unique_questions:
            mask = self.data['Question'] == question
            self.rows_dict[question] = self.data[mask]
            self.rows_dict_for_category[question] = self.data[mask]
            some_rows = self.rows_dict_for_category[question]
            self.rows_dict_for_category[question] = some_rows[self.columns]
            rows = self.rows_dict[question]
            self.rows_dict[question] = rows[(rows['YearStart'] >= 2011) & (rows['YearEnd'] <= 2022)]
            self.averages[question] = self.rows_dict[question]
            self.rows_dict[question] = self.rows_dict[question].groupby('LocationDesc')['Data_Value'].mean().reset_index()       
