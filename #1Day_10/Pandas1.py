#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np


# In[45]:



data = ({'Day':[1,2,3,4,5,6,7],
       'Sleep':[5,7,8,6,7,8,8],
       'Work':[10,8,9,6,7,8,7]})
df = pd.DataFrame(data)
print(df)
#print(df.head(4))
#print(df.tail())
#print(df.set_index(['Day'],implace = False))


# In[46]:


#print(df[["Day","Work","Fuck","Sleep"]])


# In[62]:


data2 = ({'Day1':[7,6,5,4,3,2,2],
       'Sleep1':[5,7,8,6,7,8,8],
       'Work1':[10,8,9,6,7,8,7]})
df2 = pd.DataFrame(data2)
#merge  = pd.merge(df,df2,on = 'Day')


# In[63]:


print(merge)


# In[64]:


join = df.join(df2)


# In[65]:


print(join)


# In[66]:


import matplotlib.pyplot as plt


# In[67]:


print(df)


# In[68]:


df.plot()
plt.show()


# In[72]:


print(df)
print(df2)


# In[78]:


data3 = pd.DataFrame({'Day':[1,2,3,4,5,6,7],
       'Sleep':[5,7,8,6,7,8,8],
       'Work':[10,8,9,6,7,8,7],
       "Fuck":[2,3,4,5,2,1,8]},index = [0,1,2,3,4,5,6])

data4 = pd.DataFrame({'Day':[1,2,3,4,5,6,7],
       'Sleep':[5,7,8,6,7,8,8],
       'Work':[10,8,9,6,7,8,7],
       "Fuck":[2,3,4,5,2,1,8]},index = [7,8,9,10,11,12,13])


# In[80]:


Concat = pd.concat([data3,data4])


# In[81]:


print(Concat)


# In[ ]:





# ### Data Munging

# In[85]:


contry = pd.read_csv("file.csv",index_col = 0)


# In[86]:


contry.to_html('file_EXINDEX.html')


# In[88]:


daf =contry.head(5)


# In[89]:


#print(daf)


# In[ ]:




