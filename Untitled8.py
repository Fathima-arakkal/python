#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[2]:


a = 2
while a < 20:
    print(a)
    a += 2


# In[3]:


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# In[6]:


a = 2
while a < 100:
    print(a)
    if a == 50:
        break
    a += 5


# In[7]:


a = 2
while a < 100:
    print(a)
    if a == 72:
        break
    a += 5


# In[8]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[9]:


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# In[12]:


for x in range(10,35):
  print(x)


# In[13]:


x = lambda a : a + 10
print(x(5))


# In[14]:


x = lambda a : a + 20
print(x(2))


# In[15]:


x = lambda a : a + 5
print(x(2))


# In[16]:


def a(b):
    return b+20
print(a(5))


# In[17]:


x = lambda a, b : a * b
print(x(5, 6))


# In[18]:


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# In[20]:


import numpy as np


# In[21]:


fruits = ["Apple", "Mango", "Orange"]
print(fruits)


# In[22]:


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)


# In[24]:


fruits = numpy.array(["Orange","Mango","Apple"])
print(fruits)
print(type(fruits))


# In[131]:


from numpy import random

x = random.randint(61)

print(x)


# In[163]:


x=random.randint(1,60, size=(6))
print(x)
print(type(x))


# In[167]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("Doe", 45)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


# In[173]:


class Rajagiri:
    x="Hello MCA"
a=Rajagiri()
print(a.x)
a.x


# In[179]:


class Rcss:
  def __init__(rcss,name,age,year):
    rcss.name = name
    rcss.age = age
    rcss.year = year
stud1 = Rcss("Fathima",21,2001)
stud2 = Rcss("Doney",24,1999)
stud3 = Rcss("Dona",22,2002)
print(stud1.name,stud1.age,stud1.year)
print(stud2.name,stud2.age,stud2.year)
print(stud3.name,stud3.age,stud3.year)


# In[183]:


class Rcss:
  def __init__(rcss,x,y,z):
    rcss.x = x
    rcss.y = y
    rcss.z = z
stud1 = Rcss("Fathima",21,2001)
stud2 = Rcss("Doney",24,1999)
stud3 = Rcss("Dona",22,2002)
print(stud1.x,stud1.y,stud1.z)
print(stud2.x,stud2.y,stud2.z)
print(stud3.x,stud3.y,stud3.z)


# In[190]:


class Person:
  def __init__(mysillyobject, name, surname):
    mysillyobject.name = name
    mysillyobject.surname = surname

  def myfunc(abc):
    print("Hello my name is " + abc.name , abc.surname)

p1 = Person("Fathima","Arakkal")
p1.myfunc()


# In[ ]:




