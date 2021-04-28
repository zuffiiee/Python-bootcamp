#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[23]:


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
        
    
    def distance(self):
        return ((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**0.5
    
    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])


# Can also do tuple unpacking as,
# 
# x1,y1=self.coor1
# 
# 
# x2,y2= self.coor2
# 

# In[27]:


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[25]:


li.distance()


# In[26]:


li.slope()


# In[4]:


class Cylinder:
    pi=3.14
    
    def __init__(self,height=1,radius=1):
        self.radius=radius
        self.height=height
        
    def volume(self):
        return self.pi*(self.radius**2)*self.height
    
    def surface_area(self):
        return self.pi*2*self.radius*(self.radius+self.height)


# In[8]:


c = Cylinder()


# In[9]:


c.volume()


# In[10]:


c.surface_area()


# In[ ]:





# In[75]:


class Account:
    def __init__(self,owner,balance):
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


# In[ ]:




