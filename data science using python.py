#!/usr/bin/env python
# coding: utf-8

# # Data Science using Python

# In[1]:


marks =[12,54,65,87,98,45,43,66,75,26,82]


# In[2]:


import numpy as np


# In[3]:


mean_marks = np.mean(marks)


# In[4]:


mean_marks


# In[5]:


np.median(marks)


# In[7]:


import statistics


# In[8]:


statistics.mode(marks)


# In[10]:


from scipy import stats as stati


# In[11]:


stati.mode(marks)


# In[13]:


np.std(marks)


# In[16]:


np.var(marks)


# In[17]:


np.sqrt(631.685950413223)


# In[19]:


np.percentile(marks,54)


# In[20]:


np.random.uniform(marks)


# In[21]:


np.random.uniform(0,5,250)


# In[24]:


np.random.uniform(0,10,864)


# In[35]:


randomnumber=np.random.uniform(0,5,250)


# In[33]:


import matplotlib.pyplot as plt


# In[36]:


plt.hist(randomnumber)


# In[37]:


plt.hist(marks)


# In[38]:


plt.hist(randomnumber,7)


# In[40]:


plt.hist(marks,9)


# In[44]:


rn=np.random.uniform(10,50,100000)


# In[45]:


plt.hist(rn,100)


# In[48]:


rn=np.random.normal(1,5,100000)


# In[51]:


plt.hist(rn,105)


# In[52]:


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)


# In[53]:


import numpy as np

print(np.__version__)


# In[54]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# In[55]:


arr = np.array([1, 2, 3, 4, 5])

print(arr)


# In[56]:


arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)


# In[58]:


arr = np.array([[[1, 2, 3], [4, 5, 6],[7,8,9]], [[1, 2, 3], [4, 5, 6],[7,8,9]]])

print(arr)


# In[59]:


import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[60]:


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


# In[61]:



arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)


# In[62]:


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)


# In[63]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)


# In[64]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# In[65]:


arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


# In[66]:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)


# In[70]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


# In[72]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6],[1, 2, 3],[1, 2, 3],[1, 2, 3]], [[7, 8, 9], [10, 11, 12],[1, 2, 3],[1, 2, 3],[1, 2, 3]]])

for x in arr:
  print(x)


# In[73]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


# In[74]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


# In[75]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[ ]:




