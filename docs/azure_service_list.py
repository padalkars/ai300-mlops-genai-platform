import pandas as pd
import numpy as np
from pathlib import Path
import os
path = Path(os.getcwd() + "/docs/")
print(path)

requirements_azure_map = {"ML workspace": "Azure Machine Learning", "Experiment Tracking": "ML Flow", "Training": "Azure ML Jobs",
                         "Pipeline Orchestration": "Azure ML Pipelines", "Model Registry": "Azure ML Registry", "Real-Time Inference":"Managed Online Endpoint",
                         "Batch Inference":"Batch Endpoint", "CI/CD":"GitHub Actions", "IaC": "Bicep", "Monitoring": "Azure ML Model Monitor / Azure Monitor", 
                         "GenAI":"Microsoft Foundry", "RAG":"Foundry + Retrieval Components", "Evaluation":"Foundry Evaluation", "Observability":"Foundry tracing/Azure Monitor"}

azure_technology = pd.DataFrame({"Requirement": list(requirements_azure_map.keys()), "Azure/Microsoft Technology":list(requirements_azure_map.values())})

azure_technology.to_csv(os.path.join(path, "Azure_Services.csv"))