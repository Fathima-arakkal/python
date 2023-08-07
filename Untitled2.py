#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# In[13]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)
dataset= pd.read_csv("Data (1).csv")
X = dataset.iloc[:,-1].values
Y = dataset.iloc[:,3].values


# In[ ]:


print("Handling missing values")
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
print ('X: %s'%(str(X)))


# In[ ]:


print("Encoding Categorical data")
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
print(X[:,0])


# In[ ]:


print("Scaling features")
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
print(X_train)
print(X_test)


# In[ ]:




