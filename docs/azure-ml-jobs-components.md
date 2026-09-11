Section 1 — Azure ML Job
Q. What is a job?
A. An execution workflow

Q. What is a command job?
A. A job that executes a single command.

Q. What information does a job specify?
A. Commnad:- What to execute
   Environment:- Where to execute
   Compute:- What should be the processing unit in order to carry out the task


Section 2 — Component
Q. What is a component?
A. A component is an individual task like Classification, regression, clustering etc.

Q. Why make a component reusable?
A. A component if made reusable by encapsulating it in a function or a class can be invoked easily by a job(say a command job)
   Re-usable components enable serving many common tasks for various use-cases.

Inputs
Outputs
Parameters

Section 3 — Job vs Component

This comparison is particularly important.

	Job	Component
Purpose	Execute workload	Define reusable operation
Reusable?	Execution itself isn't the reusable definition	Yes
Inputs	Yes	Yes
Outputs	Yes	Yes
Can be used in pipeline?	As execution	As pipeline building block