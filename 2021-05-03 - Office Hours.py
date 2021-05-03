#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# In[3]:


import pandas as pd


# In[4]:


data=pd.read_excel('/Users/bblais/Downloads/lynxhare.xlsx')
data


# In[14]:


t_data=array(data['year'])
y_data=array(data['hare'])

y_data=y_data[t_data<=1935]
t_data=t_data[t_data<=1935]
t_data=t_data-min(t_data)
y_data=y_data-mean(y_data)
t_data,y_data


# In[15]:


plot(t_data,y_data,'o-')


# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


sim=Simulation()
sim.add("x'=v",100000,plot=True)
sim.add("v'=-k*x/m",0,plot=False)
sim.params(m=1,k=1.5)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(0,90)


# In[28]:


plot(t_data,y_data,'-o')
plot(sim.t,sim.x,'-')


# In[ ]:




