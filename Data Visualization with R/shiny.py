#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px


# In[15]:


st.title("Trends in Demographics and Income")
st.text("Explore the difference between people who earn less than 50K and more than 50K")


# In[14]:


df = pd.read_csv("shiny.csv")

#df.head()


# In[6]:


st.header("UCI Adult Dataset")
st.write(df.head())


# In[ ]:


#df["native_country"].unique()


# In[7]:


country = ['United-States', 'Mexico', 'Greece', 'Vietnam', 'China',
       'Taiwan', 'India', 'Philippines', 'Trinadad&Tobago', 'Canada',
       'South', 'Holand-Netherlands', 'Puerto-Rico', 'Poland', 'Iran',
       'England', 'Germany', 'Italy', 'Japan', 'Hong', 'Honduras', 'Cuba',
       'Ireland', 'Cambodia', 'Peru', 'Nicaragua', 'Dominican-Republic',
       'Haiti', 'El-Salvador', 'Hungary', 'Columbia', 'Guatemala',
       'Jamaica', 'Ecuador', 'France', 'Yugoslavia', 'Scotland',
       'Portugal', 'Laos', 'Thailand', 'Outlying-US(Guam-USVI-etc)']

st.selectbox("Country:", options=country)


# In[ ]:


#st.text("Select a continuous variable and graph type (histogram or boxplot) to view on the right")
st.write("**Select a continuous variable and graph type (histogram or boxplot) to view on the right**")

continuous = st.radio("Continuous", ("age","hours per week"))

graph1 = st.radio("Graph:", ("Histogram","Boxplot"))


# In[34]:


# fighist1 = px.histogram(data_frame=df, x="age", title="Trend of Age")

# fighist1.show()

# fighist2 = px.histogram(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week")

# fighist2.show()


# In[35]:


fighist1 = px.histogram(data_frame=df, x="age", title="Trend of Age")
st.plotly_chart(fighist1)


fighist2 = px.histogram(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week")
st.plotly_chart(fighist2)


# In[38]:


# figbox1 = px.box(data_frame=df, x="age", title="Trend of Age", orientation='h')
# figbox1.show()

# figbox2 = px.box(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week", orientation='h')
# figbox2.show()


# In[39]:


figbox1 = px.box(data_frame=df, x="age", title="Trend of Age", orientation='h')
st.plotly_chart(figbox1)

figbox2 = px.box(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week", orientation='h')
st.plotly_chart(figbox2)


# In[ ]:


st.write("**Select a categorical variable to view bar chart on the right**")

continuous = st.radio("Categorical", ("education","workclass","sex"))

st.checkbox("Stack Bars", value=False )


# In[60]:


plt.figure(figsize=(15,5))
sns.countplot(x="education", data=df)
plt.title("Trend of Education", fontsize=20)
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(15,5))
sns.countplot(x="workclass", data=df)
plt.title("Trend of Workclass", fontsize=20)
plt.show()

plt.figure(figsize=(15,5))
sns.countplot(x="sex", data=df)
plt.title("Trend of Sex", fontsize=20)
plt.show()


# In[ ]:





# In[ ]:




