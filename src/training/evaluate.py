from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np

class Evaluate:
    def __init__(self, X, actuals, predicted, data_set_name=None):
        """
        Input:
        X:- The data for the independent variables
        actuals:- The ground truth for the data
        predicted:- The predictions obtained from the model
        """
        self.X = X
        self.actuals = actuals
        self.predicted = predicted
        self.data_set_name = data_set_name

    def get_metrics(self):
        """Compute the Accuracy, Precision and Recall

        Input:
        
        Return:
        A dictionary containing the metrics Accuracy, Precision and Recall.
        
        """
        actuals, predicted = np.array(self.actuals), np.array(self.predicted)

        TP = np.dot(actuals, predicted)

        TN = np.dot(1-actuals, 1-predicted)

        FP = sum(1-actuals) - TN

        FN = sum(actuals) - TP

        accuracy = round((TP+TN)/(TP+FP+TN+FN), 2)
        precision = round(TP/(TP+FP), 2)
        recall = round(TP/(TP+FN), 2)

        return {"Accuracy": [accuracy], "Precision": [precision], "Recall": [recall], "Data Set": [self.data_set_name]}

    def get_roc_curve(self, trained_model):
        """
        Input:
        trained_model:- The trained model

        Return:
        A curve representing the degree of separation between the positive and the negative classes.
        """
        predicted_probability = trained_model.predict_proba(self.X)[:, 1]

        # Area under the curve - roc_score
        auc = round(roc_auc_score(y_true=self.actuals, y_score=predicted_probability), 2)
        fpr, tpr, _ = roc_curve(y_score=predicted_probability, y_true=self.actuals)

        # Plot the auc-roc curve
        fig, ax = plt.subplots()
        ax.plot(fpr, tpr)
        if(self.data_set_name):
            plt.title(f"ROC curve - {self.data_set_name}")

        plt.xlabel("False Positive Rate")
        plt.ylabel("Recall")
        ax.legend([auc], loc="lower right")
        plt.show()

    def driver(self, trained_model):
        self.get_roc_curve(trained_model=trained_model)
        metrics_dict = self.get_metrics()
        return metrics_dict
        
        

