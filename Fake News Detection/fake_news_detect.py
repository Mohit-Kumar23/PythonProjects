import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import KFold
import itertools
import numpy as np
import seaborn as sb
import pickle

var = input("Please Enter News Text you want to verify:")

# function to run for prediction
def detecting_fake_news(var):
    # retriving the best model for prediction call
    load_model = pickle.load(open("final_model.sav",'rb'))
    prediction = load_model.predict([var])
    
    return (print("\n\nThe Given News is:",prediction[0]))
