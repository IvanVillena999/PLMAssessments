#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time 

def pause():
    for i in range(10, 0, -1): 
        print(f"The program will end in {i}...")
        time.sleep(1)


# In[ ]:


#pause() was removed


# In[5]:


def current_time(): 
    t = time.strftime("%I:%M %p")
    return t


# In[ ]:


#current_time was removed


# In[6]:


def current_date():
    d = time.strftime("%b %d %Y")
    return d


# In[ ]:


#current_date was removed


# In[ ]:




