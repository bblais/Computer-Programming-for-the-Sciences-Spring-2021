#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from pyndamics3 import Simulation


# In[4]:


import pandas as pd


# In[8]:


data=pd.read_csv('data/g149novickA.txt',header=None)


# In[13]:


x,y=array(data[0]),array(data[1])


# In[14]:


plot(x,y,'o')


# In[17]:


sim=Simulation()
sim.add("z' = S/τ - z/τ",0,plot=True)
sim.params(S=1,τ=1)
sim.add_data(t=x,z=y,plot=True)
sim.run(0,7)


# In[20]:


from pyndamics3.fit import fit,Parameter


# In[21]:


results=fit(sim,
   Parameter("S",value=1,min=0),
   Parameter("τ",value=1,min=0),
           )


# In[22]:


results


# In[23]:


sim.run(0,7)


# ## population data

# In[26]:


data=pd.read_csv('data/population_data.txt',sep='\t')


# In[28]:


data.head()


# In[30]:


x,y=array(data['Year']),array(data['World'])
plot(x,y,'o')


# In[50]:


sim=Simulation()
sim.add("p' = a*p",1,plot=True)
sim.params(a=.1)
sim.add_data(t=x,p=y,plot=True)
sim.run(0,2000)


# In[42]:


results=fit(sim,
   Parameter("a",value=0.001,min=0,max=0.1),
           )


# In[43]:


sim.run(0,2000)


# In[ ]:




