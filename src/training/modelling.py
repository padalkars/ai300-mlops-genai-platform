import pandas as pd
import numpy as np
import joblib 
from evaluate import Evaluate
from pathlib import Path


class Modeling:
    def __init__(self, X_train, y_train, X_test, y_test, ml_algo_obj, model_name=None):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.ml_algo_obj = ml_algo_obj
        self.model_name = model_name

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

    def save_results(self, entity, folder_path, file_name=None, is_model=False):
        """Used to save results and model for future reference
        
        Input:
        entity:- The entity to be stored. viz. data frame, .pkl file
        folder_path:- The location of the folder where the entity is to be stored
        file_name:- The name of the file where the entity is stored, valid when the entity is a data frame.
        is_model:- A flag to check whether a trained model is to be saved to the disk

        Return:
        None        
        """
        if(is_model):
            joblib.dump(entity, folder_path / self.model_name + ".pkl")
        else:
            entity.to_csv(entity, folder_path / file_name + ".csv")


    def driver(self, features, save_results=False):
        """
        Input:
        features:- The input features to be used for training 
        save_results:- A flag indicating whether to save the results or not. 
                       Not required during the cross validation stage

        Return:
        trained_model:- The trained model, a serailized object.
        results:- The metrics obtained for training and testing data.

        """
        # Model training
        trained_model, train_results, test_results = self.training(features=features)
        
        # Model Evaluation
        eval_obj_train = Evaluate(X=self.X_train, actuals=train_results["Actuals"], predicted=train_results["Predicted"],
                                  data_set_name="Train Data")
        train_metrics = eval_obj_train.driver(trained_model=trained_model) 

        eval_obj_test = Evaluate(X=self.X_test, actuals=test_results["Actuals"], predicted=test_results["Predicted"], 
                                data_set_name="Test Data")
        test_metrics = eval_obj_test.driver(trained_model=trained_model)

        train_metrics, test_metrics = list(map(pd.DataFrame, [train_metrics,
                                                              test_metrics]))

        results = pd.concat([train_metrics, test_metrics], axis=0)

        # Save the results
        if(save_results):
            result_path = Path(__file__).parent.parent.parent / "data" / "Results"
            self.save_results(entity=trained_model, folder_path=result_path, is_model=True)
            self.save_results(entity=train_results, folder_path=result_path, file_name="training_data_results")
            self.save_results(entity=test_results, folder_path=result_path, file_name="test_data_results")

        return trained_model, results
