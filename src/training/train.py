from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LR
from splitting import Splitting
from EDA.get_stats import Statistics
from modelling import Modeling
from cross_validation import CrossValidation as CV
from evaluate import Evaluate

data_csv_path = Path(__file__).parent.parent.parent / "data"

data = pd.read_csv(data_csv_path / "bank+marketing" / "bank" / "bank-full.csv", sep=";")

# Entire data
stats_instance = Statistics(data=data)
overall_stats = stats_instance.get_stats()
overall_stats.to_csv(data_csv_path / "overall_stats.csv")

# Variable types and seggregation
target_var = "y"
categorical_vars = stats_instance.categorical_vars
continuous_vars = stats_instance.continuous_vars

# Convert target variable to numberic class values
target_map_dict = {"no":0, "yes":1}
data["target_numeric_label"] = data[target_var].map(target_map_dict)

# Split the data into training and test sets
selected_features = continuous_vars
split_instance = Splitting(raw_data=data, target_var="target_numeric_label", independent_vars=selected_features)

# 80-20 train test split
X_train, y_train, X_test, y_test = split_instance.data_split(test_size=0.20)

# Cross Validation
lr = LR(max_iter=500, solver="liblinear")
# y_train_df = pd.DataFrame(y_train)
train_data = pd.concat([X_train, y_train], axis=1)
train_data = train_data.reset_index()

cv_instance = CV(target_var="target_numeric_label", independent_vars=continuous_vars, train_data=train_data, algo_object=lr)
stratified_folds = cv_instance.stratified_folds()

CV_results = pd.DataFrame({"Folds":[]})

for fold_num,data_tup in enumerate(stratified_folds):
    train_data, test_data = data_tup
    X_train, y_train = train_data[continuous_vars], train_data["target_numeric_label"]
    X_test, y_test = test_data[continuous_vars], test_data["target_numeric_label"]
    
    # Fold results
    results = cv_instance.training(X_train, y_train, X_test, y_test, features=continuous_vars)
    results["Folds"] = fold_num+1
    CV_results = pd.concat([CV_results, results], axis=0)


# Modelling
modelling_instance = Modeling(X_train, y_train, X_test, y_test, lr, model_name="Logistic_Regression")
trained_model, train_test_results = modelling_instance.driver(features=continuous_vars)


print(train_test_results)