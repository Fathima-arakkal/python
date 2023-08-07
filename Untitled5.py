#!/usr/bin/env python
# coding: utf-8

# In[1]:


thislist = ["apple", "banana", "cherry"]
print(thislist)


# In[6]:


a = ["Dona","Doney","Fathima"]
print(a)
print(a[1])
a.append("Gayathri")
print(a)


# In[8]:


b=["Fathima","Mca","Python"]
print(b)
b.append(2022-2024)
print(b)


# In[9]:


b=["Fathima","Mca","Python"]
print(b)
b.append(2022)
print(b)


# In[13]:


b=["Fathima","Mca","Python"]
print(b)
b.append(["Specialization","Web Security",2024])
print(b)
print(b[2])
print(b[2:6])
b.insert(1,"Dilsha")
print(b)


# In[14]:


c=[1,89,56,75,62]
b.extend(c)
print(b)


# In[15]:


len(b)


# In[16]:


type(b)


# In[18]:


b.extend(a)
print(b)


# In[20]:


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# In[21]:


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# In[22]:


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


# In[23]:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[24]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# In[25]:


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# In[26]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# In[27]:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# In[28]:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[29]:


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# In[30]:


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# In[31]:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[32]:


thislist = ["apple", "banana", "cherry"]
del thislist


# In[33]:


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# In[34]:


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[35]:


thislist = ["apple", "banana", "cherry","dona","doney","fathima"]
for x in thislist:
  print(x)


# In[36]:


thislist = ["apple", "banana", "cherry","dona","doney","fathima"]
for i in range(len(thislist)):
  print(thislist[i])


# In[37]:


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# In[38]:


thislist = ["apple", "banana", "cherry","dona","doney","fathima"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# In[39]:


thislist = ["apple", "banana", "cherry","dona","doney","fathima"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 2


# In[40]:


thislist = ["apple", "banana", "cherry","dona","doney","fathima"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 3


# In[41]:


thislist = ["apple", "banana", "cherry","dona","doney","fathima"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 4


# In[42]:


thislist = ["apple", "banana", "cherry"thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 5


# In[43]:


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# In[44]:


thislist = ["apple", "banana", "cherry","dona","doney","fathima"]
[print(x) for x in thislist]


# In[45]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# In[46]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango","dona","doney","fathima"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# In[49]:


friuts = ["aksa","bitty","christo","dona","eve","fathima","doney"]
new = []
for x in fruits:
 if "a" in x:
        newlist.append(x)
print(new)


# In[48]:


fruits = ["aksa","bitty","christo","dona","eve","fathima","doney"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# In[52]:


friuts = ["aksa","bitty","christo","dona","eve","fathima","doney"]
new = []
for x in fruits:
 if "a" in x:
   newlist.append(x)
print(new)


# In[53]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# In[54]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# In[56]:


newlist = [x for x in fruits if x != "apple"]


# In[57]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)


# In[58]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)


# In[59]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# In[60]:


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[61]:


thislist = ["Orange", "mango", "Kiwi", "pineapple", "Banana"]
thislist.sort()
print(thislist)


# In[62]:


thislist = ["oRange", "maNgo", "Kiwi", "pineaPple", "banana"]
thislist.sort()
print(thislist)


# In[63]:


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# In[65]:


def my_function():
  print("Hello from a function")


# In[66]:


def my_function():
  print("Hello from a function")

my_function()


# In[70]:


def my_function(fname):
  print(fname + " Arakkal")

my_function("Fathima")
my_function("Shajahan")
my_function("Abdurahiman")


# In[72]:


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
my_function("Fathima", "Arakkal")


# In[73]:


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# In[74]:


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Aysha", "Fathima", "Mohammed")


# In[75]:


def my_function(*kids):
  print("The Oldest child is " + kids[0])

my_function("Aysha", "Fathima", "Mohammed")


# In[76]:


def my_function(*kids):
  print("The Middle child is " + kids[1])

my_function("Aysha", "Fathima", "Mohammed")


# In[77]:


def my_function(*kids):
  print("The Oldest child is " + kids[0])
  print("The Middle child is " + kids[1])
  print("The youngest child is " + kids[2])

my_function("Aysha", "Fathima", "Mohammed")


# In[78]:


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# In[79]:


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Aysha", child2 = "Fathima", child3 = "Mohammed")


# In[81]:


def my_function(child3, child2, child1):
  print("The 3rd child is " + child3)
  print("The 2nd child is " + child2)
  print("The 1st child is " + child1)

my_function(child1 = "Aysha", child2 = "Fathima", child3 = "Mohammed")


# In[82]:


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# In[84]:


def my_function(lname = "Shajahan"):
  print("Arakkal " + lname)
my_function()
my_function("Fousiya")
my_function("Aysha")
my_function("Fathima")
my_function("Mohammed")


# In[85]:


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# In[86]:


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# In[87]:


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# In[ ]:




