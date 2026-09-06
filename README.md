# AI300 MLOps Certification Preparation

This repository is structured as a practical Azure ML and MLOps project that follows the AI-300 exam preparation topics. The goal is not just to build code, but to cover the full machine learning lifecycle that is typically assessed in the exam.

## Exam-alignment strategy

The project tasks below are mapped to the main AI-300/MLOps learning domains:

- Azure Machine Learning fundamentals
- Experimentation and model tracking
- Pipelines and automation
- Model registry and deployment
- CI/CD and infrastructure as code
- Monitoring and retraining
- Generative AI / RAG / evaluation workflows

## Project phases aligned to exam topics

### 1. Azure ML foundation
Focus: workspace, compute, datasets, environments, and experiments.

Project tasks:
- Create an Azure ML workspace and understand the role of each resource.
- Configure local and cloud compute targets for training jobs.
- Use a tabular dataset for a supervised learning scenario.
- Perform initial EDA and data quality checks.
- Capture experiment metadata using MLflow.

Repository artifacts:
- [src/training/EDA/get_stats.py](src/training/EDA/get_stats.py)
- [src/training/train.py](src/training/train.py)
- [data/bank+marketing/bank/bank-full.csv](data/bank+marketing/bank/bank-full.csv)

### 2. Training, evaluation, and model tracking
Focus: ML lifecycle, model development, and experiment tracking.

Project tasks:
- Build a training script with preprocessing and model training.
- Evaluate model quality using relevant metrics.
- Track parameters, metrics, and artifacts with MLflow.
- Keep experimentation reproducible and auditable.

What to learn for the exam:
- Why MLflow is used for tracking and comparison
- Where tracking fits between training and deployment
- How experiments support reproducibility and governance

### 3. Pipelines and reusable components
Focus: MLOps automation and orchestration.

Project tasks:
- Break the project into reusable ML components.
- Build an Azure ML pipeline for data preparation, training, and evaluation.
- Run jobs in a managed Azure ML pipeline rather than ad hoc scripts.

Exam topics covered:
- ML pipelines
- Components and orchestration
- Automation of training workflows

### 4. Model registration and deployment
Focus: packaging, versioning, and serving models.

Project tasks:
- Register the trained model in Azure ML Model Registry.
- Version the model for traceability.
- Deploy an online endpoint or batch endpoint for inference.
- Validate the deployed model with sample requests.

Exam topics covered:
- Model registry
- Deployment strategies
- Inference endpoints

### 5. CI/CD and infrastructure as code
Focus: continuous delivery for ML systems.

Project tasks:
- Set up GitHub Actions for linting, testing, and job validation.
- Automate deployment steps using pipeline definitions.
- Create infrastructure using Bicep or similar IaC tooling.
- Keep environment configuration version-controlled.

Exam topics covered:
- CI/CD for ML operations
- IaC for Azure resource provisioning
- Deployment automation

### 6. Monitoring, drift, and retraining
Focus: operational ML and production health.

Project tasks:
- Define monitoring signals such as data drift, feature drift, and performance metrics.
- Track model behavior after deployment.
- Set up triggers for retraining or investigation when metrics degrade.

Exam topics covered:
- Model monitoring
- Drift detection
- Feedback loop and retraining strategy

### 7. Generative AI and RAG extension
Focus: GenAIOps in the broader AI platform context.

Project tasks:
- Add a GenAI/RAG capability built on Azure AI or Foundry services.
- Integrate evaluation, tracing, and feedback loops.
- Compare traditional MLOps with GenAIOps patterns.

Exam topics covered:
- Generative AI workflows
- Prompt evaluation
- Monitoring and tracing for AI applications

## Recommended weekly execution plan

### Week 1
- Set up repository structure and Azure ML workspace understanding
- Build EDA and baseline training flow
- Add MLflow tracking

### Week 2
- Create reusable training components
- Build Azure ML training pipeline
- Register the model
- Deploy a model endpoint

### Week 3
- Add CI/CD automation
- Add Bicep infrastructure templates
- Test deployment flow end to end

### Week 4
- Add monitoring and retraining logic
- Add GenAI/RAG capability
- Review architecture, Q&A, and final documentation

## Final exam readiness checklist

Before the exam, the project should clearly demonstrate:
- Azure ML workspace usage and core concepts
- ML pipeline orchestration
- Experiment tracking with MLflow
- Model registry and deployment flow
- CI/CD automation with GitHub Actions
- Azure infrastructure setup with IaC
- Monitoring and retraining practices
- Understanding of GenAI / RAG evaluation and observability

## Key project outcome

The repository should be considered a working MLOps project that mirrors the core AI-300 themes, not just a data science notebook. This makes it stronger as study material because it reflects the end-to-end lifecycle of an Azure AI solution.
