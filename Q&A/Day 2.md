Q1. What is an Azure ML workspace?
Answer:- It's an Azure ML resource that enables, compute, model building, tracking the activities performed as well as serving the solution(model).
Q2. What is a compute instance?
Answer:- Purpose:- Running notebook/scripts.
          Sharing:- Single user, no sharing of resources.
          Lifecycle:- Need to de-allocate resources manually.
          Scaling:- Fixed size, No acaling.
Q3. What is a compute cluster?
Answer:- Purpose:- End-end solutioning using AutoML.
          Sharing:- Resources are shared amongst users.
          Lifecycle:- Automatically de-allocates resources.
          Scaling:- Autoscales dynamically
          
Q4. What is serverless compute?
Answer:- Serverless compute allows Azure ML to manage underlying compute infrastructure for a job requirements/quota.
 
Q5. What is an Azure ML environment?
Answer:- All the required resources specific to the task are placed in the environment.
Q6. Why are environments important?
Answer:- An independent setup a docker container or a virtual enviromnent having the packages and necessay installations of versions specific to a usecase. 
To avaoid conflicting packages and configurations in case of shared resources beween users. 

Q7. What is an ML job?
Answer:- Training code
     ↓
Command Job
     ↓
Compute
     ↓
Environment
     ↓
Execution
     ↓
Outputs / logs / metrics

Q8. Where does MLflow fit?
Answer:- MLflow provides a tracking URI. 
Tracks models, metrics, artifacts, experiments.
Can be used for model management/deployment scenarios.
                 ┌─────────────┐
                 │   MLflow    │
                 │   Tracking  │
                 └──────┬──────┘
                        │
                        ↓
Training Job ───────→ Experiment
                        │
                        ├── Parameters
                        ├── Metrics
                        ├── Artifacts
                        └── Model
Training/Pipeline --> MLFlow tracking --> metrics/artifacts/model

Q9. What is the difference between workspace and environment?

 What is the difference between compute instance and compute cluster?
 
Compute Instance                                    Compute Cluster
Purpose:- Running notebook/scripts.                 End-end solutioning using AutoML.
Sharing:- Single user, no sharing of resources.     Resources are shared amongst users.
Lifecycle:- Need to de-allocate resources manually. Automatically de-allocates resources.
Scaling:- Fixed size, No acaling.                   Autoscales dynamically