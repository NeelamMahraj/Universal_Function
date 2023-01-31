#!/usr/bin/env python
# coding: utf-8

# # 20 UNIVERSAL FUNCTION OF NUMPY

# In[8]:


# Unary Universal Functions of Numpy
import numpy as np
a = np.arange(1,11)
a


# In[9]:


#Compute square root
np.sqrt(a)


# In[10]:


#compute exponential value
np.exp(a)


# In[14]:


# Natural logarithm base e,log10,log2 and log1p
np.log(a)
print(a)
np.log10(a)
print(a)
np.log2(a)
print(a)
np.log1p(a)
print(a)


# In[15]:


#compute the sign of each element(1=+ve,0=-ve,-1=-ve)
np.sign(a)


# In[20]:


#new array
a1 = np.arange(0.1,10.1)
print(a1)


# In[24]:


# Compute the ceiling of each element(i.e. the smaller integer is greater or equal to that number) 
np.ceil(a1)


# In[22]:


# Compute the floor of each element(i.e. the largest integer is less or equal to that number) 
np.floor(a1)


# In[25]:


# Round elements to the nearest interger 
np.rint(a1)


# In[26]:


# Return fractional or integer parts as a separate array
np.modf(a1)


# In[27]:


# Return boolean array indicating weather each value is NaN (Not a Number)
np.isnan(a1)


# In[28]:


# Return boolean array indicating weather each element is finite
np.isfinite(a1)


# In[29]:


# Return boolean array indicating weather each element is infinite
np.isinf(a1)


# In[31]:


# Binary Universal Functions of Numpy

x = np.arange(1,20)
y = np.arange(1.5,20.5)
print(x)
print(y)


# In[32]:


# add coresponding elements in arrays
np.add(x,y)


# In[34]:


# subtract coresponding elements in arrays
np.subtract(x,y)


# In[35]:


# multiply coresponding elements in arrays
np.multiply(x,y)


# In[36]:


# divide coresponding elements in arrays
np.divide(x,y)


# In[37]:


# maximum elements
np.maximum(x,y)


# In[38]:


# minimum elements
np.minimum(x,y)


# In[39]:


#Raise element in first array to powersindicated second array
np.power(x,y)


# In[40]:


# Reminder of division
np.mod(x,y)


# In[41]:


# Copy sign of values in second argument to values in first argument
np.copysign(x,y)


# In[ ]:




