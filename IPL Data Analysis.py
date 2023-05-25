#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = (14, 8)


# In[3]:


matches=pd.read_csv("C:/Users/djnag/Downloads/matches.csv",encoding = "ISO-8859-1")


# In[4]:


matches.shape


# In[5]:


matches.head


# In[6]:


matches.describe()


# In[7]:


matches.info()


# In[8]:


matches['season'].unique()


# In[9]:


max(matches['win_by_runs'])


# In[10]:


# Match won by the maximum margin of runs
matches.iloc[matches['win_by_runs'].idxmax()]


# In[11]:


max(matches['win_by_wickets'])


# In[12]:


# Match won by maximum wickets
matches.iloc[matches['win_by_wickets'].idxmax()]


# In[13]:


# Match won by minimum margin of runs (not by 1 run)
matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()]


# In[14]:


# Match won by minimum wickets (not by 0 wickets)
matches.iloc[matches[matches['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]


# In[15]:


matches['dl_applied'].unique()


# In[16]:


# Matches where D/L method was and wasn't applied
# 0 indicates normal match with no D/L method applied and 1 indicates a rain curtailed match with D/L method being applied
matches['dl_applied'].value_counts()


# In[17]:


# % of matches with and without D/L method (0 for no D/L and 1 for D/L method applied)
round(matches['dl_applied'].value_counts()/matches['dl_applied'].count()*100, 2)


# In[18]:


# Plot to visualise the no. of matches held in each city
sns.countplot(y='city', data=matches)
plt.title('No. of matches held in each city\n')
plt.xlabel('\nNo. of matches held')
plt.ylabel('Cities\n')
plt.xlim([0,120])
plt.show()


# In[19]:


# No. of matches won by each team
matches['winner'].value_counts()


# In[20]:


# Plot to visualise the no. of matches won by each team
data=matches['winner'].value_counts()
fig, ax=plt.subplots()
ax.set_xlim([0,120])
sns.barplot(y=data.index, x=data, orient='h')
plt.title('No. of matches won by each team\n')
plt.xlabel("\nNo. of matches won")
plt.ylabel('Teams\n')
plt.show()


# In[21]:


# Plot to visualise the no. of matches held every season
sns.countplot(x='season', data=matches)
plt.title('No. of matches held every season\n')
plt.xlabel('\nSeason')
plt.ylabel('No. of matches held\n')
plt.show()


# In[22]:


# Picking the top 10 players based on the no. of Man of Match (MOM) awards won
mom=matches['player_of_match'].value_counts()[:10]
mom


# In[23]:


# Plot to visualise the top 10 players based on the no. of MOM awards won
fig, ax=plt.subplots()
ax.set_ylim([0,28])
ax.set_title('Top 10 players based on no. of MOM awards won\n')
sns.barplot(x=mom.index, y=mom, orient='v')
plt.ylabel('No. of MOM awards won\n')
plt.xlabel('\nPlayers')
plt.show()


# In[24]:


# Does winning the toss mean winning the match?
winnerwinner=matches['toss_winner']== matches['winner']
winnerwinner.groupby(winnerwinner).size()


# In[25]:


# % of games where the toss winning team lost the match (indicated by false) and toss winning team won the match(indicated by true)
round(winnerwinner.groupby(winnerwinner).size() / winnerwinner.count() * 100,2)


# In[26]:


# How many times did the captain choose fielding and batting after winning the toss?
matches['toss_decision'].value_counts()


# In[27]:


# % of matches where the toss winning team's captain chose fielding and batting
round(matches['toss_decision'].value_counts()/matches['toss_decision'].count()*100, 2)


# In[28]:


## Stadiums which have hosted D/L method applied matches 
matches.query('dl_applied==1')['venue']


# In[29]:


# Cities which have witnessed D/L method applied matches
matches.query('dl_applied==1')['city']


# In[30]:


# Seasons with D/L method applied matches
year=matches.query('dl_applied==1')['season']
year


# In[31]:


# Plot to visualise the no. of matches where D/L method was applied season wise
fig, ax=plt.subplots()
ax.set_ylim([0,5])
ax.set_title('No. of matches where D/L method was applied, season wise\n')
sns.countplot(x=year, data=matches)
plt.xlabel('\nSeason')
plt.ylabel('No. of matches\n')
plt.show()


# In[32]:


# Different results for games
matches['result'].value_counts()


# In[33]:


# How many times did each team win the toss?
matches['toss_winner'].value_counts()


# In[34]:


# Plot to visualise the no. of tosses won by each team
toss=matches['toss_winner'].value_counts()
fig, ax=plt.subplots()
ax.set_title('No. of tosses won by each team\n')
sns.barplot(y=toss.index, x=toss, orient='h')
plt.xlabel('\nNo. of tosses won')
plt.ylabel('Teams\m')
plt.show()


# In[35]:


# Best venue for defending your total
matches.venue[matches.win_by_runs!=0].mode()


# In[36]:


# Best venue to chase a total
matches.venue[matches.win_by_wickets!=0].mode()


# In[37]:


# Best defending team
matches.winner[matches.win_by_runs!=0].mode()


# In[38]:


# Best chasing team
matches.winner[matches.win_by_wickets!=0].mode()


# In[39]:


# No. of matches played in different stadiums
sns.countplot(y='venue', data=matches)
plt.title('No. of matches played in different stadiums\n')
plt.xlabel('\nNo. of matches played')
plt.ylabel('Stadiums\n')
plt.show()


# In[ ]:




