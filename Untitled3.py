#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
add = a + b
sub = a - b
mul = a * b
div = a / b
print("Addition",add)
print("Subtraction",sub)
print("Multiplication",mul)
print("Division",div)


# In[10]:


a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
c=input("1. Add,2. Sub,3. Mul,4. Div\n")
if (c== "1" or c == "add"):
    print(("Addition", a + b)
    
elif(c== "2" or c == "sub"):
          print(("Subtraction", a - b)
    
elif(c== "3" or c == "mul"):
                print(("Multipilcation", a * b)
    
elif(c== "4" or c == "div"):
                      print(("Division", a / b)
    
else :
                            print("invalid")
    


# In[ ]:


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    print("---- Menu ----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid input. Please try again.")
        continue

    print("Result:", result)


# In[ ]:


a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=input("enter 1.add,2.sub,3.mul,4.div")
if(c=="1"):
    print("add",int(a+b))
elif(c=="2"):
    print("sub",a-b)
elif(c=="3"):
    print("mul",a*b)
elif(c=="4"):
    print("div",a/b)
else:
    print("invalid error")
    


# In[ ]:


a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=input("enter 1.add,2.sub,3.mul,4.div")
if(c=="1"):
    print("add",int(a+b))
elif(c=="2"):
    print("sub",a-b)
elif(c=="3"):
    print("mul",a*b)
elif(c=="4"):
    print("div",a/b)
else:
    print("invalid error")


# In[ ]:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# In[ ]:


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


# In[ ]:





# In[ ]:




