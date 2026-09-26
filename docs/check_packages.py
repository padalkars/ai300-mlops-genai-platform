import importlib
import sys


IMPORTS = {
	"azure.ai.ml": "from azure.ai.ml import MLClient, command, Input, Output",
	"azure.ai.ml.entities": "from azure.ai.ml.entities import Environment, Model",
	"azure.identity": "from azure.identity import DefaultAzureCredential",
	"azure.ai.projects": "from azure.ai.projects import AIProjectClient",
	"azure.ai.evaluation": "from azure.ai.evaluation import evaluate",
	"azure.storage.blob": "from azure.storage.blob import BlobServiceClient",
	"azure.keyvault.secrets": "from azure.keyvault.secrets import SecretClient",
	"azure.search.documents": "from azure.search.documents import SearchClient",
	"azure.cosmos": "from azure.cosmos import CosmosClient",
	"mlflow": "import mlflow",
	"pandas": "import pandas",
	"sklearn": "import sklearn",
	"joblib": "import joblib",
	"azureml.core": "from azureml.core import Workspace, Experiment, Environment, Dataset",
	"azureml.train.sklearn": "from azureml.train.sklearn import SKLearn",
}


print(f"Python: {sys.executable}")
failed = False
for package, statement in IMPORTS.items():
	try:
		importlib.import_module(package)
		print(f"OK   {statement}")
	except Exception as error:
		failed = True
		print(f"FAIL {statement}\n     {type(error).__name__}: {error}")

if failed:
	raise SystemExit("One or more imports failed")