Credit Card Fraud Detection

Context

It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

Content
The dataset contains transactions made by credit cards in September 2013 by European cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification.

overview of the project

The project aims to build Credit card Fraud Detection system using Machine Learning with Python.

Model Training.

Model 1: No Optimization

I initially trained a model without any optimization techniques, and the results were as follows:

. Training Accuracy: 83.45%
. Test Accuracy: 81.43%

Model 2: Adam Optimization

For the second model, I employed the Adam optimization technique. Adam is an adaptive learning rate optimization algorithm that combines ideas from both Momentum and RMSProp. The model was trained with the following results:

Training Accuracy: 98.92%
Test Accuracy: 95.00%

Adam Optimization Parameters
Learning Rate: 0.00005
Reason: To ensure small and stable weight updates
Batch Size: 32 (default value)

Stochastic Gradient Descent (SGD)

The third method utilized Stochastic Gradient Descent as the optimization algorithm. SGD is a classic optimization algorithm that updates the weights using the gradients of the loss function with respect to the weights. However, the results were suboptimal:

Training Accuracy: 69.60%
Test Accuracy: 75.00%

SGD Optimization Parameters
Learning Rate: 0.9
Reason: To traverse through shallow local minima and accelerate convergence.
Batch Size: 32

Root Mean Square (RMS)

For the fourth method, I applied the Root Mean Square (RMS) optimization technique. RMSProp adapts the learning rates of each parameter by dividing the learning rate by the moving average of the squared gradients. The model achieved the following results:

Training Accuracy: 98.92%
Test Accuracy: 95.71%

RMS Optimization Parameters
Learning Rate: 0.001 (default value)
Batch Size: 32 (default value)

Conclusion 

The results demonstrate the effectiveness of optimization techniques in improving model performance. The Adam and RMS optimization methods outperformed the model trained without optimization, achieving higher accuracy on both the training and test sets.

