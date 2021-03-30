#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# In[6]:


data=pd.read_csv('data/HIVseries.csv',header=None)
data


# In[23]:


t_data=array(data[0])
V_data=array(data[1])


# In[24]:


plot(t_data,V_data,'o')


# In[25]:


def doubleexp(t,A=1,α=1,B=1,β=1):
    return A*exp(-α*t) + B*exp(-β*t)


# In[27]:


t_fake=linspace(0,7,100)
V_fake=doubleexp(t_fake,A=175000,α=.5,B=25000,β=.1)
plot(t_fake,V_fake,'-')
plot(t_data,V_data,'o')


# In[59]:


model=Model(doubleexp)
model.param_names


# In[64]:


params=model.make_params()
params['A']=Parameter("A",min=0,value=175000)
params['α']=Parameter("α",min=0,value=.1)
params['β']=Parameter("β",min=0,value=1)
params['B']=Parameter("B",min=0,value=25000)


# In[65]:


result = model.fit(V_data, params, t=t_data)


# In[ ]:





# In[66]:


result


# In[67]:


plot(t_data,V_data,'o')

t_fake=linspace(0,7,1000)
V_fake=result.eval(t=t_fake)
plot(t_fake,V_fake,'-')


# ## plotting a sign function

# In[50]:


x=linspace(0,5,1000)


# In[51]:


y=sin(3*x)


# In[52]:


figure(figsize=(10,5))
plot(x,y,'-')


# In[ ]:




