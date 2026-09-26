
from evaluate import Evaluate
import pandas as pd
from modelling import Modeling
from sklearn.model_selection import StratifiedKFold as SKF
from pathlib import Path

class CrossValidation:

    def __init__(self, target_var:str, independent_vars:list, train_data:pd.DataFrame, algo_object):
        """
        Input:
        train_data:- The training data used for cross validation
        algo_object:- The object of the training algorithm class
1
        """
        self.train_data = train_data
        self.algo_obj = algo_object
        self.target_var = target_var
        self.independent_vars = independent_vars

    def training(self, X_train, y_train, X_test, y_test, features):
        """
        Input:
        X_train:-
        y_train:-
        X_test :-
        y_test:-
        features:-

        Return:
        results:- A dataframe comprising of evaluation metrics for the train and test set
        """
        modelling_instance = Modeling(X_train, y_train, X_test, y_test, ml_algo_obj=self.algo_obj)
        trained_model, results = modelling_instance.driver(features=features, save_results=False)

        return results

    def stratified_folds(self, n_folds:int=5):
        """Get the train and  test data sets for each fold
        
        Input:
        n_folds:- The number of parts in which the data is to be split

        Return:
        fold_data_list:- A list containing train and test set tuple for each fold
        """
        stratified_split_instance = SKF(n_splits=n_folds, shuffle=True, random_state=24)
        # print(help(stratified_split_instance.split))
        train_test_split = stratified_split_instance.split(X=self.train_data[self.independent_vars], 
                                                                  y=self.train_data[self.target_var])
        fold_data_list = []
        
        # print(train_test_split)

        for split in train_test_split:
            train_indices, test_indices = split
            
            try:
                X_train, y_train = self.train_data.loc[train_indices, self.independent_vars], self.train_data.loc[train_indices, self.target_var]
                X_test, y_test = self.train_data.loc[test_indices, self.independent_vars], self.train_data.loc[test_indices, self.target_var]
                train_data = pd.concat([X_train, y_train], axis=1)
                test_data = pd.concat([X_test, y_test], axis=1)
                fold_data_list.append((train_data, test_data))

            except AttributeError as AE:
                print(AE.name)

        return fold_data_list
        

    def get_fold_results(self, n_folds:int=5):
        """
        Input:
        n_folds:- The number of folds of train and test datasets

        Return:-
        Fold_1:- train_indices, test_indices
        Fold_2:- train_indices, test_indices
        ...
        """
        fold_results_df = pd.DataFrame()

        obs_per_fold = (self.train_data.shape[0])//n_folds
        start_ind = 0
        all_indices = self.train_data.index.tolist()

        for f in range(n_folds):
            if(f==(n_folds-1)):
                end_ind = len(all_indices)
            else:
                end_ind = start_ind + obs_per_fold
            
            val_test_indices = all_indices[start_ind:end_ind]
            val_train_indices = list(set(all_indices).difference(set(val_test_indices)))

            val_test = self.train_data.loc[val_test_indices, :]
            val_train = self.train_data.loc[val_train_indices, :]
            
            X_val_train, y_val_train = val_train[self.independent_vars], val_train[self.target_var]
            X_val_test, y_val_test = val_test[self.independent_vars], val_test[self.target_var]
            
            fold_results = self.training(X_train=X_val_train, y_train=y_val_train, X_test=X_val_test,
                                         y_test=y_val_test, features=self.independent_vars)

            # Tag the fold 
            fold_results["Fold"] = "Fold_"  + str(f)
            fold_results_df = pd.concat([fold_results_df, fold_results], axis=0)
            
            start_ind = end_ind

        return fold_results_df
