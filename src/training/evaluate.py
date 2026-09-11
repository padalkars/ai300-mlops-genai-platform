from sklearn.metrics import roc_auc_score
import numpy as np

class Evaluate:

    def get_metrics(self, actuals, predicted, data_set=None):
        """Compute the Accuracy, Precision and Recall

        Input:
        actuals:- A list of actual class labels for the observations
        predicted:- A list of predicted class labels for the same set of observations
        data_set:- The name of the data set, viz. "Train Set", "Test Set", "Validation Set"

        Return:
        A dictionary containing the metrics Accuracy, Precision and Recall.
        
        """
        actuals, predicted = np.array(actuals), np.array(predicted)

        TP = np.dot(actuals, predicted)

        TN = np.dot(1-actuals, 1-predicted)

        FP = sum(1-actuals) - TN

        FN = sum(actuals) - TP

        accuracy = round((TP+TN)/(TP+FP+TN+FN), 2)
        precision = round(TP/(TP+FP), 2)
        recall = round(TP/(TP+FN), 2)

        return {"Accuracy": [accuracy], "Precision": [precision], "Recall": [recall], "Data Set": [data_set]}

    def auc_roc(self, trained_model, X_train, X_test):
        pass

        