#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


ls data


# In[3]:


import pandas as pd


# In[4]:


from sci378 import *


# In[60]:


def list_files(pattern):
    from glob import glob
    import zipfile
    from fnmatch import fnmatch
    if pattern.endswith('.zip'):
        with zipfile.ZipFile(pattern) as z:
            return [_.filename for _ in z.filelist ]
    elif '.zip/' in pattern:
        parts=pattern.split('.zip/')
        pattern=parts[1]
        if not pattern:
            pattern='*'
        
        with zipfile.ZipFile(parts[0]+".zip") as z:
            return [_.filename for _ in z.filelist if fnmatch(_.filename,pattern)]
    else:
        return glob(pattern)


# In[61]:


def read_zip_csv(zipfname,csvfname,**kwargs):
    import zipfile
    import pandas as pd
    
    with zipfile.ZipFile(zipfname) as z:
        data=pd.read_csv(z.open(csvfname),**kwargs)
        
    return data
    


# In[69]:


data=read_zip_csv('data/multiple peak data csv.zip','multiple peak data csv/sample44.csv')
data


# In[67]:


names=list_files('data/multiple peak data csv.zip/*.csv')
names


# In[36]:


n=names[0]


# In[38]:


n


# In[46]:


from fnmatch import fnmatch


# In[48]:


fnmatch(names[0],'*.csv')


# In[ ]:




