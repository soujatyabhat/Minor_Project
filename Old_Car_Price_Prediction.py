import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Take the Datset(Car_Prediction_API Based.csv) as input
car=pd.read_csv('Car_Prediction_API Based.csv')

#Using Shape method first we check the Dimension of whole data..
print(car.shape)

#USing isna().sum() method we check that, Is there any Nan value or not!!
print(car.isna().sum())

'''
Name            0
Company         0
Year            0
Price           0
KMS_Driven      0
Fuel_Type       1
Transmission    0
Current Year    0
Age             0

'''

#Here we see that there is one Nan value in Fuel_Type column, we omit this using following code..
car=car[~car['Fuel_Type'].isna()]

#Again we check the existance of Nan value..
print(car.isna().sum())

'''
Name            0
Company         0
Year            0
Price           0
KMS_Driven      0
Fuel_Type       0
Transmission    0
Current Year    0
Age             0

'''



'''
---:We have to update some data of the dataset:---

1.We have to erase the ","(comma) sign from 'Price' column of the dataset.
2.We have to change the datatype of 'Price' column in integer type.
3.We have to erase the ","(comma) sign from 'KMS_Driven' column of the dataset.
4.We have to change the datatype of 'KMS_Driven' column in integer type. 

'''

'''Here we erase the comma sign and change the datatype of the Price column'''
car['Price']=car['Price'].str.replace(',','').astype(int)

'''Here we erase the comma sign and change the datatype of the KMS_Driven column'''
car['KMS_Driven']=car['KMS_Driven'].str.split().str.get(0).str.replace(',','')
car['KMS_Driven']=car['KMS_Driven'].astype(int)



'''Here we saved the cleared and updated dataset'''
car.to_csv('Cleared_Data.csv')


'''We store the some value of dataset in two variables'''
X=car[['Company','Age']]
y=car['Price']
 

''' Here we train our regression model
    1. Prepare the data for training and testing.
    2. Split the data.
    3. Fixed the size of train data and test data.
'''
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


from sklearn.linear_model import LinearRegression


'''We want to pass the categorical value of 'Company' column so thats why we import OneHotEncoder'''
from sklearn.preprocessing import OneHotEncoder

'''We transform the categorical value by using column_transformer'''
from sklearn.compose import make_column_transformer

'''Here pipeline firstly transfer the column and then go to the linear regression object.'''
from sklearn.pipeline import make_pipeline

'''Here fixed the categorical value of Company column'''
ohe=OneHotEncoder()
ohe.fit(X[['Company']])

'''Here we transfer the categorical value by using OneHotEncoder and passed the other value by using remainder.'''
column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),['Company']),
                                    remainder='passthrough')

lr=LinearRegression()

'''Here pipeline first transfer the column and then it send the data to linear regreesion.'''
pipe=make_pipeline(column_trans,lr)
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)



'''We check the accuracy by using accuracy method.'''
accuracy = (pipe.score(X_test,y_pred))
print("Accuracy:",accuracy)


def excute(m,a):
    return pipe.predict(pd.DataFrame(columns=X_test.columns,data=np.array([m,a]).reshape(1,2)))

