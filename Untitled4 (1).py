#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 1
y = 2.8
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# In[2]:


import random

print(random.randrange(1, 10))


# In[3]:


import random

print(random.randrange(1, 100))


# In[4]:


import random

print(random.randrange(1, 10))


# In[5]:


import random

print(random.randrange(1, 10))


# In[6]:


import random

print(random.randrange(1, 60))


# In[7]:


import random

print(random.randrange(1, 61))


# In[8]:


name="Fathima Arakkal Shajahan"
for x in name:
    print(x)


# In[9]:


name="Fathima Arakkal Shajahan"
for x in name:
    print(x[0])


# In[10]:


a = "fathima arakkal shajahan"
print(a[1])


# In[14]:


a = "fathima arakkal shajahan"
print(a[9])


# In[18]:


name = "Fathima Arakkal Shajahan"
print("Arakkal" not in name)


# In[19]:


name = "Fathima Arakkal Shajahan"
print(name[0:5])


# In[23]:


name = "Fathima Arakkal Shajahan"
print(name[-6:-13])


# In[20]:


name = "Fathima Arakkal Shajahan"
print(name[0:5])
print("fath" not in name)


# In[21]:


name = "Fathima Arakkal Shajahan"
print(name[0:5])
print("Fath" not in name)


# In[24]:


name = "Fathima Arakkal Shajahan"
print(name[-6:-13])


# In[25]:


name = "Fathima Arakkal Shajahan"
print(name[-0:-5])


# In[26]:


name = "Fathima Arakkal Shajahan"
print(name[-9:-2])


# In[27]:


a = "fathima"
print(a.upper())


# In[28]:


a = "FATHIMA"
print(a.lower())


# In[29]:


a = "  FATHIMA aRAKKAL sHAJAHAN"
print(a.strip()) # returns "Hello, World!"


# In[30]:


a = "Fathima Arkkal Shajahan"
print(a.replace("H", "J"))


# In[31]:


a = "FATHIMA ARAKKAL SHAJAHAN"
print(a.replace("A", "J"))


# In[32]:


a = "Fathima Arakkal Shajahan"
print(a.split(",")) # returns ['Hello', ' World!']


# In[33]:


a = "FATHIMA ARAKKAL SHAJAHAN"
print(a.replace("A", "x"))


# In[ ]:




