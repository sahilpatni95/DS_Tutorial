import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pickle


url = 'https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv'
df =  pd.read_csv(url)

# X = ['MolLogP', 'MolWt', 'NumRotatableBonds', 'AromaticProportion']
X = df.drop(['logS'], axis = 1)
# Y = ['logS']
Y = df.iloc[:,-1]

# Linear Regression Model
model = linear_model.LinearRegression()
model.fit(X, Y)

# Prediction
pred = model.predict(X)

# Performance
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
print('Mean squared error (MSE): %.2f' % mean_squared_error(Y, pred))
print('Coefficient of determination (R^2): %.2f' % r2_score(Y, pred))

# Model Equation
print('LogS = %.2f %.2f LogP %.4f MW + %.4f RB %.2f AP' % (model.intercept_, model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3] ) )

# Save Model Using Pickle
pickle.dump(model, open('model.pkl', 'wb'))
print("Model Saved")