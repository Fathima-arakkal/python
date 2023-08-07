#!/usr/bin/env python
# coding: utf-8

# # Python Mysql
# 

# In[5]:


pip install mysql-connector-python


# In[6]:


import mysql.connector


# In[12]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)


# In[15]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


# In[16]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[18]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)


# In[19]:


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# In[20]:


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[22]:


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# In[23]:


mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[24]:


mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# In[25]:


mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[26]:


mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# In[27]:


mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)


# In[28]:


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[29]:


mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[30]:


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)


# In[33]:


mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[1]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# In[2]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# In[3]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


# In[4]:


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[5]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[7]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE cust (name VARCHAR(255), address VARCHAR(255))")


# In[8]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[9]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO cust (name, address) VALUES (%s, %s)"
val = [
  ('Dona', 'Mannuthi'),
  ('Doney','Kottayam'),
  ('Fathima','Kodungallur'),
  ('Gayathri Menon','Edappaly'),
  ('Gayathri Sunil','Kalamasherry'),
  ('Irin','Thrissur'),
  ('Jerusha','Pathanamthitta'),
  ('John Gilbert','Kakkanad'),
  ('Jovitta','Irinjalakuda'),
  ('Keerthana','Kochi'),
  ('Lakshmi','S.N Junction'),
  ('Lemin','Kumblangi'),
  ('Maria','Pallinada'),
  ('Althaf','Kaloor'),
  ('Nikhil','JLN'),
    
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# In[10]:


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cust")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[12]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fathima_python"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE student (name VARCHAR(255), address VARCHAR(255), age  VARCHAR(100),bloodgroup VARCHAR(255))")


# In[13]:


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[14]:


mycursor = mydb.cursor()

sql = "INSERT INTO student (name, address,age,bloodgroup) VALUES (%s, %s,%s,%s)"
val = [
  ('Dona', 'Mannuthi','21','A+'),
  ('Doney','Kottayam','23','B+'),
  ('Fathima','Kodungallur','21','AB+'),
  ('Gayathri Menon','Edappaly','22','B+'),
  ('Gayathri Sunil','Kalamasherry','21','B+'),
  ('Irin','Thrissur','23','O+'),
  ('Jerusha','Pathanamthitta','24','AB+'),
  ('John Gilbert','Kakkanad','23','O+'),
  ('Jovitta','Irinjalakuda','22','B+'),
  ('Keerthana','Kochi','24','A+'),
  ('Lakshmi','S.N Junction','25','B-'),
  ('Lemin','Kumblangi','25','O-'),
  ('Maria','Pallinada','23','A+'),
  ('Althaf','Kaloor','22','O+'),
  ('Nikhil','JLN','24','A+'),
    
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# In[15]:


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[16]:


mycursor = mydb.cursor()

sql = "UPDATE student SET address = 'Vytilla' WHERE address = 'Kochi'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


# In[17]:


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[18]:


mycursor = mydb.cursor()

sql = "DELETE FROM student WHERE address = 'JLN'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# In[19]:


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[ ]:




