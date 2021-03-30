#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# ## Crichton problem

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

# In[4]:


from glob import glob


# In[15]:


time_series_folder='/Users/bblais/Desktop/time series'
fnames=glob(time_series_folder+'/*.csv')
fnames=fnames[:10]


# In[16]:


len(fnames)


# In[17]:


fnames


# In[18]:


station_info=pd.read_excel('data/station_info.xlsx')
station_info.head()


# In[19]:


fname=fnames[0]


# In[25]:


data=pd.read_csv(fname)
data=data.dropna()
x_data=data['Year']
y_data=data['Temperature']
data


# In[26]:


model=models.LinearModel()
result=model.fit(y_data,x=x_data)


# In[27]:


result


# In[28]:


plot(x_data,y_data,'o')

x_fake=linspace(1960,2020,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# In[31]:


result.params['slope'].value


# In[34]:


def get_slope(fname,plotit=False):
    data=pd.read_csv(fname)
    data=data.dropna()
    x_data=data['Year']
    y_data=data['Temperature']
    model=models.LinearModel()
    result=model.fit(y_data,x=x_data)
    
    if plotit:
        plot(x_data,y_data,'o')

        x_fake=linspace(1960,2020,100)
        y_fake=result.eval(x=x_fake)
        plot(x_fake,y_fake,'-')        
    
    return result.params['slope'].value


# In[37]:


get_slope(fname)


# In[38]:


def myfunction(x,a=1):
    return x+a


# In[41]:


myfunction(7,10)


# In[44]:


time_series_folder='/Users/bblais/Desktop/time series'
fnames=glob(time_series_folder+'/*.csv')
#fnames=fnames[:10]


# In[45]:


S=Storage()

for filename in fnames:
    value=get_slope(filename)
    #print(filename,value)
    
    S+=value,

slopes=S.arrays()
slopes


# In[50]:


station_names=list(station_info['Station'])


# In[51]:


len(station_names)


# In[52]:


name=station_names[0]
name


# In[53]:


glob(time_series_folder+"/"+name+".csv")


# In[58]:


station_info[station_info['Station']==name].iloc[0]  # gets the first row matching name


# In[59]:


fnames[:10]


# In[60]:


fname=fnames[0]
fname


# In[66]:


import os


# In[68]:


parts=os.path.split(fname)
parts


# In[69]:


parts[-1]


# In[71]:


print("hello\there\n")


# In[72]:


base,ext=os.path.splitext(parts[-1])


# In[73]:


base


# In[74]:


ext


# In[75]:


def station_name_from_filename(filename):
    parts=os.path.split(filename)
    base,ext=os.path.splitext(parts[-1])
    return base


# In[78]:


station_name_from_filename(fnames[3])


# In[85]:


def first_row(station_name):
    if '.csv' in station_name:
        station_name=station_name_from_filename(station_name)
    
    return station_info[station_info['Station']==station_name].iloc[0]    


# In[86]:


first_row(station_name_from_filename(fnames[3]))


# In[87]:


first_row(fnames[3])


# In[84]:


fnames[3]


# In[ ]:




