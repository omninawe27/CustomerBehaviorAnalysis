#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# df =pd.read_csv('downloads/customer_shopping_behavior.csv')
df =pd.read_csv('downloads/customer_shopping_behavior.csv')


# In[2]:


df


# In[3]:


df.info()


# In[4]:


df.describe(include='all') //if not use include all then it will result only for numerical coloumns


# In[5]:


# check missing values
df.isnull().sum()


# In[6]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))


# In[7]:


df.isnull().sum()


# In[8]:


# rename
df.columns = df.columns.str.capitalize()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[9]:


df.columns


# In[10]:


# create column age_group
labels = ['Young_adult','Adult','Middle_aged','Senior']
df['Age_group']= pd.qcut(df['Age'],q=4,labels=labels)


# In[11]:


df[['Age','Age_group']].head(10)


# In[12]:


# create column purchase frequency days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['Frequency_of_purchases'].map(frequency_mapping)


# In[13]:


df[['purchase_frequency_days','Frequency_of_purchases']].sample(10)


# In[14]:


df[['Discount_applied','Promo_code_used']]


# In[15]:


(df['Discount_applied']== df['Promo_code_used']).all()


# In[16]:


df =df.drop('Promo_code_used',axis=1)


# In[17]:


df.columns


# In[18]:


get_ipython().system('pip install psycopg2-binary sqlalchemy')


# In[19]:


get_ipython().system('python.exe -m pip install --upgrade pip')


# In[20]:


from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres"      # default user
password = "1234" # the password you set during installation
host = "localhost"         # if running locally
port = "5432"              # default PostgreSQL port
database = "customer_behavior"    # the database you created in pgAdmin

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer"   # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:




