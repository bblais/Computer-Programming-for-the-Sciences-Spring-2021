#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


import lmfit


# In[4]:


data=pd.read_csv('data/linear_data.csv')
data


# In[5]:


x=array(data['x'])
y=array(data['y'])
x,y


# ## Fit with lmfit

# In[6]:


model=lmfit.models.LinearModel()


# In[7]:


results=model.fit(y,x=x)
results


# ## Retry lmfit with mcmc

# In[8]:


def lnlike(data,**kwargs):
    x,y=data
    for key in kwargs:
        if key=='_σ':
            continue
        else:
            lmparams[key].value=kwargs[key]
    ys=lmmodel.eval(lmparams,x=x)
    return lognormalpdf(ys-y,0,kwargs['_σ'])


# In[9]:


from sci378.stats import *


# In[10]:


lmmodel=lmfit.models.LinearModel()
lmparams=lmmodel.make_params()

model=MCMCModel((x,y),lnlike,
                slope=Uniform(-50,50),
                intercept=Uniform(-50,50),
                _σ=Jeffreys(),  # need to define this even though it isn't in your function
               )


# In[11]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[12]:


model.plot_distributions()


# In[13]:


plot(x,y,'o')

x_fake=linspace(-6,6,20)
y_fake=results.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# In[14]:


model.triangle_plot()


# In[ ]:




