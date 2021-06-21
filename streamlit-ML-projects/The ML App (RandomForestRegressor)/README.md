# Streamlit ML projects

# Demo

Launch the web app:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/ml-app/main/ml-app.py)

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *ml*
```
conda create -n ml python
```
Secondly, we will login to the *ml* environement
```
conda activate ml
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://raw.githubusercontent.com/sahilpatni95/streamlit-ML-projects/master/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```
###  Download and unzip contents from GitHub repo

Download and unzip contents - https://github.com/sahilpatni95/streamlit-ML-projects
###  Launch the app

```
streamlit run main.py
```
