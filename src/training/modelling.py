import pandas as pd
import numpy as np
import joblib 
from evaluate import Evaluate


class Modeling:
    def __init__(self, X_train, y_train, X_test, y_test, ml_algo_obj):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.ml_algo_obj = ml_algo_obj

    def training(self, features):
        trained_model = self.ml_algo_obj.fit(self.X_train[features], 
                                             self.y_train)
        
        # Training data predictions
        predicted_train = trained_model.predict(self.X_train[features])
        train_probabilities = trained_model.predict_proba(self.X_train[features])

        # Testing data predictions
        predicted_test = trained_model.predict(self.X_test[features])
        test_probabilities = trained_model.predict_proba(self.X_test[features])

        train_results = pd.DataFrame({"Train_Indices":self.X_train.index.tolist(), 
                                      "Actuals":self.y_train, 
                                      "Probabilities":train_probabilities[:, 1],
                                      "Predicted":predicted_train})
        
        test_results = pd.DataFrame({"Test_Indices":self.X_test.index.tolist(), 
                                     "Actuals":self.y_test, 
                                     "Probabilities":test_probabilities[:, 1],
                                     "Predicted":predicted_test})

        return trained_model, train_results, test_results

    def save_results(self, entity, path, file_name, is_model=False):
        """Used to save results and model for future reference
        
        Input:
        entity:- The entity to be stored. viz. prediction results, model
        path:- The location of the folder where the entity is to be stored
        file_name:- The name of the file where the entity is stored
        is_model:- A flag to check whether a trained model is to be saved to the disk

        Return:
        None        
        """
        if(is_model):
            joblib.dump(path / file_name)
        else:
            pass


    def driver(self, features):
        # Model training
        trained_model, train_results, test_results = self.training(features=features)
        
        # Model Evaluation
        eval_obj = Evaluate()
        train_metrics = eval_obj.get_metrics(actuals=train_results["Actuals"], 
                                             predicted=train_results["Predicted"],
                                             data_set="Train") 
        test_metrics = eval_obj.get_metrics(actuals=test_results["Actuals"],
                                            predicted=test_results["Predicted"],
                                            data_set="Test")

        train_metrics, test_metrics = list(map(pd.DataFrame, [train_metrics,
                                                              test_metrics]))

        results = pd.concat([train_metrics, test_metrics], axis=0)

        return trained_model, results
