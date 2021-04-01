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

# In[96]:


data=pd.read_csv('data/time series data pandas.csv.zip')
data


# In[97]:


#data.to_excel('test.xlsx')


# In[25]:


station_info=pd.read_excel('data/station_info_updated.xlsx')
station_info.shape


# In[26]:


station_info.head()


# In[54]:


station_info[station_info['Brightness']<10]


# In[58]:


def get_slope(name,plotit=False):
    subdata=data[['time',name]].dropna()
    x_data=subdata['time']
    y_data=subdata[name]
    model=models.LinearModel()
    result=model.fit(y_data,x=x_data)
    
    if plotit:
        plot(x_data,y_data,'o')

        x_fake=linspace(1960,2020,100)
        y_fake=result.eval(x=x_fake)
        plot(x_fake,y_fake,'-')
        title(name)
    
    return result.params['slope'].value


def first_row(name):
    return station_info[station_info['Station']==name].iloc[0]    


# In[59]:


get_slope('MAZAR_I_SHARIF'),first_row('MAZAR_I_SHARIF')


# In[61]:


from tqdm import tqdm


# In[62]:


S=Storage()
slope_data={}

for name in tqdm(station_info['Station']):
    data1=Struct()
    data1.slope=get_slope(name)
    data1.station=name
    
    row=first_row(name)
    if row.Brightness>=10:
        data1.urban=True
    else:
        data1.urban=False
        
    data1.latitude=row.Latitude
    data1.longitude=row.Longitude
    
    slope_data[name]=data1
    


# In[ ]:





# In[64]:


all([slope_data[_].urban for _ in slope_data])


# In[65]:


def closest_rural(urban_name):
    min_distance=1e500
    min_name=None
    
    for name in station_info['Station']:
        if slope_data[name].urban:
            continue # skip the urbans
            
        x1,y1=slope_data[name].latitude,slope_data[name].longitude
        x2,y2=slope_data[urban_name].latitude,slope_data[urban_name].longitude
        distance=sqrt((x1-x2)**2+(y1-y2)**2)
        
        if distance<min_distance:
            min_distance=distance
            min_name=name
            
    return min_name
    


# In[73]:


for name in tqdm(slope_data):
        
    if slope_data[name].urban:
        rural_name=closest_rural(name)
        slope_data[name].closest_rural_name=rural_name
        slope_data[name].closest_rural_slope=slope_data[rural_name].slope
    else:
        continue
        
    
    


# In[76]:


urban_slope=array([slope_data[_].slope for _ in slope_data if slope_data[_].urban])
nearby_rural_slope=array([slope_data[_].closest_rural_slope for _ in slope_data if slope_data[_].urban])
rural_slope=array([slope_data[_].slope for _ in slope_data if not slope_data[_].urban])


# In[98]:


len(urban_slope)


# In[102]:


histogram(urban_slope,500);
histogram(rural_slope,500);
xlim([-.1,.1])
xlabel('slope')
mean(urban_slope),mean(rural_slope)


# In[103]:


figure(figsize=(8,8))
plot([0],[0],'o',alpha=0.2)
axis('equal')
xlabel('urban slope')
ylabel('rural slope')
plot([0,0],[-.7,.7],'k')
plot([-.7,.7],[0,0],'k')
xlim([-.3,.3])
ylim([-.3,.3])


# In[105]:


figure(figsize=(8,8))
plot(urban_slope,nearby_rural_slope,'o',alpha=0.1)
axis('equal')
xlabel('urban slope')
ylabel('rural slope')
plot([0,0],[-.7,.7],'k')
plot([-.7,.7],[0,0],'k')
xlim([-.3,.3])
ylim([-.3,.3])


# In[ ]:




