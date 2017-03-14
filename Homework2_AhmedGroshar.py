
# coding: utf-8

# In[12]:

import nsfg
import thinkplot
import thinkstats2
pres = nsfg.ReadFemResp()


# EX 1

fmar1age = pres['fmar1age']

his = thinkstats2.Hist(pres.fmar1age)
hist1 = thinkstats2.Hist(his)
pres.fmar1age.value_counts().sort_index()


# In[17]:


thinkplot.Hist(hist1,width=0.5)
thinkplot.Show(xlabel='Age at first marriage', ylabel='Frequency of first marriage')


# In[21]:

# EX 2

fmarno = pres['fmarno']
histo = thinkstats2.Hist(fmarno)
pres.fmarno.value_counts().sort_index()


# In[22]:


thinkplot.Hist(histo, color='blue',width=0.5,label="Respondents' number of mariage ")
thinkplot.Show(xlabel="Respondents' number of mariage ", ylabel='Frequency')


# In[33]:

# EX 3

totincr = pres['totincr']
histog = thinkstats2.Hist(totincr)
pres.totincr.value_counts().sort_index()


# In[34]:


thinkplot.Hist(histog, color='green',width=0.5,label="Total income") 
thinkplot.Show(xlabel='Range', ylabel='Frequency')


# In[36]:

# EX 4

never_married = pres[pres.fmarno == 0]
married = pres[pres.fmarno >= 1]

histog41 = thinkstats2.Hist(never_married.totincr, label="Never Married Person")
histog42 = thinkstats2.Hist(married.totincr, label="Married Person")

thinkplot.Hist(histog41, align='right',width=0.5,color='blue')
thinkplot.Hist(histog42, align='left',width=0.5,color='green')
thinkplot.Show(xlabel='Time', ylabel='Amount',)


# In[38]:

# EX 5

print 'Max value of total income of never married respondents is %.2f' %never_married.totincr.max()

print 'Max total income of married respondents is %.2f' %married.totincr.max()

print 'Minimum of income of never married respondents is %.2f' %never_married.totincr.min()

print 'Miminum of total income of never married respondents is %.2f' %married.totincr.min()

print 'Varience of the total income of the never married respondents is %.2f' %never_married.totincr.var()

print 'Varience of total income of married respondents is %.2f' %married.totincr.var()

print 'Mean of total income of never married respondentsis %.2f' %never_married.totincr.mean()

print 'Mean of total income of married respondents is %.2f' %married.totincr.mean()

print 'Standart deviation of total income of never married respondents is %.2f' %never_married.totincr.std()

print 'Standart deviation of the total income of married respondents is %.2f' %married.totincr.std()




