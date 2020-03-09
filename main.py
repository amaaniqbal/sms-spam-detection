#Display message
print ("Importing Libraries...")

#Import libraries
import sys
import string
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
import pandas as pd

#Import libraries for performing NLP
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix

#Display message
print ("All libraries imported...")

#Display message
print ("Reading the dataset...")

#Read CSV
messages = pd.read_csv('dataset/SMSSpamCollection', sep='\t', names=['Label', 'Message'])

#Display message
print ("Dataset read successfully...")

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


#Display message
print ("Started creating pipeling...")

#TRAINING
#Create Pipeline
#Both training and testing data will pass through our created pipeline sequentially
pipeline = Pipeline([
        ('bow', CountVectorizer(analyzer=processText)),    # strings to token integer counts
        ('tfidf', TfidfTransformer()),                     # integer counts to weighted TF-IDF scores
        ('classifier', MLPClassifier())                    # train on TF-IDF vectors with MLP classifier
    ])

#Display message
print ("Pipeline created successfully...")

 
#Display message
print ("Fitting the pipeline...")

#Fitting using pipeline
pipeline.fit(msg_train, label_train)

#Display message
print ("Pipeline fitted successfully...")


#Display message
print ("Predicting the results...")

argumentsList = sys.argv

if len(argumentsList) == 1 :
    #TESTING
    #Predicting using pipeline
    predictions = pipeline.predict(msg_test)
    
    #Display message
    print ("Results predicted...")
    
    
    #Display message
    print ("Displaying results...")
    print ("Confusion Matrix :")
    
    
    #PRINTING RESULTS
    print(confusion_matrix(label_test, predictions))

else :
    # Extract the message
    message = " ".join(sys.argv[1:])
    
    #TESTING
    #Predicting using pipeline
    prediction = pipeline.predict(pd.Series(message))
    
    #Display message
    print ("Results predicted...")
    
    #Display message
    print ("Displaying results...\n")
    print ("Input Message is a ", prediction)
    
