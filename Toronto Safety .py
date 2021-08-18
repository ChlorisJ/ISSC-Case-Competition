#!/usr/bin/env python
# coding: utf-8

# ## Toronto Livability - Safety

# In[1]:


# Import some packages
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import figure


# In[2]:


# Import geopanda for mapping
import geopandas as gpd
from pandas_profiling import ProfileReport


# In[3]:


# Pandas Dataset
data = pd.read_csv('Casecomp/neighbourhood-crime-rates.csv')


# In[4]:


data.head()


# In[5]:


# Aggregate all crime to new col 'Crime rate'
data['Crime_rate2014'] = data['Assault_Rate2014']+data['AutoTheft_Rate2014']+data['TheftOver_Rate2014']
+data['BreakAndEnter_Rate2014']+data['Robbery_Rate2014']+data['Shooting_Rate2014']

data['Crime_rate2015'] = data['Assault_Rate2015']+data['AutoTheft_Rate2015']+data['TheftOver_Rate2015']
+data['BreakAndEnter_Rate2015']+data['RobberyRate_2015']+data['Shootings_Rate2015']

data['Crime_rate2016'] = data['Assault_Rate2016']+data['AutoTheft_Rate2016']+data['TheftOver_Rate2016']
+data['BreakAndEnter_Rate2016']+data['Robbery_Rate2016']+data['Shootings_Rate2016']

data['Crime_rate2017'] = data['Assault_Rate2017']+data['AutoTheft_Rate2017']+data['TheftOver_Rate2017']
+data['BreakAndEnter_Rate2017']+data['Robbery_Rate2017']+data['Shootings_Rate2017']

data['Crime_rate2018'] = data['Assault_Rate2018']+data['AutoTheft_Rate2018']+data['TheftOver_Rate2018']
+data['BreakAndEnter_Rate2018']+data['Robbery_Rate2018']+data['Shootings_Rate2018']

data['Crime_rate2019'] = data['Assault_Rate2019']+data['AutoTheft_Rate2019']+data['TheftOver_Rate2019']
+data['BreakAndEnter_Rate2019']+data['Robbery_Rate2019']+data['Shootings_Rate2019']

data['Crime_rate2020'] = data['Assault_Rate2020']+data['AutoTheft_Rate2020']+data['TheftOver_Rate2020']
+data['BreakAndEnter_Rate2020']+data['Robbery_Rate2020']+data['Shootings_Rate2020']


# In[6]:


data.head()


# In[7]:


# Get Toronto Crime rate by taking average crime rate in 140 neighbourhoods.
y = data[data.columns[-7:]]
y.mean()


# In[8]:


y.mean().plot()


# In[ ]:





# In[9]:


# Take a look at Crime rate across neighbourhoods in Toronto from 2014-2020
y.T.plot()


# 

# In[10]:


# Get Geopandas dataframe called 'to'
to = gpd.read_file('Casecomp/neighbourhood-crime-rates_GEO.geojson')


# In[11]:


to.head()


# In[12]:


# We only consider rates for this analysis hense below columns are removed
to = to.drop(columns={'Assault_2014','Assault_2015','Assault_2016','Assault_2017','Assault_2018','Assault_2019','Assault_2020',
                     'AutoTheft_2014','AutoTheft_2015','AutoTheft_2016','AutoTheft_2017','AutoTheft_2018','AutoTheft_2019','AutoTheft_2020',
                      'BreakAndEnter_2014','BreakAndEnter_2015','BreakAndEnter_2016','BreakAndEnter_2017','BreakAndEnter_2018','BreakAndEnter_2019','BreakAndEnter_2020',
                      'Robbery_2014','Robbery_2015','Robbery_2016','Robbery_2017','Robbery_2018','Robbery_2019','Robbery_2020',
                      'TheftOver_2014','TheftOver_2015','TheftOver_2016','TheftOver_2017','TheftOver_2018','TheftOver_2019','TheftOver_2020',
                      'Homicide_2014','Homicide_2015','Homicide_2016','Homicide_2017','Homicide_2018','Homicide_2019','Homicide_2020',
                      'Shootings_2014','Shootings_2015','Shootings_2016','Shootings_2017','Shootings_2018','Shootings_2019','Shootings_2020',
                     
                     })


# In[13]:


to.describe()


# In[14]:


to = to.set_index('OBJECTID')


# In[15]:


to.plot()


# In[16]:


# Check missing values
to.isnull().sum()


# In[17]:


to['Crime_rate2014'] = to['Assault_Rate2014']+to['AutoTheft_Rate2014']+to['TheftOver_Rate2014']
+to['BreakAndEnter_Rate2014']+to['Robbery_Rate2014']+to['Shooting_Rate2014']


# In[18]:


to['Crime_rate2015'] = to['Assault_Rate2015']+to['AutoTheft_Rate2015']+to['TheftOver_Rate2015']
+to['BreakAndEnter_Rate2015']+to['RobberyRate_2015']+to['Shootings_Rate2015']


# In[19]:


to['Crime_rate2015'] = to['Assault_Rate2015']+to['AutoTheft_Rate2015']+to['TheftOver_Rate2015']
+to['BreakAndEnter_Rate2015']+to['RobberyRate_2015']+to['Shootings_Rate2015']


# In[20]:


to['Crime_rate2016'] = to['Assault_Rate2016']+to['AutoTheft_Rate2016']+to['TheftOver_Rate2016']
+to['BreakAndEnter_Rate2016']+to['Robbery_Rate2016']+to['Shootings_Rate2016']


# In[21]:


to['Crime_rate2017'] = to['Assault_Rate2017']+to['AutoTheft_Rate2017']+to['TheftOver_Rate2017']
+to['BreakAndEnter_Rate2017']+to['Robbery_Rate2017']+to['Shootings_Rate2017']


# In[22]:


to['Crime_rate2018'] = to['Assault_Rate2018']+to['AutoTheft_Rate2018']+to['TheftOver_Rate2018']
+to['BreakAndEnter_Rate2018']+to['Robbery_Rate2018']+to['Shootings_Rate2018']


# In[23]:


to['Crime_rate2019'] = to['Assault_Rate2019']+to['AutoTheft_Rate2019']+to['TheftOver_Rate2019']
+to['BreakAndEnter_Rate2019']+to['Robbery_Rate2019']+to['Shootings_Rate2019']


# In[24]:


to['Crime_rate2020'] = to['Assault_Rate2020']+to['AutoTheft_Rate2020']+to['TheftOver_Rate2020']
+to['BreakAndEnter_Rate2020']+to['Robbery_Rate2020']+to['Shootings_Rate2020']


# ### Crime rate 

# 

# In[25]:


to['Crime_rate2020'].describe()


# In[26]:


to['Crime_rate2020']


# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:


feature = to['Crime_rate2020']
vmin, vmax = 0, 5000
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='PuBu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('Overall Crime Rate Toronto 2020')
ax.axis('off')
sm = plt.cm.ScalarMappable(cmap='PuBu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[28]:


# Higest crime rate in 2020
High= to.nlargest(5,'Crime_rate2020')
NNEIB= High[['Neighbourhood','Crime_rate2014','Crime_rate2015',
             'Crime_rate2016','Crime_rate2017','Crime_rate2018',
                       'Crime_rate2019','Crime_rate2020']]
NNEIB


# In[29]:


# Lowest 10 crime rate in 2020
CR20_low = to.nsmallest(10,'Crime_rate2020')
SAFEST_NEIB= CR20_low[['Neighbourhood',
                       'Crime_rate2020']]
SAFEST_NEIB


# In[30]:


to['geometry']


# In[31]:



fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(facecolor='lavender', linewidth=3, ax=ax,edgecolor='1',alpha=1,)
ax.set_title('Safest Neibourhood in Toronto 2020')
CR20_low.plot(alpha=3, facecolor='tab:purple', linewidth=3, ax=ax)
ax.set_axis_off()
plt.axis('equal')
("")

to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
 plt.annotate(s=row['_id'], xy=row['coords'],
              horizontalalignment='center')


# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[32]:


CR20_low['Crime_rate2014']


# In[33]:


CR = to.T.iloc[-8:-1]


# In[34]:


CR


# In[ ]:





# In[ ]:





# In[ ]:





# In[35]:


y1 = (CR20_low['Crime_rate2014'],CR20_low['Crime_rate2015'],CR20_low['Crime_rate2016'],
     CR20_low['Crime_rate2017'],CR20_low['Crime_rate2018'],CR20_low['Crime_rate2019'],
     CR20_low['Crime_rate2020'])


# In[36]:


y1


# In[37]:


x1 = ['2014','2015','2016','2017','2018','2019','2020']
y1 = (CR20_low['Crime_rate2014'],CR20_low['Crime_rate2015'],CR20_low['Crime_rate2016'],
     CR20_low['Crime_rate2017'],CR20_low['Crime_rate2018'],CR20_low['Crime_rate2019'],
     CR20_low['Crime_rate2020'])


plt.plot(x1, y1, label='Crime rate toronto')

plt.xlabel('Year')
plt.ylabel('Assault Rate')
plt.title("Assault rate rrend in lowest 5 assault rate neibourhoods")
  
plt.plot(y1, linestyle='-', linewidth='1')
plt.legend(CR20_low['Neighbourhood'],bbox_to_anchor=(1.05, 1))

plt.show()


# In[38]:


y1


# In[39]:


sns.scatterplot(data=to, x='Crime_rate2019', y='_id', hue='_id', )


# In[40]:


sns.lineplot(data=to, x='_id', y='Crime_rate2019')


# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


y=[to['Crime_rate2014'],to['Crime_rate2015'],to['Crime_rate2016'],
    to['Crime_rate2017'],to['Crime_rate2018'],to['Crime_rate2019'],to['Crime_rate2020']]

y


# ### Assault

# In[42]:


to['Assault_Rate2020'].describe()


# In[53]:


feature = to['Assault_Rate2020']
vmin, vmax = 0, 5000
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='BuPu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('Assault Rate Toronto 2020')
ax.axis('off')


sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
plt.rcParams['font.size'] = 12

("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[57]:


AR20_high = to.nlargest(5,'Assault_Rate2020')
AR20_high[['Neighbourhood','Assault_Rate2020']]


# In[58]:


AR20_low = to.nsmallest(10,'Assault_Rate2020')
safest1 = AR20_low[['Neighbourhood','Assault_Rate2020']]
safest1


# In[59]:


AR20_low['_id']


# In[60]:


x1 = ['2014','2015','2016','2017','2018','2019','2020']
y1 = (lst_ar_low['Assault_Rate2014'],lst_ar_low['Assault_Rate2015'],lst_ar_low['Assault_Rate2016'],
     lst_ar_low['Assault_Rate2017'],lst_ar_low['Assault_Rate2018'],lst_ar_low['Assault_Rate2019'],
     lst_ar_low['Assault_Rate2020'])

plt.plot(x1, y1, label='Assault_Rate')

plt.xlabel('Year')
plt.ylabel('Assault Rate')
plt.title("Assault rate rrend in lowest 5 assault rate neibourhoods")
  
plt.plot(y1, linestyle='-', linewidth='1')
plt.legend(AR20_low['Neighbourhood'],bbox_to_anchor=(1.05, 1))

plt.show()


# ### Auto Theft

# In[58]:


to['AutoTheft_Rate2020'].describe()


# In[57]:


feature = to['AutoTheft_Rate2020']
vmin, vmax = 0, 1000
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='BuPu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('AutoTheft Rate Toronto 2020')
ax.axis('off')
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
plt.rcParams['font.size'] = 12
("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[55]:


AT20_high = to.nlargest(5,'AutoTheft_Rate2020')
AT20_high[['Neighbourhood','AutoTheft_Rate2020']]


# In[ ]:


AT20_low = to.nsmallest(5,'AutoTheft_Rate2020')
safest2 = AT20_low[['Neighbourhood','AutoTheft_Rate2020']]
safest2


# ### Break And Enter

# In[61]:


to['BreakAndEnter_Rate2020'].describe()


# In[60]:


feature = to['BreakAndEnter_Rate2020']
vmin, vmax = 0, 1000
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='BuPu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('Break And Enter Rate Toronto 2020')
ax.axis('off')
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
plt.rcParams['font.size'] = 12
("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[ ]:


BE20_high = to.nlargest(5,'BreakAndEnter_Rate2020')
BE20_high[['Neighbourhood','BreakAndEnter_Rate2020']]


# In[ ]:


BE20_low = to.nsmallest(10,'BreakAndEnter_Rate2020')
safest3 = BE20_low[['Neighbourhood','BreakAndEnter_Rate2020']]
safest3 


# ### Robbery 

# In[64]:


to['Robbery_Rate2020'].describe()


# In[63]:


feature = to['Robbery_Rate2020']
vmin, vmax = 0, 600
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='BuPu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('Robbery Rate Toronto 2020')
ax.axis('off')
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
plt.rcParams['font.size'] = 12
("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[ ]:


RR20_high = to.nlargest(5,'Robbery_Rate2020')
RR20_high[['Neighbourhood','Robbery_Rate2020']]


# In[ ]:


RR20_low = to.nsmallest(10,'Robbery_Rate2020')
safest4 = RR20_low[['Neighbourhood','Robbery_Rate2020']]
safest4


# ### Theft Over

# In[67]:


to['TheftOver_Rate2020'].describe()


# In[68]:


feature = to['TheftOver_Rate2020']
vmin, vmax = 0, 200
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='BuPu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('Theft Over Toronto 2020')
ax.axis('off')
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
plt.rcParams['font.size'] = 12
("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[ ]:


TO20_high = to.nlargest(5,'TheftOver_Rate2020')
TO20_high[['Neighbourhood','TheftOver_Rate2020']]


# In[ ]:


TO20_low = to.nsmallest(10,'TheftOver_Rate2020')
safest5 = TO20_low[['Neighbourhood','TheftOver_Rate2020']]
safest5


# ### Homicide

# In[ ]:


to['Homicide_Rate2020'].describe()


# In[ ]:


feature = to['Homicide_Rate2020']
vmin, vmax = 0, 20
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='BuPu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('Homicide Rate Toronto 2020')
ax.axis('off')
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[ ]:


HM20_high = to.nlargest(5,'Homicide_Rate2020')
HM20_high[['Neighbourhood','Homicide_Rate2020']]


# In[ ]:


HM20_low = to.nsmallest(10,'Homicide_Rate2020')
safest6 = HM20_low[['Neighbourhood','Homicide_Rate2020']]
safest6


# ### Shootings

# In[71]:


to['Shootings_Rate2020'].describe()


# In[74]:


feature = to['Shootings_Rate2020']
vmin, vmax = 0, 100
fig, ax = plt.subplots(1, figsize=(20, 12))
to.plot(column=feature, cmap='BuPu', linewidth=3, ax=ax, edgecolor='0.8')
ax.set_title('Shooting Rate Toronto 2020')
ax.axis('off')
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
plt.rcParams['font.size'] = 13
("")
to['coords'] = to['geometry'].apply(lambda x: x.representative_point().coords[:])
to['coords'] = [coords[0] for coords in to['coords']]
for idx, row in to.iterrows():
    plt.annotate(s=row['_id'], xy=row['coords'],
                 horizontalalignment='center')


# In[ ]:


ST20_high = to.nlargest(5,'Shootings_Rate2020')
ST20_high[['Neighbourhood','Shootings_Rate2020']]


# In[ ]:


ST20_low = to.nsmallest(10,'Shootings_Rate2020')
safest6 = ST20_low[['Neighbourhood','Shootings_Rate2020']]


# In[ ]:





# In[ ]:




