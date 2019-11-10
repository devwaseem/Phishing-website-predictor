import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn import tree
import pickle
from pathlib import Path

__model_filename = "model.bin"

def train_model():
    df = pd.read_csv("data.csv",delimiter=",")
    Y = df.Result
    X = df.drop("Result",axis=1)
    X = X.drop("Statistical_report",axis=1)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X,Y)
    pickle.dump(clf, open(__model_filename, 'wb'))
    return clf

def load_model(force=False):
    if not Path("",__model_filename).is_file() or force: 
        return train_model()
    return pickle.load(open(__model_filename, 'rb'))