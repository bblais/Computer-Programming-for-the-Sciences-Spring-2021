#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# In[38]:


def lnlike(data,**kwargs):
    assert len(lmmodel.independent_vars)==1
    
    x,y=data
    independent_vars={lmmodel.independent_vars[0]:x}
    for key in kwargs:
        if key=='_σ':
            continue
        else:
            lmparams[key].value=kwargs[key]
    ys=lmmodel.eval(lmparams,**independent_vars)
    return lognormalpdf(ys-y,0,kwargs['_σ'])


# In[39]:


from sci378.stats import *


# In[40]:


lmmodel=lmfit.models.LinearModel()
lmparams=lmmodel.make_params()

model=MCMCModel((x,y),lnlike,
                slope=Uniform(-50,50),
                intercept=Uniform(-50,50),
                _σ=Jeffreys(),  # need to define this even though it isn't in your function
               )


# In[41]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[42]:


model.plot_distributions()


# In[43]:


plot(x,y,'o')

x_fake=linspace(-6,6,20)
y_fake=results.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# In[44]:


model.triangle_plot()


# ## What if I do a custom function, and it uses $t$ as a variable?

# In[45]:


t=array(data['x'])
V=array(data['y'])
t,V


# In[47]:


def my_function(t,a=1,b=1,c=1):
    return a*t**2 + b*t + c


# In[50]:


model=lmfit.Model(my_function)


# In[51]:


results=model.fit(V,t=t)
results


# In[52]:


lmmodel=lmfit.Model(my_function)
lmparams=lmmodel.make_params()

model=MCMCModel((t,V),lnlike,
                a=Uniform(-50,50),
                b=Uniform(-50,50),
                c=Uniform(-50,50),
                _σ=Jeffreys(),  # need to define this even though it isn't in your function
               )


# In[53]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[54]:


model.plot_distributions()


# In[56]:


plot(t,V,'o')

t_fake=linspace(-6,6,20)
V_fake=results.eval(t=t_fake)
plot(t_fake,V_fake,'-')


# In[ ]:


plot(t,V,'o')

t_fake=linspace(-6,6,20)
V_fake=results.eval(t=t_fake)
plot(t_fake,V_fake,'-')


# ## still to do - get the functions to show the best-fit curves (95% levels) from mcmc

# In[ ]:




