# Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np

#import matplotlib.pyplot as plt
#import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error


@st.cache
def load_data():
    # Reading Downloaded DataSet 
    # DataSet Link: "http://bit.ly/w-data"

    df = pd.read_csv('./student_scores - student_scores.csv')
    df.head()

    X = df.iloc[:, :-1].values  
    y = df.iloc[:, 1].values

    return X,y

@st.cache
def model():
    """This function train the model and return the accuracy/"""
    # Load features and target
    X, y = load_data()

    # Create model and get accuracy.
    lrmodel = LinearRegression()
    lrmodel.fit(X, y)
    acc = lrmodel.score(X, y)

    # return accuracy
    return lrmodel, acc*100
