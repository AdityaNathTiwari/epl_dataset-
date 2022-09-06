#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


epl_df=pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Desktop\\DATA SET\\epldataset8.csv')
epl_df.head()


# In[3]:


epl_df.tail()


# In[4]:


epl_df.info()


# In[5]:


epl_df.describe()


# In[6]:


epl_df.isna()


# In[7]:


epl_df.isna().sum()


# In[10]:


epl_df['minspermatch']=(epl_df['Mins']/epl_df['Matches']).astype(int)
epl_df['Goalspermatch']=(epl_df['Goals']/epl_df['Matches']).astype(float)
epl_df.head()
                        
                        


# In[11]:


Total_goals=epl_df['Goals'].sum()
print(Total_goals)


# In[15]:


Total=epl_df['Penalty_Attempted'].sum()
print(Total)


# In[16]:



pneltynotscored=epl_df['Penalty_Attempted'].sum()-epl_df['Penalty_Goals'].sum()
print(pneltynotscored)


# In[20]:


epl_df['Penalty_Goals'].sum()


# In[33]:


plt.figure(figsize=(13,6))
pneltynotscored=epl_df['Penalty_Attempted'].sum()-epl_df['Penalty_Goals'].sum()
totalpenaltygoals=epl_df['Penalty_Goals'].sum()
data=[pneltynotscored,totalpenaltygoals]
labels=['penalties missed','penalties scored']
color=sns.color_palette("Paired")
plt.pie(data,labels=labels,colors=color,autopct='%.0f%%')
plt.show()


# In[42]:


# unique position 
epl_df['Position'].unique()


# In[41]:


epl_df.head()


# In[46]:


epl_df[epl_df['Position']=='FW'].sum()


# In[47]:


np.size((epl_df['Nationality'].unique()))


# In[58]:


Nationality=epl_df.groupby('Nationality').size().sort_values(ascending=False)
Nationality.head(10).plot(kind='bar',figsize=(12,6),color=sns.color_palette("magma"))


# In[2]:


epl_df['Club'].value_counts().nlargest(5).plot(kind='bar',color=sns.color_palette("magma"))


# In[4]:


epl_df=pd.read_csv('C:\\Users\\LENOVO\\OneDrive\\Desktop\\DATA SET\\epldataset8.csv')


# In[5]:


epl_df['Club'].value_counts().nlargest(5).plot(kind='bar',color=sns.color_palette("magma"))


# In[12]:


epl_df['Club'].value_counts().nsmallest(5).plot(kind='bar',color=sns.color_palette("Paired"))


# In[14]:


under20=epl_df[epl_df['Age']<=20]
age20_25=epl_df[(epl_df['Age']>20)&(epl_df['Age']<=25)]
age25_30=epl_df[(epl_df['Age']>25)&(epl_df['Age']<=30)]
above30=epl_df[epl_df['Age']>30]


# In[37]:


#x=np.array([under20['Name'].count(),age20_25['Name'].count(),age25_30['Name'].count(),above30['Name'].count()])
#mylabels =["<=20",">20&<=25",">25&<=30",">30"]
#plt.title('total player with age group',frontsize=20)
#plt.pie(x,labels = mylabels,autopct="%.1f%%")
#plt.show()


# In[36]:


players_under_20=epl_df[epl_df['Age']<20]
players_under_20['Club'].value_counts().plot(kind='bar',color=sns.color_palette("cubehelix"))


# In[56]:


players_under_20[players_under_20["Club"]=='Manchester City']


# In[57]:


plt.figure(figsize=(12,6))
sns.boxplot(x='Club',y='Age',data=epl_df)
plt.xticks(rotation =90)


# In[60]:


num_player=epl_df.groupby('Club').size()
data=(epl_df.groupby('Club')['Age'].sum())/ num_player
data.sort_values(ascending=False)


# In[74]:


# TOTAL ASSIST FROM EACH CLUB
Assistsbytheclub=pd.DataFrame(epl_df.groupby('Club',as_index=False)['Assists'].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax=sns.barplot(x='Club',y='Assists',data=Assistsbytheclub.sort_values(by="Assists"),palette="Paired")
ax.set_xlabel("Club",fontsize=30)
ax.set_xlabel("Assists",fontsize=20)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"] = (20,8)
plt.title('plot of clubs vs total assits',fontsize = 20)


# In[61]:



#epl_df.head()


# In[81]:


top_10_assists=epl_df[['Name','Club','Assists','Matches']].nlargest(n=10,columns='Assists')
top_10_assists


# In[93]:


# total goals from each club
goalsbyclub=pd.DataFrame(epl_df.groupby("Club",as_index=False)["Goals"].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax=sns.barplot(x="Club",y="Goals",data=goalsbyclub.sort_values(by="Goals"),palette="rocket")
ax.set_xlabel("Club",fontsize=30)
ax.set_ylabel("Goals",fontsize=20)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"]=(20,8)
plt.title('plot of clubs vs total club',fontsize=20)


# In[95]:


#most goals by a player
top_10_goals=epl_df[['Name','Club','Goals','Matches']].nlargest(n=10,columns="Goals")
top_10_goals


# epl_df.head()

# In[94]:


epl_df.head()


# In[97]:


#top 10 goals according to per matches
top_10_goals_permatch=epl_df[['Name','Club','Goals',"Matches"]].nlargest(n=10,columns="Goals")
top_10_goals_permatch


# In[1]:


#import matplotlib.pyplot as plt
#import numpy as np
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
#x = np.cos(u) * np.sin(v)
#y = np.sin(u) * np.sin(v)
#z = np.cos(v)
#ax.plot_wireframe(x, y, z, color="BLUE")
#ax.set_title("Sphere")
#plt.show()


# In[2]:


ax = plt.axes(projection='3d')
""""
# Data for a three-dimensional line
#zline = np.linspace(0, 15, 1000)
#xline = np.sin(zline)
#yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'red')

# Data for three-dimensional scattered points
zdata = 100 * np.random.random(100)
xdata = np.sin(zdata) + 0.5 * np.random.randn(100)
ydata = np.cos(zdata) + 0.5 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
""""


# In[ ]:





# In[3]:


""""goalsbyclub=pd.DataFrame(epl_df.groupby("Club",as_index=False)["Goals"].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax=sns.barplot(x="Club",y="Goals",data=goalsbyclub.sort_values(by="Goals"),palette="rocket")
ax.set_xlabel("Club",fontsize=30)
ax.set_ylabel("Goals",fontsize=20)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"]=(20,8)
plt.title('plot of clubs vs total club',fontsize=20)
""""


# In[ ]:





# In[ ]:




