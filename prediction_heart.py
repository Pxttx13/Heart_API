import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings


"""
def prepare(cp_selected, trestbps, chol, fbs_selected, restecg_selected, thalach, exang_selected):
    # loading the csv data to a Pandas DataFrame
    path = "C:/Users/Kashaf/Desktop/heart.csv"
    heart_data = pd.read_csv(path)

    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    model = LogisticRegression()
    # Filter out any warnings
    warnings.filterwarnings("ignore")
    model.fit(X_train, Y_train)

    # accuracy on training data
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

    # Filter out any warnings
    warnings.filterwarnings("ignore")

    input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
        print('The Person does not have a Heart Disease')
    else:
        print('The Person has Heart Disease')


"""

def prepare(cp, trestbps, chol, fbs, restecg, thalach, exang):
    # loading the csv data to a Pandas DataFrame
    path = "C:/Users/Kashaf/Desktop/heart.csv"
    heart_data = pd.read_csv(path)

    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    model = LogisticRegression()
    # Filter out any warnings
    warnings.filterwarnings("ignore")
    model.fit(X_train, Y_train)

    # accuracy on training data
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

    # Filter out any warnings
    warnings.filterwarnings("ignore")

    # Input data for prediction
    # input_data = (0, cp, 0, trestbps, chol, fbs, 0, restecg, 0, thalach, 0, 0, exang)

    input_data = (37,1,2,130,250,0,1,187,0,3.5,0,0,2)
    
    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The Person does not have a Heart Disease'
    else:
        return 'The Person has Heart Disease'
