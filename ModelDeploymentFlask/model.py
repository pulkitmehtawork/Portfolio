# import libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import json
import requests

# read salary data and split it into featues and labels
df = pd.read_csv('SalDetail.csv')
X = df.iloc[:,:-1]
y = df.iloc[:,1]


# split data into train , test dataset

X_train, X_test , y_train, y_test = train_test_split(X,y,random_state=0)

# Build model and fit it on training data 
model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
# save the model
pickle.dump(model , open('model.pkl','wb'))

# load the model
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[3]]))
