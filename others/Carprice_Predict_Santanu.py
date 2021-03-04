import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('csv/final.csv')
p=dataset.isnull().sum()
print(dataset.shape)
dataset['Price']=dataset['Price'].str.replace(',',"")
dataset['KMS_Driven']=dataset['KMS_Driven'].str.replace('kms',"")
dataset['KMS_Driven']=dataset['KMS_Driven'].str.replace(',',"")
df=dataset.dropna()
p1=dataset.isnull().sum()
print(df.shape)
x=df.iloc[:,[2,4,5]].values
y=df.iloc[:,3].values
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
x[:, 2] = labelencoder.fit_transform(x[:, 2])
print(x)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x, y, 
                    test_size = .25, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)

accuracy=(regressor.score(x_test,y_pred))
print("Accuracy=",accuracy)

from sklearn import metrics
print("Error=",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#Output Transfer
def execute(year,km,fuel):
    arr = np.array([year,km,fuel]).reshape(1, 3)
    return regressor.predict(arr)




