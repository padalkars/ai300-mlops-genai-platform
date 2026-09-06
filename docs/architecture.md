Objective:- Build and operationalize an ML System on Azure that supports training, deployment, monitoring and continuous improvement, 
with GenAI/RAG capability layered on top of it.

--> Where does CI/CD fit?

Developer
   ↓
GitHub
   ↓
Pull Request
   ↓
CI
   ↓
Tests
   ↓
Build
   ↓
Azure ML
   ↓
Deploy

--> Where does Monitoring Fit?

             ┌──────────────┐
             │   Monitoring │
             └──────┬───────┘
                    │
Data → Train → Model → Deploy → Inference
                    │
                    ↓
                 Feedback
                    │
                    └──→ Retraining


--> Where will GenAIOps enter?

                 ML System
                    │
             ┌──────┴──────┐
             ↓             ↓
        ML inference    GenAI
                           │
                         RAG
                           │
                     Microsoft Foundry
                           │
                Evaluation + Tracing
                           │
                       Monitoring

--> What problems does Azure ML solve?
Azure ML provides managed compute where training jobs can run.
   Local files(laptop) --> Azure ML Compute --> Train Model

Enables automation via ML Pipelines.
   Data --> Train --> Evaluate --> Deploy --> Track(ML Flow) --> Register

Where to store/version model?
   Model registry

