import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data=pd.read_csv(r'D:\faiq\iris_data_2a.csv')
print(data.head())
x=data.drop('species','columns')
y=data['species']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

scaler=StandardScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
result= regressor.predict(x_test)
print("Result:\n",result)

from sklearn.metrics import mean_absolute_error,mean_squared_error
print('Mean Absolute Error:', mean_absolute_error(y_test, result))
print('Mean Squared Error:', mean_squared_error(y_test, result))
print('Mean Root Squared Error:', np.sqrt(mean_squared_error(y_test, result)))
