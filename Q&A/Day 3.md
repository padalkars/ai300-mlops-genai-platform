Basic
Q. What is an Azure ML job?
A. viz.:- command job, sweep job, parallel job
Q. What is a command job?
A. An entity that suggests what to execute, where to execute and what should be the input and the output. viz. python train.py
Q. What is a component?
A. A component is an individual task viz.: Classification, Regression, Clustering
   Examples of components:-
   1. data pre-processing
   2. training
   3. evaluate
   4. monitoring
   5. serving
Q. Why are components useful?
A. 

Q. What are component inputs and outputs?
A. Inputs:- Data, trained model, 
   Outputs:- trained Model(.pkl), metrics(accuracy, precision, recall etc.), serving(url/endpoint)

Important
Q. Job vs component — what's the difference?
A. Job:- Triggers an execution. Example:- Command Job, Scalled Job, Parallel Job, Pipeline Job
   Component:- An entity dedicated for a task that needs to be done.

Q. Can a component be reused?
A. Yes. For example a method that performs data pre-processing steps like missing value analysis, variable encoding etc. can be used across multiple tasks or within the same task. A component is an individual task viz.: Classification, Regression, Clustering.

Q. What is the relationship between a component and a pipeline?
A. A component is a part of a pipeline.

Q. Where does compute fit into a job?
A. Resources like CPU/GPU to be used to carry out the processing of the component.

Q. Where does environment fit into a job?
A. 

Scenario questions
Q. You need to execute train.py once. What would you use? 
A. I will use command job.

Q.You have preprocessing, training and evaluation steps that should be reused in different workflows. What should you create?
A. Create components for each of the tasks like pre-processing, training and evaluation.

Q. You want to combine several ML steps into an end-to-end workflow. What should you use?
A. I will use a pipeline.

Q. Two training jobs need different Python dependencies. Where should those dependencies be defined?
A. 

Q. You want Azure ML to execute your workload without manually managing a compute resource. What compute option might you consider?
A. Serverless Compute.