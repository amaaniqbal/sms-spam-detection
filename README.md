# SMS Spam Detection
This repository teaches to code an SMS Spam Classifier using Multi-Layer Perceptron. Here, scikit-learn pipelines are used for pipelining the training and testing task on the training and testing sets respectively. The codes for the same are avaialble in `main.py`.

A high level view of the system is as follows:

- Import libraries
- Import SMS Spam Collection dataset
- Define function for removing punctuations and stopwords
- Split training and testing set
- Create pipeline
  - Construct Bag of Words
  - Compute tf-idf scores
  - Instantiate MLP Classifier
- Fit the pipeline on the training set
- Test the pipeline on the test set
- Print the results


