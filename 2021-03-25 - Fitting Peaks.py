#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


import pandas as pd


# In[3]:


data=pd.read_csv('data/peak data csv/sample0.csv')


# In[4]:


data.head()


# In[5]:


t=array(data.t)
y=array(data.y)


# In[6]:


plot(t,y,'o')


# In[7]:


from lmfit import *


# In[8]:


model=models.GaussianModel()


# In[9]:


results=model.fit(y,x=t,amplitude=1e7,center=1,sigma=1)
results


# In[13]:


x_fake=linspace(0,2,2000)
y_fake=results.eval(x=x_fake)
plot(t,y,'o')
plot(x_fake,y_fake,'-')
xlim([.9,1.3])


# In[14]:


results.best_values


# In[17]:


results.params['amplitude'].value


# In[18]:


p=results.params['amplitude']


# In[19]:


p.value


# In[20]:


p.stderr


# ## Outline
# 
# Goal: find the amplitudes for all of the peaks in the peak data csv folder.

# - get list of the files
# - for each of the files do... (call the current file "filename")
# 
#     - load the file (x,y)
#     - fit the data
#     - get the amplitude information
#     - store that amplitude information

# In[23]:


def get_amplitude(filename):
    data=pd.read_csv(filename)
    t=array(data.t)
    y=array(data.y)    
    model=models.GaussianModel()
    results=model.fit(y,x=t,amplitude=1e7,center=1,sigma=1)

    p=results.params['amplitude']
    
    return p.value


# In[24]:


value=get_amplitude('data/peak data csv/sample0.csv')
value


# In[25]:


from sci378 import Storage


# In[ ]:


S=Storage()

for filename in ['data/peak data csv/sample0.csv','data/peak data csv/sample1.csv','data/peak data csv/sample2.csv']:
    pass


# In[29]:


S=Storage()

for filename in ['data/peak data csv/sample0.csv',
                 'data/peak data csv/sample1.csv',
                 'data/peak data csv/sample2.csv',
                ]:
    value=get_amplitude(filename)
    print(filename,value)
    
    S+=value,

amplitudes=S.arrays()
amplitudes


# In[30]:


from glob import glob


# In[33]:


glob('data/*.txt')


# In[34]:


glob('data/*.zip')


# In[35]:


S=Storage()

for filename in glob('data/peak data csv/*.csv'):
    value=get_amplitude(filename)
    #print(filename,value)
    
    S+=value,

amplitudes=S.arrays()
amplitudes


# ## Michael Crichton

# - need temperature vs time data for all of the station (csv files in one folder)
# - need rural/urban info for each station
# - location (latitude, logitude) for each station
# 
# 
# - for each file do ....
#     - load data
#     - fit to a line
#     - get the slope of the line
#     - store those values
# 
# 
# - average of all the slopes?  (X)
# - count all positives/negatives for rural, urban -- fraction of positive for rural vs urban
# - average urban average rural, look statistical test on the average
# 
# - go through all the urban stations
#     - find the closest rural station
#     - I already have the slopes - rural slope value, and an urban slope value
#     
# - plot the difference (histogram)
# - plot rural slope (y-axis) vs urban slope (x-axis)
# 

# In[ ]:




