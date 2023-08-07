#!/usr/bin/env python
# coding: utf-8

# In[1]:


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero."
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# In[ ]:


a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
add = a + b
sub = a - b
mul = a * b
div = a / b
print(add)
print(sub)
print(mul)
print(div)

