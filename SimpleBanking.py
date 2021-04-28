#!/usr/bin/env python
# coding: utf-8

# In[ ]:

class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
    def deposit(self,amt):
        self.balance=self.balance+amt
        print(f"Account credited with ${amt}.Balance:${self.balance}")
    
    def withdraw(self,wamt):
        bal=self.balance-wamt
        if bal>=0:
            self.balance=bal
            print(f"Account debited with ${wamt}.Balance:${self.balance}")
        else:
            print(f"Do not have enough balance.Can only withdraw ${self.balance}")
            

# In[76]:
acct1 = Account('Jose',100)


# In[77]:
print(acct1)


# In[78]:
acct1.deposit(10)


# In[79]:
acct1.withdraw(60)


# In[80]:
acct1.withdraw(60)

