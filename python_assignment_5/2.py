import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
filename="Problem2.csv"
data=pd.read_csv(filename)
lst=['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for x in lst:
    avg=float(data[x].mean())
    data[x]=data[x].replace(0,avg)
x=data.iloc[:,0:8]
y=data.iloc[:,8]
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.1)
scale_x=StandardScaler()
x_train=scale_x.fit_transform(x_train)
x_test=scale_x.transform(x_test)
k_list,accuracy_list=[],[]
for k in range(3,len(y_test)//2,2):
    model=KNeighborsClassifier(n_neighbors=k,p=2,metric='euclidean')
    model.fit(x_train,y_train)
    y_prediction=model.predict(x_test)
    accuracy = accuracy_score(y_test,y_prediction)
    k_list.append(k)
    accuracy_list.append(accuracy)
plt.plot(k_list,accuracy_list)
plt.show()