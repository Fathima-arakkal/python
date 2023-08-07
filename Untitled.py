#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello Welcome")
    def deposit(self):
        amount = float(input("Enter the amount to deposit"))
        self.balance +=amount
        print("\n Amount deposited" ,amount)
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw"))
        if self.balance >= amount:
            self.balance -=amount;
            print("\n You have withdrawed", amount)
        else:
            print("\n Insufficient balance")
    def display(self):
        print("\n Current balance", self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()


# In[ ]:





# In[2]:


class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello Welcome")
    def deposit(self):
        amount = float(input("Enter the amount to deposit"))
        self.balance +=amount
        print("\n Amount deposited" ,amount)
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw"))
        if self.balance >= amount:
            self.balance -=amount:
            print("\n You have withdrawed", amount)
        else:
            print("\n Insufficient balance")
    def display(self):
        print("\n Current balance", self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()


# In[ ]:




