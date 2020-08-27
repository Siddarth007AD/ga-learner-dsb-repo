# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)

print(df.head())
# print(df.Shape())

X = df.drop('list_price', axis=1)

y = df['list_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=6)
# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20,20))

for i in range(0,3):
    for j in range(0,3): 
            col = cols[i*3 + j]
            axes[i,j].set_title(col)
            axes[i,j].scatter(X_train[col],y_train)
            axes[i,j].set_xlabel(col)
            axes[i,j].set_ylabel('list_price')
        

# code ends here
plt.show()
# code ends here



# --------------
# Code starts here

# find the correlation btw the feature of X_train
corr = X_train.corr()
# print(X_train)
print(corr)
# drop columns ffrom X_train
X_train.drop(['play_star_rating','val_star_rating'],axis = 1, inplace=True)

# drop columns from X_test
X_test.drop(['play_star_rating','val_star_rating'],axis = 1, inplace=True)

# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here

regressor = LinearRegression()
print(regressor)
# Fit the model on the training data X_train and y_train
regressor.fit(X_train, y_train)

# Make predictions on the X_test
y_pred = regressor.predict(X_test)
print(y_pred)
# Calculate mse
mse = mean_squared_error(y_test, y_pred)
print(mse)

# Calculate r2_score
r2 = r2_score(y_test, y_pred)
print(r2)
# Code ends here


# --------------
# Code starts here

residual = y_test - y_pred
print(residual)

# Code ends here


