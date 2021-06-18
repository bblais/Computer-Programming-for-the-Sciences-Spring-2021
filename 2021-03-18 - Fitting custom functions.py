#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from lmfit import *


# See: https://lmfit.github.io/lmfit-py/builtin_models.html  for more examples

# In[3]:


x_data,y_data=(array([-10.        ,  -8.94736842,  -7.89473684,  -6.84210526,
         -5.78947368,  -4.73684211,  -3.68421053,  -2.63157895,
         -1.57894737,  -0.52631579,   0.52631579,   1.57894737,
          2.63157895,   3.68421053,   4.73684211,   5.78947368,
          6.84210526,   7.89473684,   8.94736842,  10.        ]),
 array([ 84.5439605 ,  79.96429095,  53.29446178,  15.49595419,
         55.59294258,  57.74976334, -17.47795207,  19.03107704,
        -31.19976545, -10.54910001,  17.56865009,   5.42434731,
         -9.60203555,  21.4654494 ,  44.94972133,   6.80172884,
         62.75223289,  58.16212626, 111.04251023,  83.52494712]))


# In[4]:


plot(x_data,y_data,'o')


# ## Step 1 - define the function

# In[5]:


def quad(x,a=1,b=1,c=1):
    return a*x**2 + b*x + c


# ## Step 2 - define the model and construct the parameter list

# In[6]:


qmodel=Model(quad)


# In[7]:


qmodel.param_names


# In[8]:


params=qmodel.make_params()
params


# ## Step 3 - modify the parameter list (min, max, etc...) as needed

# In[9]:


params['a']=Parameter("a",min=0,value=0.5)


# ## Step 4 - do the fit, look at the values, etc...

# In[36]:


result = qmodel.fit(y_data, params, x=x_data)


# In[12]:


type(result)


# In[16]:


print(result.fit_report())


# In[28]:


from IPython.display import display, Markdown,HTML


# In[22]:


display(Markdown(result.fit_report()))


# In[23]:


result.fit_report()


# In[31]:


from markdown import markdown


# In[34]:


display(HTML(markdown("# header\nsomething else")))


# In[39]:


import pandas as pd


# In[51]:


pd.DataFrame( ( ('fitting method','leastsq'), ('func evals',17) ) ,columns=[' ','  '],index=[' ','  '])


# In[11]:


result


# In[26]:


plot(x_data,y_data,'o')

x_fake=linspace(-12,12,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# ## Turns out lmfit already has this function...

# In[27]:


qmodel=models.QuadraticModel()


# In[28]:


qmodel.param_names


# In[29]:


result = qmodel.fit(y_data, params, x=x_data)


# In[30]:


plot(x_data,y_data,'o')

x_fake=linspace(-12,12,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# # Another Data Set

# In[57]:


x_data,y_data=(array([0.        , 0.12820513, 0.25641026, 0.38461538, 0.51282051,
        0.64102564, 0.76923077, 0.8974359 , 1.02564103, 1.15384615,
        1.28205128, 1.41025641, 1.53846154, 1.66666667, 1.79487179,
        1.92307692, 2.05128205, 2.17948718, 2.30769231, 2.43589744,
        2.56410256, 2.69230769, 2.82051282, 2.94871795, 3.07692308,
        3.20512821, 3.33333333, 3.46153846, 3.58974359, 3.71794872,
        3.84615385, 3.97435897, 4.1025641 , 4.23076923, 4.35897436,
        4.48717949, 4.61538462, 4.74358974, 4.87179487, 5.        ]),
 array([ 1.0428932 ,  0.89749902,  0.75670392,  0.64111299,  0.55718173,
         0.52405064,  0.56088843,  0.5490807 ,  0.42480484,  0.47428914,
         0.2934649 ,  0.34352106,  0.33185889,  0.27993667,  0.26003406,
         0.27138304,  0.39834035,  0.28156451,  0.2572975 ,  0.27710445,
         0.15969731,  0.22588548,  0.18106594,  0.15347512,  0.25385423,
         0.20835157,  0.1964213 ,  0.09014651,  0.11874164,  0.14871592,
         0.06117995,  0.19194054,  0.05546755,  0.10819372,  0.13157402,
         0.16435838,  0.04113969, -0.03053311,  0.0710629 ,  0.08495973]))


# In[93]:


plot(x_data,y_data,'o')


# ## Step 1 - define the function
# 
# ## Step 2 - define the model and construct the parameter list
# 
# ## Step 3 - modify the parameter list (min, max, etc...) as needed
# 
# ## Step 4 - do the fit, look at the values, etc...

# In[62]:


def exponential(x,A=1,τ=0.1):
    return A*exp(-x/τ)

def double_exponential(x,A1=.5,τ1=0.5,A2=.5,τ2=3):
    return exponential(x,A1,τ1)+exponential(x,A2,τ2)


# In[ ]:





# In[66]:


mymodel=Model(exponential)
params=mymodel.make_params()
params['A'].value=1
params['A'].min=0
params['τ'].value=1
params['τ'].min=0
params


# In[68]:


result = mymodel.fit(y_data, params, x=x_data)
result


# In[69]:


plot(x_data,y_data,'o')

x_fake=linspace(0,12,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# In[70]:


mymodel=Model(double_exponential)
params=mymodel.make_params()
params['A1'].value=1
params['A1'].min=0
params['τ1'].value=1
params['τ1'].min=0
params['A2'].value=1
params['A2'].min=0
params['τ2'].value=1
params['τ2'].min=0
params


# In[71]:


result = mymodel.fit(y_data, params, x=x_data)
result


# In[72]:


plot(x_data,y_data,'o')

x_fake=linspace(0,12,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# ## Turns out lmfit has this function too (different parameter names)...

# In[73]:


mymodel=models.ExponentialModel()


# In[75]:


mymodel.param_names


# In[76]:


params=mymodel.make_params()
params['amplitude'].value=1
params['amplitude'].min=0
params['decay'].value=1
params['decay'].min=0
params


# In[78]:


result = mymodel.fit(y_data, params, x=x_data)


# In[79]:


plot(x_data,y_data,'o')

x_fake=linspace(0,12,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# In[88]:


# the prefix is so that the parameters have unique names
mymodel=models.ExponentialModel( prefix='one_') + models.ExponentialModel(prefix='two_')  
mymodel.param_names


# In[89]:


params=mymodel.make_params()
params['one_amplitude'].value=1
params['one_amplitude'].min=0
params['one_decay'].value=1
params['one_decay'].min=0
params['two_amplitude'].value=1
params['two_amplitude'].min=0
params['two_decay'].value=1
params['two_decay'].min=0
params


# In[90]:


result = mymodel.fit(y_data, params, x=x_data)


# In[91]:


plot(x_data,y_data,'o')

x_fake=linspace(0,12,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')


# In[ ]:




