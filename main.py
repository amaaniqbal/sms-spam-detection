#Import libraries
import string
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
import pandas as pd

#Import libraries for performing NLP
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neural_network import MLPClassifier

#Read CSV
messages = pd.read_csv('dataset/SMSSpamCollection', sep='\t', names=['Label', 'Message'])

#Text Processing
#Tokenization
#No stemming
def processText(message) :
    """
        This function performs tokenization of input string
        1. Remove punctuations
        2. Remove stopwords
        3. Returns the list of clean text words
    """
    noPunctuation = [char for char in message if char not in string.punctuation]
    noPunctuation = ''.join(noPunctuation)   #Join all the character in character array returned in the previous statament
    tokenizedMessage = [word for word in noPunctuation.split() if word.lower() not in stopwords.words('english')]
    return tokenizedMessage

#Split dataset into train and test set
from sklearn.model_selection import train_test_split
msg_train, msg_test, label_train, label_test = train_test_split(messages['Message'], messages['Label'], test_size=0.2)


#Create Pipeline
#Importing pipeline 
from sklearn.pipeline import Pipeline

#TRAINING
#Both training and testing data will pass through our created pipeline sequentially
pipeline = Pipeline([
        ('bow', CountVectorizer(analyzer=processText)),    # strings to token integer counts
        ('tfidf', TfidfTransformer()),                     # integer counts to weighted TF-IDF scores
        ('classifier', MLPClassifier())                    # train on TF-IDF vectors with MLP classifier
    ])

#Fitting using pipeline
pipeline.fit(msg_train, label_train)


#TESTING
#Predicting using pipeline
predictions = pipeline.predict(msg_test)


#PRINTING RESULTS
from sklearn.metrics import confusion_matrix
print(confusion_matrix(label_test, predictions))
