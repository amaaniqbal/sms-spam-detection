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

## Example Workflow
```
name: SMS Spam Detection Action

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.5, 3.6, 3.7, 3.8]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run the classifier
      run: |
        python main.py
```


## Contributing
Please feel free to create an issue if you find a bug or send a pull request if you wish to improve the existing code/add a new feature. 
