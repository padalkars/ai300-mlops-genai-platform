Knowledge Map - Day 2
      
                 Azure ML Workspace
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
      Data            Compute          Environment
                         │                 │
              ┌──────────┼─────────┐       │
              │          │         │       │
           Instance    Cluster  Serverless │
              │          │         │       │
              └──────────┴─────────┘       │
                         │                 │
                         └──────┬──────────┘
                                ↓
                               Job
                                │
                                ↓
                             MLflow
                                │
                  ┌─────────────┼─────────────┐
                  ↓             ↓             ↓
               Metrics      Artifacts      Models

Azure ML Workspace:-

Compute Instance:- An entity providing single user(no-sharing), single node, no auto-scaling compute used to execute scripts and notebooks.

Compute Cluster:- An entity providing multi-user, multi-node, auto-scaling compute used for high performance automated model training.

Serverless Compute:- A fully managed on-demand compute, Azure ML creates, scales and manages compute for you. This removes the headache of learning about compute infrastructure or setting it up.

Azure ML Environments:- An entity that enables execution of ML Job and it's tracking.

Jobs:- A job represents execution or workload submitted to Azure ML.Examples:- command job, scaled job
Comparing various jobs:-
| Feature              | Command      | Sweep                       | Parallel                        | Pipeline                    |
| -------------------- | ------------ | --------------------------- | ------------------------------- | --------------------------- |
| Main purpose         | Execute code | Tune hyperparameters        | Process tasks/data concurrently | Orchestrate workflow        |
| Runs code?           | ✅            | ✅                           | ✅                               | Through child jobs          |
| Multiple executions? | Usually 1    | Many trials                 | Many parallel tasks             | Multiple steps              |
| Main variation       | None         | Hyperparameters             | Data/task partitions            | Workflow dependencies       |
| Best example         | Train model  | Find best learning rate     | Batch inference                 | Train → evaluate → register |
| Optimization         | ❌            | ✅                           | ❌                               | ❌                           |
| DAG/workflow         | ❌            | ❌                           | ❌                               | ✅                           |
| Parallelism          | Possible     | Trials can run concurrently | Core purpose                    | Steps can have dependencies |


ML Flow:- An entity used for tracking experiments and logging the model, results, artifacts obtained from the training process.

Workspace vs Environment:- 