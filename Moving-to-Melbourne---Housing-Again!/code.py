# --------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path

#Code starts here

# load the dataframe
df = pd.read_csv(path)
# print(df.head())

#Indepenent varibles
X = df.drop('Price',axis=1)
# print(X)

# store dependent variable
y = df['Price']
# print(y)

# spliting the dataframe

X_train,X_test,y_train,y_test = train_test_split(X,y ,test_size=0.3,random_state=6)
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)

# check correlation
corr = X_train.corr()

# print correlation
print(corr)

#Code ends here




# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here
regressor = LinearRegression()
# print(regressor)

# fitting the modal of trainning data 
regressor.fit(X_train,y_train)

# make a prediction 
y_pred = regressor.predict(X_test)

# find the r^2 score
r2 =  r2_score(y_test,y_pred)
print(r2)


# --------------
from sklearn.linear_model import Lasso

# Code starts here
# Instantiate a lasso funcation 
lasso = Lasso()

# fit the model on training data 
lasso.fit(X_train, y_train)

# make the prediction with lasso funcation with X_test variable 
lasso_pred = lasso.predict(X_test)

# Calculate the r^2 score 
r2_lasso = r2_score(y_test, lasso_pred)
print(r2_lasso)


# --------------
from sklearn.linear_model import Ridge

# Code starts here
# Instantiate a lasso funcation 
ridge = Ridge()

# fit the model on training data 
ridge.fit(X_train, y_train)

# make the prediction with lasso funcation with X_test variable 
ridge_pred = ridge.predict(X_test)

# Calculate the r^2 score 
r2_ridge = r2_score(y_test, ridge_pred)
print(r2_ridge)


# Code ends here


# --------------
from sklearn.model_selection import cross_val_score

#Code starts here

# Initiate a LinearRegression() object  
regressor = LinearRegression()

# Calculate the cross_val_score on X_train,y_train having model = regressor and cv = 10, and store the result in a variable called 'score'. 
score = cross_val_score(regressor, X_train, y_train, cv=10)
# print(score)

mean_score = np.mean(score)
print(mean_score)


# --------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here
# Initiate a pipeline for polynomial features as 'make_pipeline' having parameter 'PolynomialFeatures(2),linearregressioin
model = make_pipeline(PolynomialFeatures(2), LinearRegression())
print(model)
# Fit the model on the training data, X_train and y_train.
model.fit(X_train, y_train)

# Make predictions on the X_test
y_pred = model.predict(X_test)
print(y_pred)

# Find the r^2 score and store the result
r2_poly = r2_score(y_test, y_pred)
print(r2_poly)


