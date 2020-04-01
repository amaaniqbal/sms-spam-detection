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


## Usage
Run the file `main.py` without any command line arguments to view the classifier performance on the available test set. In order to test on the custom input, run the following command:

```
python main.py "Custom input string goes here"
```

In the command, custom input string can also be specified without quotes.


## Action Usage
To use this action in your repository, create a file like .github/workflows/spam_detect.yml with the following content:
```
name: Spam Detection Action
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: SMS Spam Detection Action
      uses: amaaniqbal/sms-spam-detection@v1.10
      with:
        # Message to be checked for spam
        message: "input message to be tested goes here..."
```
You can remove the `with` section completely if you just wish to see the classifier performance.


## Contributing
Please feel free to create an issue if you find a bug or send a pull request if you wish to improve the existing code/add a new feature. 
