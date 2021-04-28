#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
from pyndamics3 import Simulation


# <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/29728a7d4bebe8197dca7d873d81b9dce954522e">

# In[10]:


sim=Simulation()
sim.add("S' = -β*S*I/N",100,plot=1)
sim.add("I' = +β*S*I/N - γ*I",1,plot=1)
sim.add("R' = +γ*I",plot=1)
sim.add("N = S+I+R",plot=1)

sim.params(β=.5,γ=.1)
sim.run(90)


# ## adding a function definition

# In[7]:


def β_vs_t(t,β0,β1,T):
    value = sin(2*pi*t/T)*β1 + β0
    return value


# In[9]:


sim=Simulation()
sim.add("S' = -β_vs_t(t,β0,β1,T)*S*I/N",100,plot=1)
sim.add("I' = +β_vs_t(t,β0,β1,T)*S*I/N - γ*I",1,plot=1)
sim.add("R' = +γ*R",plot=1)

sim.add("N = S+I+R",plot=1)

sim.params(β0=1,β1=0.5,T=10,γ=.8)
sim.functions(β_vs_t)
sim.run(50)


# In[ ]:




