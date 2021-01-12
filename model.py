import sklearn
import pandas as pd
import numpy as np
import pickle

data=pd.read_csv('Salary_Data.csv')



#splitting input and output columns
x=data['YearsExperience']
y=data['Salary']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

x_train=np.array(x_train).reshape(-1,1)

y_train=np.array(y_train).reshape(-1,1)

from sklearn.linear_model import LogisticRegression

logRr=LogisticRegression()

logRr.fit(x_train,y_train)


pickle.dump(logRr,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))
print(model.predict([[6]]))