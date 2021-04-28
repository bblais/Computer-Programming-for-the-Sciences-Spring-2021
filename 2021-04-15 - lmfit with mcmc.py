#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().run_line_magic('pylab', 'inline')


# In[13]:


from sci378 import *


# In[14]:


import lmfit


# In[15]:


data=pd.read_csv('data/linear_data.csv')
data


# In[16]:


x=array(data['x'])
y=array(data['y'])
x,y


# ## Fit with lmfit

# In[17]:


model=lmfit.models.LinearModel()


# In[18]:


results=model.fit(y,x=x)
results


# In[25]:


model.independent_vars


# ## Retry lmfit with mcmc

# In[34]:


def lnlike(data,**kwargs):
    assert len(lmmodel.independent_vars)==1
    
    independent_vars={lmmodel.independent_vars[0]:x}
    x,y=data
    for key in kwargs:
        if key=='_σ':
            continue
        else:
            lmparams[key].value=kwargs[key]
    ys=lmmodel.eval(lmparams,**independent_vars)
    return lognormalpdf(ys-y,0,kwargs['_σ'])


# In[35]:


from sci378.stats import *


# In[36]:


lmmodel=lmfit.models.LinearModel()
lmparams=lmmodel.make_params()

model=MCMCModel((x,y),lnlike,
                slope=Uniform(-50,50),
                intercept=Uniform(-50,50),
                _σ=Jeffreys(),  # need to define this even though it isn't in your function
               )


# In[37]:


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




