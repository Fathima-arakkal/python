#!/usr/bin/env python
# coding: utf-8

# In[1]:


thistuple = ("apple", "banana", "cherry")
print(thistuple)


# In[ ]:





# In[2]:


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# In[3]:


def my_function(x):
  return 15 * x

print(my_function(2))
print(my_function(5))
print(my_function(10))


# In[4]:


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# In[5]:


def myfun(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
myfun(fruits)


# In[10]:


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)


# In[11]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# In[12]:


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[15]:


my_list = ["dona","doney","fathima"]
list1 = list(my_list)
print(list1)
print(list2)


# In[16]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[17]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[18]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# In[20]:


fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")


# In[23]:


points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
print(points)
print(x)


# In[24]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# In[25]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# In[26]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# In[1]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# In[3]:


a = {"Name" : "Fathima","Course" : "MCA","Year" : "2022-2024"}
print(a)


# In[5]:


a = {"Name" : "Fathima","Course" : "MCA","Year" : "2022-2024","name" : "fathima"}
print(a)
print(len(a))


# In[7]:


a = {"Name" : "Fathima","Course" : "MCA","Year" : "2022-2024"}
print(a)
print(len(a))


# In[13]:


cars = {"brand": ["Jeep","Ford","Audi","Hyundai"],"model": ["Compass","Mustang","A6","Tacson"] ,"year": [2007,2021,2023,2019]}
cars["brand"]
cars["model"]
cars["year"]


# In[14]:


cars = {"brand": ["Jeep","Ford","Audi","Hyundai"],"model": ["Compass","Mustang","A6","Tacson"] ,"year": [2007,2021,2023,2019]}
cars["brand"]


# In[15]:


cars = {"brand": ["Jeep","Ford","Audi","Hyundai"],"model": ["Compass","Mustang","A6","Tacson"] ,"year": [2007,2021,2023,2019]}
cars["model"]


# In[17]:


cars = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tacson"] ,
    "year": [2007,2021,2023,2019]
}
cars["year"]


# In[24]:


cars = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tucson"] ,
    "year": [2007,2021,2023,2019],
    "price":[2140000,7460000,6770000,2863000]
}
cars.get("model")


# In[26]:


cars = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tucson"] ,
    "year": [2007,2021,2023,2019],
    "price":[2140000,7460000,6770000,2863000]
}
cars.get("brand")


# In[27]:


cars.values()


# In[28]:


cars.keys()


# In[36]:


cars = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tucson"] ,
    "year": [2007,2021,2023,2019],
    "price":[2140000,7460000,6770000,2863000]
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
if "brand" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
x=cars["model"]
print(x)
y=cars["price"]
print(y)
z=cars["brand"]
print(z)
a=cars["year"]
print(a)


# In[3]:


school = {
    "names" = ["Rcss","Rset","Rbs"]
    "year" = (2001,2002,2003)
    "address" = ['Kalamasherry','Kakanad','Kochi']
 }
print(school)


# In[ ]:


mydetail ={
    'name':('Fathima Arakkal'),
    'age':[21],
    'gender':('Female')
    'address':[{'Thrissur','Kerala'}
}


# In[18]:


family = {
  "Father" : {
    "name" : "Shajahan Arakkal",
    "year" : 1967
  },
  "Mother" : {
    "name" : "Fousiya Shajahan",
    "year" : 1979
  },
  "Children" : {
    "name" : ["Aysha","Fathima","Mohammed"],
    "year" : [1999,2001,2008]
  }
    
}


# In[21]:


print(family)


# In[22]:


my_dict = {
    'integer': 42,
    'float': 3.14,
    'string': 'Hello, world!',
    'boolean': True,
    'list': [1, 2, 3],
    'tuple': (4, 5, 6),
    'set': {7, 8, 9},
    'dictionary': {'key': 'value'},
    'none': None
}


# In[26]:


print(my_dict)


# In[27]:


cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
cars["year"] = 2018


# In[28]:


print(cars)


# In[29]:


cars = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tucson"] ,
    "year": [2007,2021,2023,2019],
    "price":[2140000,7460000,6770000,2863000]
}
print(cars)


# In[32]:


cars= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
cars.update({"year": 2020})


# In[33]:


print(cars)


# In[39]:


car = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tucson"] ,
    "year": [2007,2021,2023,2019],
    "price":[2140000,7460000,6770000,2863000]
}
print(car)


# In[40]:


car.update({"price":2280000})
print(car)


# In[41]:


print(car)


# In[42]:


car


# In[43]:


car = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tucson"] ,
    "year": [2007,2021,2023,2019],
    "price":[2140000,7460000,6770000,2863000]
}
print(car)


# In[44]:


car


# In[45]:


car = {
  "brand": "Nissan",
  "model": "Patrol",
  "year": 2021
}
car.pop("model")
print(car)


# In[46]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)


# In[47]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del car["model"]
print(car)


# In[48]:


car = {
  "brand": "Nissan",
  "model": "Patrol",
  "year": 1964
}
car.clear()
print(car)


# In[53]:


car = {
    "brand": ["Jeep","Ford","Audi","Hyundai"],
    "model": ["Compass","Mustang","A6","Tucson"] ,
    "year": [2007,2021,2023,2019],
    "price":[2140000,7460000,6770000,2863000]
}
print(car)


# In[54]:


for x in car['brand']:
  print(x)


# In[55]:


for x in car['model']:
  print(x)


# In[56]:


for x in car['price']:
  print(x)


# In[57]:


for x in car['year']:
  print(x)


# In[58]:


for x in car:
  print(car[x])


# In[59]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# In[60]:


child1 = {
  "name" : "Aysha",
  "year" : 1999
}
child2 = {
  "name" : "Fathima",
  "year" : 2001
}
child3 = {
  "name" : "Mohammed",
  "year" : 2008
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# In[61]:


print(myfamily)


# In[62]:


print(myfamily["child2"]["name"])


# In[ ]:




