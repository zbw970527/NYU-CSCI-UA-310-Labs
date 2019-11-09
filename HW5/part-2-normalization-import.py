
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np


# In[ ]:


data = pd.read_csv("Consumer_Services_Mediated_Complaints.csv");


# In[ ]:


data.keepColumn('Business Name','Industry','Complaint Type','Mediation Start Date','Mediation Close Date','Satisfaction','Business State')
data.dropNA('Business Name','Industry','Complaint Type','Mediation Start Date','Mediation Close Date','Satisfaction','Business State')
data.toCSV("hw05.csv")


# In[43]:


file = pd.read_csv('hw05.csv')


# In[30]:


x = np.array(file['Industry'].unique())


# In[31]:


pd.DataFrame(x).to_csv("industry.csv", header = None)


# In[44]:


z = np.array(file['Complaint Result'].unique())
pd.DataFrame(z).to_csv("complaint_result.csv", header = None)


# In[39]:


data = file[['Business Name','Business State']]


# In[41]:


data.to_csv("company.csv", header = None)


# In[42]:


z = np.array(file['Business Name'].unique())
pd.DataFrame(z).to_csv("company_name.csv", header = None)

