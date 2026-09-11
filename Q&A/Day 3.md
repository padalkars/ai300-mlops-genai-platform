Basic
What is an Azure ML job?
Q. What is a command job?
A. An execution workflow used to execute a command. viz. python train.py
Q. What is a component?
A. A component is an individual task viz.: Classification, Regression, Clustering
Why are components useful?
What are component inputs and outputs?

Important
Q. Job vs component — what's the difference?
A.
Q. Can a component be reused?
A. A component is an individual task viz.: Classification, Regression, Clustering
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
A.
Q. You want to combine several ML steps into an end-to-end workflow. What should you use?
A.
Q. Two training jobs need different Python dependencies. Where should those dependencies be defined?
A.
Q. You want Azure ML to execute your workload without manually managing a compute resource. What compute option might you consider?
A. 