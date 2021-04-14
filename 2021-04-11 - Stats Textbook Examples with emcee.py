#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378.stats import *


# # Single Population

# ## Normal noise + known $\sigma$

# ![image.png](attachment:2bb8c0f4-1de0-4e33-87ed-1e28e6d5007d.png)
# ![image.png](attachment:e3ce6a1e-f0d7-4dca-98e2-a00fbefad45b.png)

# $$
# \begin{eqnarray}
# x_i &\sim& \mu + \epsilon_i \\
# P(x_i|\mu,\sigma) &\sim& \text{Normal}(\mu,\sigma) 
# \end{eqnarray}
# $$
# known $\sigma$

# $$
# \begin{eqnarray}
# P(\mu|{x_i},\sigma) \sim P({x_i}|\mu,\sigma) P(\mu|\sigma)
# \end{eqnarray}
# $$

# In[3]:


def lnlike(data,μ):
    # known σ
    x=data
    return lognormalpdf(x,μ,σ)


# In[4]:


data=array([12.0,14,16])
σ=1
model=MCMCModel(data,lnlike,
                μ=Uniform(-50,50),
                )


# In[5]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[6]:


model.plot_distributions()


# compare to textbook solution

# In[7]:


x,y=model.get_distribution('μ')
plot(x,y,'-')
μ̂=mean(data)
N=len(data)
σμ=σ/sqrt(N)
y_pred=[exp(lognormalpdf(_,μ̂,σμ)) for _ in x]
plot(x,y_pred,'r--')


# In[8]:


model.P('μ>15')


# ## Normal noise + unknown $\sigma$

# In[9]:


def lnlike(data,μ,σ):
    x=data
    return lognormalpdf(x,μ,σ)


# In[10]:


data=array([12.0,14,16])
model=MCMCModel(data,lnlike,
                μ=Uniform(-50,50),
                σ=Jeffreys()
                )


# In[11]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[12]:


model.plot_distributions()


# In[13]:


model.percentiles([2.5,50,97.5])


# In[14]:


model.triangle_plot()


# ### compare to textbook

# In[16]:


x,y=model.get_distribution('μ')


# In[31]:


plot(x,y,'-')
μ̂=mean(data)
N=len(data)

σμ=std(data,ddof=1)/sqrt(N)
y_pred=[exp(logtpdf(_,N-1,μ̂,σμ)) for _ in x]
plot(x,y_pred,'r--')


# In[39]:


# In[20]:




x,y=model.get_distribution('σ',bins=800)


# In[55]:


plot(x,y,'-')

V=((data-data.mean())**2).sum()
logp=-N*log(x)-V/2/x**2
y_pred=exp(logp)
dx=x[1]-x[0]
y_pred=y_pred/y_pred.sum()/dx

plot(x,y_pred,'r--')


# In[ ]:
xlim([0,20])


# ## Proportion
# 
# data: $h$, $N$
# 
# $$
# P(\theta|h,N) \sim \text{Bernoulli}(\theta,h,N)
# $$
# 

# In[3]:


def lnlike(data,θ):
    h,N=data
    return logbernoullipdf(θ,h,N)


# In[4]:


data=3,12
model=MCMCModel(data,lnlike,
                θ=Uniform(0,1),
                )


# In[5]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[6]:


model.plot_distributions()


# In[7]:


model.P("θ <0.5")


# # Jaynes and Confidence Intervals
# 
# https://bayes.wustl.edu/etj/articles/confidence.pdf
# 
# ## Exponential
# 
# 
# ![image.png](attachment:c5d80fba-78d8-4104-8229-a0236563ef55.png)
# 
# ![image.png](attachment:d8d54cc2-e339-4695-8a2f-151c32219820.png)
# 
# bb: What *can't* $\theta$ be, given this data?

# In[16]:


def lnlike(data,θ):
    x=data
    d=θ-x
    d[d>0]=-np.inf
    return np.sum(d)


# In[18]:


data=array([12.0,14,16])
model=MCMCModel(data,lnlike,
                θ=Uniform(-50,50),
                )


# In[19]:


model.run_mcmc(1500,repeat=3)
model.plot_chains()


# In[20]:


model.plot_distributions()


# ### Frequentist Solution
# 
# ![image.png](attachment:d2e89adb-c071-4720-b1d1-106dd8f48622.png)
# 
# ![image.png](attachment:99e2adfb-c551-406b-90e7-c8f4e472f6a7.png)
# 
# ![image.png](attachment:f21f12b6-5024-4134-b3e3-2555c39cf1ed.png)

# ## Cauchy Distribution
# 
# ![image.png](attachment:4d0b52f9-12aa-4ee1-83e3-9b4cfd72a6ee.png)
# 
# -----
# 
# ![image.png](attachment:940b6424-e573-4336-ad9e-c144d8a0c7b2.png)
# 
# -----

# In[3]:


x=linspace(-5,15,500)
y=D.cauchy.pdf(x,loc=5,scale=1)

plot(x,y,color='orange',label='Cauchy')

y=D.norm.pdf(x,loc=5,scale=1)
plot(x,y,label='Normall')

legend()


# In[4]:


def lnlike(data,μ,σ):
    x=data
    return logcauchypdf(x,μ,σ)


# In[5]:


data=array([3.,5])
model=MCMCModel(data,lnlike,
                μ=Uniform(-50,50),
                σ=Jeffreys()
                )


# In[6]:


model.run_mcmc(1500,repeat=3)
model.plot_chains()


# In[7]:


model.plot_distributions()


# # Two Populations

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
from sci378.stats import *


# ![image.png](attachment:140b13c2-4b12-446c-8da2-e209f0d1e9a5.png)

# In[2]:


def lnlike(data,μ1,σ1,μ2,σ2):
    x1,x2=data
    return lognormalpdf(x1,μ1,σ1)+lognormalpdf(x2,μ2,σ2)


# In[3]:


data1=array([10.,11,12])
data2=array([12.,14,16])


# In[4]:


model=MCMCModel((data1,data2),lnlike,
                μ1=Uniform(-50,50),
                σ1=Jeffreys(),
                μ2=Uniform(-50,50),
                σ2=Jeffreys()
               )


# In[5]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[6]:


model.plot_distributions()


# In[8]:


model.best_estimates()


# In[9]:


model.plot_distributions('μ1-μ2')


# In[10]:


model.P('(μ1-μ2)>0.0')


# ## Paired

# In[11]:


def lnlike(data,μ,σ):
    x1,x2=data
    return lognormalpdf(x1-x2,μ,σ)


# In[12]:


model=MCMCModel((data1,data2),lnlike,
                μ=Uniform(-50,50),
                σ=Jeffreys(),
               )


# In[13]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[14]:


model.plot_distributions()


# In[15]:


model.P('μ<0')


# ## BEST Test

# https://jkkweb.sitehost.iu.edu/BEST/
# 
# ![image.png](attachment:a45bd817-6a7f-4b71-996a-8e8bf0fdfd88.png)

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378.stats import *


# In[10]:


drug = (101,100,102,104,102,97,105,105,98,101,100,123,105,103,100,95,102,106,
        109,102,82,102,100,102,102,101,102,102,103,103,97,97,103,101,97,104,
        96,103,124,101,101,100,101,101,104,100,101)
placebo = (99,101,100,101,102,100,97,101,104,101,102,102,100,105,88,101,100,
           104,100,100,100,101,102,103,97,101,101,100,101,99,101,100,100,
           101,100,99,101,100,102,99,100,99)

data1=drug
data2=placebo

pooled=np.concatenate((data1,data2))
M=pooled.mean()
S=pooled.std()


def lnprior(μ1,σ1,μ2,σ2,ν):
    value=0.0
    value+=lognormalpdf(μ1,M,1000*S)
    value+=lognormalpdf(μ2,M,1000*S)

    mn=0.001*S
    mx=1000*S
    value+=loguniformpdf(σ1,mn,mx-mn)
    value+=loguniformpdf(σ2,mn,mx-mn)

    value+=logexponpdf2(ν-1,scale=29)
    return value


def lnlike(data,μ1,σ1,μ2,σ2,ν):
    x1,x2=data
    value=0.0
    value+=logtpdf(x1,ν,μ1,σ1)
    value+=logtpdf(x2,ν,μ2,σ2)
        
    return value

model=MCMCModel((data1,data2),lnlike,
                lnprior,
                μ1=M,  # starting values for MCMC
                μ2=M,
                σ1=S,
                σ2=S,
                ν=10,
               )


# In[11]:


model.params


# In[12]:


model.run_mcmc(800,repeat=3)
model.plot_chains()


# In[13]:


model.plot_distributions()


# In[14]:


model.plot_distributions('μ1-μ2')


# In[19]:


model.plot_distributions('σ1-σ2')
t=gca().get_title()
title('Difference of sigma '+t)


# In[27]:


model.plot_distributions('(μ1-μ2)/sqrt((σ1**2+σ2**2)/2)')


# In[28]:


import arviz as az


# In[37]:


inference=az.from_emcee(model.sampler,model.params)


# In[38]:


az.plot_posterior(inference);


# In[ ]:




