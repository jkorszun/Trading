#!/usr/bin/env python
# coding: utf-8

# In[1]:


# define fractal function
def fractals(Data, high, low, up, down):
    
    # Fractal Up
    for i in range(len(Data)):
        if Data[i, high] < Data[i - 2, high] and Data[i - 1, high] < Data[i - 2, high] and Data[i - 2, high] > Data[i - 3, high] and Data[i - 2, high] > Data[i - 4, high]:
                Data[i - 2, up] = 1
   
    # Fractal Down
    for i in range(len(Data)):    
        if Data[i, low] > Data[i - 2, low] and Data[i - 1, low] > Data[i - 2, low] and Data[i - 2, low] < Data[i - 3, low] and Data[i - 2, low] < Data[i - 4, low]:        
                Data[i - 2, down] = -1   
    return Data


# In[2]:


# define bullish/bearish signal
def signal(Data):
    
    # Bullish Signal
    for i in range(len(Data)):
        
        if Data[i - 2, 5] != 0:
                
                Data[i, 6] = 1
   
    # Bearish Signal
    for i in range(len(Data)):
        
        if Data[i - 2, 4] != 0:
                
                Data[i, 7] = -1 
    return Data


# In[3]:


# create signals function 
def adder(Data, times):
    for i in range(1, times + 1):
        new = np.zeros((len(Data), 1), dtype = float)
        Data = np.append(Data, new, axis = 1)
    return Data
def deleter(Data, index, times):
    for i in range(1, times + 1):
        Data = np.delete(Data, index, axis = 1)
    return Data
def jump(Data, jump):
    Data = Data[jump:, ]
    return Data


# In[ ]:




