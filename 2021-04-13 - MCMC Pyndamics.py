#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# In[3]:



t=array([7,14,21,28,35,42,49,56,63,70,77,84],float)
h=array([17.93,36.36,67.76,98.10,131,169.5,205.5,228.3,247.1,250.5,253.8,254.5])

plot(t,h,'-o')
xlabel('Days')
ylabel('Height [cm]')


# In[4]:


sim=Simulation()
sim.add("h' = a*h*(1-h/K)",1,plot=True)
sim.params(a= 1 , K= 260 )
sim.add_data(t=t,h=h,plot=True)
sim.run(80)


# In[5]:


from pyndamics3.mcmc import *


# In[6]:


model=MCMCModel(sim,
               a=Uniform(0,2),
               K=Uniform(50,500),)


# In[7]:


model.run_mcmc(300,repeat=3)
model.plot_chains()


# In[8]:


samples=model.samples
samples.shape


# In[ ]:





# In[ ]:





# In[12]:


model.plot_distributions()


# In[13]:


sim.run(80)


# In[14]:


model=MCMCModel(sim,
               a=Uniform(0,2),
               K=Uniform(50,500),
               initial_h=Uniform(0,50),)


# In[15]:


model.run_mcmc(300,repeat=3)
model.plot_chains()


# In[16]:


model.plot_distributions()


# In[17]:


sim.run(80)


# In[ ]:




