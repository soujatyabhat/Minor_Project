import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('final.csv')
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
print("Result=",regressor.predict([[2010,72000,2]]))

plt.plot(x_train[:,1],y_train,'r*')
#y_pred_train=regressor.predict(x_train)
#plt.plot(x_train[:,1],y_pred_train)
plt.title("Car Price Predection")
plt.xlabel("KM_Drives")
plt.ylabel("Price")
plt.show()

plt.plot(x_train[:,0],y_train,'r*')
#y_pred_train=regressor.predict(x_train)
#plt.plot(x_train[:,1],y_pred_train)
plt.title("Car Price Predection")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

'''plt.figure(figsize=(270,100))
plt.scatter(x_train[:,1],y_train,marker=',',color='r',s=10000)
plt.xticks(fontsize=100)
plt.yticks(fontsize=120)
#y_pred_train=regressor.predict(x_train)
#plt.plot(x_train[:,1],y_pred_train)
plt.title("Car Price Prediction",fontsize=300)
plt.xlabel("KM_Drives",fontsize=300)
plt.ylabel("Price",fontsize=300)
plt.show()

plt.figure(figsize=(270,100))
plt.scatter(x_train[:,0],y_train,marker=',',color='b',s=10000)
plt.xticks(fontsize=100)
plt.yticks(fontsize=120)
#y_pred_train=regressor.predict(x_train)
#plt.plot(x_train[:,1],y_pred_train)
plt.title("Car Price Prediction",fontsize=300)
plt.xlabel("Year",fontsize=300)
plt.ylabel("Price",fontsize=300)'''

