from sklearn.model_selection import train_test_split
import pandas as pd

class Splitting:

    def __init__(self, raw_data:pd.DataFrame, target_var:str, independent_vars:list):
        self.raw_data = raw_data
        self.target_var = target_var
        self.independent_vars = independent_vars

    def data_split(self, test_size:float):
        """Split the data into train and test sets given the test_size

        Input:
        test_size:- Percentage(0-1) of records in the test set
        
        """
        X = self.raw_data[self.independent_vars]
        y = self.raw_data[self.target_var]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        return X_train, y_train, X_test, y_test
