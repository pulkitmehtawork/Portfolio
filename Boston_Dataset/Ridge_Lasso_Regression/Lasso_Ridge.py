# Load Libraries 
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load data 
dataset = load_boston()

# load data into dataframe 

# df with all features 
df = pd.DataFrame(dataset.data,columns = dataset.feature_names)
# add target column
df['price'] = dataset.target      


print(df.head())

# lets apply linear regression and check rmse 
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lr = LinearRegression()
lr_score = cross_val_score(lr,X,y,
                           scoring='neg_mean_squared_error',
                           cv=5)
mean_mse = np.mean(lr_score)
print('Mean MSE for linear regression is ',mean_mse)

#lets try to improve using ridge and lasso regression
# Ridge regression 
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
rr = Ridge()
param = {'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}

ridge_regressor = GridSearchCV(rr, param_grid = param, scoring='neg_mean_squared_error',cv=5)
ridge_regressor.fit(X,y)

print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_)


# Lasso regression 
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
la = Lasso()
param = {'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}

lasso_regressor = GridSearchCV(la, param_grid = param, scoring='neg_mean_squared_error',cv=5)
lasso_regressor.fit(X,y)

print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)




























            


 

