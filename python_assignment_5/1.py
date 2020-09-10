import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
filename="Problem1.txt"
data=pd.read_csv(filename,sep='\t')
x=data.iloc[:,3:]
y=data.iloc[:,2]
k_list,accuracy_list_1=[],[]

#for K Nearest Neighbors between different number of neighbors and accuracy
for k in range(3,10,2):
    x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.2)
    scale_x=StandardScaler()
    x_train=scale_x.fit_transform(x_train)
    x_test=scale_x.transform(x_test)
    model=KNeighborsClassifier(n_neighbors=k,p=2,metric='euclidean')
    model.fit(x_train,y_train)
    y_prediction=model.predict(x_test)
    model=confusion_matrix(y_test,y_prediction)
    accuracy = accuracy_score(y_test,y_prediction)
    k_list.append(k)
    accuracy_list_1.append(accuracy)

#For Logistic Regression between different random_state and accuracy
random_cases,accuracy_list_2=[],[]
for k in range(8):
    x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=k,test_size=0.2)
    scale_x=StandardScaler()
    x_train=scale_x.fit_transform(x_train)
    x_test=scale_x.transform(x_test)
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_prediction=model.predict(x_test)
    accuracy = accuracy_score(y_test,y_prediction)
    random_cases.append(k)
    accuracy_list_2.append(accuracy)

plt.figure(1)
plt.scatter(k_list,accuracy_list_1)  #figure_1 between different number of neighbors and accuracy using K Nearest Neighbors
plt.figure(2)
plt.scatter(random_cases,accuracy_list_2)  #figure_1 between different random_state and accuracy using Logistic Regression
plt.show()

avg_1=sum(accuracy_list_1)/len(k_list)
avg_2=sum(accuracy_list_2)/len(random_cases)
if avg_1>avg_2:
    print("K Nearest Neighbour is better in this case")
else:
    print("Logistic Regression is better in this case")