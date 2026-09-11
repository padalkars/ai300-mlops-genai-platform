import pandas as pd
import numpy as np
from collections import Counter
from pathlib import Path


class Statistics:
    def __init__(self, data):
        self.data = data
        self.continuous_vars = []
        self.categorical_vars = []

    def missing_value_analysis(self):
        """Get the count of missing values in the data.
        
        Input:
        None

        Return:
        missing_values_df:- A data frame representing the counts of missing values
        
        """
        missing_values_df = pd.DataFrame(self.data.isnull().sum())
        
        missing_values_df = missing_values_df.reset_index()
        missing_values_df = missing_values_df.rename(columns={0:"Missing_Value_Count",
                                                              "index": "Features"})
        missing_values_df["Missing_Value_Percentage"] = round(missing_values_df["Missing_Value_Count"]*100/self.data.shape[0], 2)

        return missing_values_df

    def get_data_tyes(self):
        data_types = pd.DataFrame(self.data.dtypes)
        data_types = data_types.reset_index()
        data_types = data_types.rename(columns={0:"Data_Types", "index":"Features"})

        return data_types

    def get_descriptive_stats(self, cont_vars, cat_vars):
        """
        Input:
        cont_vars:- A list of continuous variables in the data.
        cat_vars:- A list of categorical variables in the data.

        Return:
        descriptive_stats:- Mean, Q1, Q2(Median), Q3, Number of categories
        """
        category_counts = [self.data[var].nunique() for var in cat_vars]

        descriptive_stats = self.data[cont_vars].describe().T.reset_index()
        descriptive_stats = descriptive_stats.rename(columns={"index":"Features"})

        category_counts_df = pd.DataFrame({"Features":cat_vars, "Category_Counts":category_counts})

        result_stats = pd.concat([descriptive_stats, category_counts_df], axis=0)

        return result_stats


    def get_frequency(self, cat_var):
        frequency_df = self.data.groupby(cat_var).apply(lambda df:df.shape[0])
        frequency_df = pd.DataFrame(frequency_df)
        frequency_df = frequency_df.rename(columns={0:"Counts"})
        frequency_df = frequency_df.reset_index()
        frequency_df = frequency_df.rename(columns={0:"Categories"})

        # Sort in descending order fo frequency counts
        frequency_df = frequency_df.sort_values(by="Counts", ascending=False)

        # Compute the percentage distribution of each category
        frequency_df["%_Distribution"] = frequency_df["Counts"]*100/self.data.shape[0]

        return frequency_df

    def get_stats(self):
        missing_values_stats = self.missing_value_analysis()
        data_types = self.get_data_tyes()

        self.continuous_vars = data_types.loc[(data_types["Data_Types"]=="int64") | (data_types["Data_Types"]=="float64"), 
                                         "Features"].tolist()

        self.categorical_vars = data_types.loc[data_types["Data_Types"]=="object", "Features"].tolist()

        descriptive_stats = self.get_descriptive_stats(cont_vars=self.continuous_vars, cat_vars=self.categorical_vars)

        overall_stats = pd.merge(missing_values_stats, data_types, on="Features", how="inner")
        overall_stats = pd.merge(overall_stats, descriptive_stats, on="Features", how="left")

        return overall_stats

