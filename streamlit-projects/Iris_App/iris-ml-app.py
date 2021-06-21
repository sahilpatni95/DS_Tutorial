import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Perdiction App

This App predicts the **Iris Flower** type!
""")

st.sidebar.header("User Input Parameters")

def user_input_features():
    sepal_len = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    sepal_wid = st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.4)
    petal_len = st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
    petal_wid = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)
    data = {'sepal_length' : sepal_len,
            'sepal_width'  : sepal_wid,
            'petal_length' : petal_len,
            'petal_width'  : petal_wid}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

perdiction = clf.predict(df)
perdiction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Perdiction')
st.write(iris.target_names[perdiction])
#st.write(prediction)

st.subheader('Perdiction Probability')
st.write(perdiction_proba)