
# coding: utf-8

# # corona virus live tracking for india

# In[15]:


import pandas as pd
df=pd.read_json('https://www.mohfw.gov.in/data/datanew.json')
df


# In[17]:


del df["sno"]


# In[18]:


df=df.iloc[:-1,:]


# In[19]:


df.head()


# In[20]:


df.tail()


# In[21]:


columnsTitles=['state_name','active','positive','cured','death','new_active','new_positive','new_cured','new_death','state_code']

df=df.reindex(columns=columnsTitles)


# In[22]:


df.head()


# In[25]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
total_states = np.arange(len(df['state_name']))


# In[26]:


total_states


# In[27]:


df['active']


# # #positive Number of cases based on states

# In[39]:


from matplotlib.pyplot import figure
figure(num=None,figsize=(9,6),dpi=200,facecolor='w',edgecolor='k')
plt.barh(total_states,df['positive'],align='center',alpha=0.5,
        color=(1,0,0),
        edgecolor=(0.5,0.2,0.8) )
plt.yticks(total_states,df['state_name'])
plt.xlim(1,max(df['positive'])+100)
plt.xlabel('positive number of cases')
plt.title('corona virus cases')
plt.show()


# # active number of cases based on states

# In[42]:


from matplotlib.pyplot import figure
figure(num=None,figsize=(9,6),dpi=200,facecolor='w',edgecolor='k')
plt.barh(total_states,df['active'],align='center',alpha=0.5,
        color=(0,0,1),
        edgecolor=(0.2,0.5,0.8) )
plt.yticks(total_states,df['state_name'])
plt.xlim(1,max(df['active'])+100)
plt.xlabel('active number of cases')
plt.title('corona virus cases')
plt.show()


# In[43]:


df.columns


# In[44]:


df=df.set_index('state_name',drop='true')


# In[45]:


df.head()


# In[46]:


df.plot.barh(stacked=True,figsize=(11,11))


# In[47]:


df1=df.iloc[:,1:3]
df1.plot.barh(stacked=True,figsize=(11,11))


# In[49]:


df2=df.iloc[:,1:5]
df2.plot.barh(stacked=True,figsize=(11,11))

