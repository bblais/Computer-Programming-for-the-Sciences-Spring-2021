#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# In[14]:


sim = Simulation()
sim.add(("Ih'=a*Im*(1-Ih)-b*Ih"),0,plot=True)
sim.add(("Im'=c*Ih*(1-Im)-d*Im"), .1, plot=True)
sim.params(a=.1, b=0.2,  c=0.5, d=.3)
sim.run(100)


# In[ ]:




