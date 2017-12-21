
# coding: utf-8

# In[465]:


import pandas as pd
get_ipython().magic('pylab inline')


# In[466]:


df = pd.read_csv('train.csv')


# In[467]:


df


# In[468]:


df.shape


# In[469]:


df.Survived.value_counts()


# In[470]:


342/891


# In[471]:


df.Sex.value_counts()


# In[472]:


df.Sex.value_counts().plot(kind='bar')


# In[473]:


df[df.Sex=='female']


# In[474]:


df[df.Sex.isnull()]


# In[475]:


df.Fare.value_counts()
df.describe()


# In[476]:


df.Fare.hist()


# In[477]:


df[df.Fare.isnull()]


# In[478]:


df[df.Fare==0]


# In[479]:


df[df.Cabin.isnull()]


# In[480]:


## who are first women and childern?

fig, axs = plt.subplots(1,2)
df[df.Sex=='male'].Survived.value_counts().plot(kind='bar',ax=axs[0],title='Male survived')
df[df.Sex=='female'].Survived.value_counts().plot(kind='bar',ax=axs[1],title='Female survived')


# In[481]:


df[df.Age <10].Survived.value_counts().plot(kind='bar', title='people who survived below 10 years')


# In[482]:


df[(df.Age <10) & (df.Sex=='female')].Survived.value_counts().plot(kind='bar', title='Female children who survived below 10 years')


# In[483]:


df[(df.Age <10) & (df.Sex=='male')].Survived.value_counts().plot(kind='bar', title='male children who survived below 10 years')

