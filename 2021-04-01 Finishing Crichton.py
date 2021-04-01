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


# In[5]:


time_series_folder='/Users/bblais/tex/bryant/spring_2021/computer_programming_378/Crichton Data/time series'
fnames=glob(time_series_folder+'/*.csv')
fnames=fnames[:10]


# In[6]:


len(fnames)


# In[7]:


fnames


# In[8]:


station_info=pd.read_excel('data/station_info.xlsx')
station_info.head()


# In[31]:


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

def station_name_from_filename(filename):
    import os
    parts=os.path.split(filename)
    base,ext=os.path.splitext(parts[-1])
    return base

def first_row(station_name):
    if '.csv' in station_name:
        station_name=station_name_from_filename(station_name)
    
    if not any(station_info['Station']==station_name):
        return None
    
    return station_info[station_info['Station']==station_name].iloc[0]    


# In[32]:


station_name='CARACAS-LA CARLOTA'
any(station_info['Station']==station_name)


# In[33]:


fnames=glob(time_series_folder+'/*.csv')
station_names_with_data=[station_name_from_filename(filename) for filename in fnames]
#fnames=fnames[:10]


# In[36]:


S=Storage()

count=0
for filename in fnames:
    data=Struct()
    data.slope=get_slope(filename)
    data.station=station_name_from_filename(filename)
    
    row=first_row(data.station)
    if row is None:
        count+=1
        continue
    if row.Brightness>=10:
        data.urban=True
    else:
        data.urban=False
    
    S+=data,
    
print("Could not find info for ",count)


# In[28]:


data.station


# In[86]:


first_row(station_name_from_filename(fnames[3]))


# In[87]:


first_row(fnames[3])


# In[84]:


fnames[3]


# In[ ]:




