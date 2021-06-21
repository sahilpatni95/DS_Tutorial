import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes, load_boston

# Page layout
## Page expands to full width

st.set_page_config(page_title='The Machine Learning App ', layout='wide')

#-------------------------------------#
# Model Building
def build_model(df):
    X = df.iloc[:,:-1]
    Y = df.iloc[:,-1]

    st.markdown('** Data Shape **')
    st.write(' Training Set')
    st.info(X.shape)
    st.write(' Test Set')
    st.info(Y.shape)

    #st.markdown(' ** Data Infomations **')
    #st.write(' Training Set')
    #st.info(X.info())
    #st.write(' Test Set')
    #st.info(Y.info())

    st.markdown('** Variable Details**:')
    st.write(' X variable (Training) ')
    st.info(list(X.columns))
    st.write('Y variable (Test)')
    st.info(Y.name)

    # Data splitting
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= split_size)

    # RandomForestRegressor Model
    rf = RandomForestRegressor(n_estimators = parameter_n_estimators,
                               random_state = parameter_random_state,
                               max_features = parameter_max_features,
                               criterion = parameter_criterion,
                               min_samples_split = parameter_min_samples_split,
                               min_samples_leaf = parameter_min_samples_leaf,
                               bootstrap = parameter_bootstrap,
                               oob_score = parameter_oob_score,
                               n_jobs = parameter_n_jobs)
    rf.fit(X_train,Y_train)

    st.subheader(' Model Performance ')

    st.markdown(' ** Training Set ** ')
    Y_pred_train = rf.predict(X_train)
    st.write(' Co-efficient Of Determination ($R^2$):')
    st.info(r2_score(Y_train, Y_pred_train))

    st.write('Error (MSE or MAE):')
    st.info( mean_squared_error(Y_train, Y_pred_train))

    st.markdown(' ** Test Set ** ')
    Y_pred_test = rf.predict(X_test)
    st.write(' Co-efficient Of Determination ($R^2$):')
    st.info(r2_score(Y_test, Y_pred_test))

    st.write('Error (MSE or MAE):')
    st.info(mean_squared_error(Y_test, Y_pred_test))

    st.subheader(' Model Parameters ')
    st.write(rf.get_params())

#-------------------------------#

st.write("""
# The Machine Learning App (RandomForestRegressor)
In this implementation, the *RandomForestRegressor()* function is used in this app for build a regression model using the **Random Forest** algorithm.
Try adjusting the hyperparameters!
""")

#---------------------------------#
# Sidebar - Collects user input features into dataframe
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

# Sidebar - Specify parameter settings
with st.sidebar.header('2. Set Parameters'):
    split_size = st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5)

with st.sidebar.subheader('2.1. Learning Parameters'):
    parameter_n_estimators = st.sidebar.slider('Number of estimators (n_estimators)', 0, 1000, 100, 100)
    parameter_max_features = st.sidebar.select_slider('Max features (max_features)', options=['auto', 'sqrt', 'log2'])
    parameter_min_samples_split = st.sidebar.slider('Minimum number of samples required to split an internal node (min_samples_split)', 1, 10, 2, 1)
    parameter_min_samples_leaf = st.sidebar.slider('Minimum number of samples required to be at a leaf node (min_samples_leaf)', 1, 10, 2, 1)

with st.sidebar.subheader('2.2. General Parameters'):
    parameter_random_state = st.sidebar.slider('Seed number (random_state)', 0, 1000, 42, 1)
    parameter_criterion = st.sidebar.select_slider('Performance measure (criterion)', options=['mse', 'mae'])
    parameter_bootstrap = st.sidebar.select_slider('Bootstrap samples when building trees (bootstrap)', options=[True, False])
    parameter_oob_score = st.sidebar.select_slider('Whether to use out-of-bag samples to estimate the R^2 on unseen data (oob_score)', options=[False, True])
    parameter_n_jobs = st.sidebar.select_slider('Number of jobs to run in parallel (n_jobs)', options=[1, -1])

#---------------------------------#

# Main panel

# Displays the dataset
st.subheader(' Dataset')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.markdown(' **Glimpse of dataset** ')
    st.write(df)
    build_model(df)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Diabetes dataset
        diabetes = load_diabetes()
        X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
        Y = pd.Series(diabetes.target, name='response')
        df = pd.concat([X, Y], axis=1 )

        st.markdown('The Diabetes dataset is used as the example.')
        st.write(df.head(5))

        # Boston housing dataset
        #boston = load_boston()
        #X = pd.DataFrame(boston.data, columns=boston.feature_names)
        #Y = pd.Series(boston.target, name='response')
        #df = pd.concat( [X,Y], axis=1 )

        #st.markdown('The Boston housing dataset is used as the example.')
        #st.write(df.head(5))

        build_model(df)
