#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px


# In[2]:


st.title("Trends in Demographics and Income")
st.text("Explore the difference between people who earn less than 50K and more than 50K")


# In[3]:


df = pd.read_csv("shiny.csv")

#df.head()


# In[4]:


st.header("UCI Adult Dataset")
st.write(df.head())


# In[ ]:


#df["native_country"].unique()


# In[5]:


country = ['United-States', 'Mexico', 'Greece', 'Vietnam', 'China',
       'Taiwan', 'India', 'Philippines', 'Trinadad&Tobago', 'Canada',
       'South', 'Holand-Netherlands', 'Puerto-Rico', 'Poland', 'Iran',
       'England', 'Germany', 'Italy', 'Japan', 'Hong', 'Honduras', 'Cuba',
       'Ireland', 'Cambodia', 'Peru', 'Nicaragua', 'Dominican-Republic',
       'Haiti', 'El-Salvador', 'Hungary', 'Columbia', 'Guatemala',
       'Jamaica', 'Ecuador', 'France', 'Yugoslavia', 'Scotland',
       'Portugal', 'Laos', 'Thailand', 'Outlying-US(Guam-USVI-etc)']

st.selectbox("Country:", options=country)


# In[6]:


#st.text("Select a continuous variable and graph type (histogram or boxplot) to view on the right")
st.write("**Select a continuous variable and graph type (histogram or boxplot) to view on the right**")

continuous = st.radio("Continuous", ("age","hours per week"))

graph1 = st.radio("Graph:", ("Histogram","Boxplot"))


# In[ ]:


# fig, ax = plt.subplots(1,2, sharex=False, figsize=(16,5))

# sns.histplot(x="age", data=df, hue_order=df.income, ax=ax[0])
# ax[0].set_title('Title of the first chart')

# sns.histplot(x="hours_per_week", data=df, hue_order=df.income, ax=ax[1])
# ax[1].set_title('Title of the second chart')

# plt.show()


# In[42]:


g = sns.FacetGrid(data=df, col="income", height=5, aspect=1)
g.map(plt.hist, "age")
plt.suptitle("Trend of Age", x=0.1, y=1.1, fontsize=30)
plt.show()
st.pyplot(g)


# In[37]:


g = sns.FacetGrid(data=df, col="income", height=5, aspect=1)
g.map(plt.hist, "hours_per_week")
plt.suptitle("Trend of Hours Per Week", x=0.2, y=1.1, fontsize=30)
plt.show()
st.pyplot(g)


# In[ ]:


# fighist1 = px.histogram(data_frame=df, x="age", title="Trend of Age")

# fighist1.show()

# fighist2 = px.histogram(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week")

# fighist2.show()


# In[ ]:


# fighist1 = px.histogram(data_frame=df, x="age", title="Trend of Age")
# st.plotly_chart(fighist1)


# fighist2 = px.histogram(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week")
# st.plotly_chart(fighist2)


# In[ ]:


# figbox1 = px.box(data_frame=df, x="age", title="Trend of Age", orientation='h')
# figbox1.show()

# figbox2 = px.box(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week", orientation='h')
# figbox2.show()


# In[41]:


g = sns.FacetGrid(data=df, col="income", height=5, aspect=1)
g.map(sns.boxplot, "age")
plt.suptitle("Trend of Age", x=0.1, y=1.1, fontsize=30)
plt.show()
st.pyplot(g)


# In[36]:


g = sns.FacetGrid(data=df, col="income", height=5, aspect=1)
g.map(sns.boxplot, "hours_per_week")
plt.suptitle("Trend of Hours Per Week", x=0.2, y=1.1, fontsize=30)
plt.show()

st.pyplot(g)


# In[ ]:


# figbox1 = px.box(data_frame=df, x="age", title="Trend of Age", orientation='h')
# st.plotly_chart(figbox1)

# figbox2 = px.box(data_frame=df, x="hours_per_week", title="Trend of Hours Per Week", orientation='h')
# st.plotly_chart(figbox2)


# In[11]:


st.write("**Select a categorical variable to view bar chart on the right**")

continuous = st.radio("Categorical", ("education","workclass","sex"))

st.checkbox("Stack Bars", value=False )


# In[27]:


g = sns.FacetGrid(data=df, col="income", height=5, aspect=2.3)
g.map(sns.countplot, "education")
plt.suptitle("Trend of Education", x=0.0, y=1.2, fontsize=30)
plt.show()

st.pyplot(g)


# In[28]:


g = sns.FacetGrid(data=df, col="income", height=5, aspect=2.3)
g.map(sns.countplot, "workclass")
plt.suptitle("Trend of Workclass", x=0.0, y=1.2, fontsize=30)
plt.show()

st.pyplot(g)


# In[29]:


g = sns.FacetGrid(data=df, col="income", height=5, aspect=2.3)
g.map(sns.countplot, "sex")
plt.suptitle("Trend of Sex", x=0.0, y=1.2, fontsize=30)
plt.show()

st.pyplot(g)


# In[30]:


# fig = plt.figure(figsize=(15,5))
# sns.countplot(x="education", data=df, hue=df.income)
# plt.title("Trend of Education", fontsize=20)
# plt.xticks(rotation=45)
# plt.show()
# st.pyplot(fig)

# fig = plt.figure(figsize=(15,5))
# sns.countplot(x="workclass", data=df, hue=df.income)
# plt.title("Trend of Workclass", fontsize=20)
# plt.show()
# st.pyplot(fig)

# fig = plt.figure(figsize=(15,5))
# sns.countplot(x="sex", data=df, hue=df.income)
# plt.title("Trend of Sex", fontsize=20)
# plt.show()
# st.pyplot(fig)


# In[31]:


# fig, ax = plt.subplots(1,2, sharex=False, figsize=(16,5))
# fig.suptitle('Main Title')



# sns.countplot(x="education", data=df, hue=df.income, ax=ax[0])
# ax[0].set_title('Title of the first chart')
# ax[0].tick_params('x', labelrotation=45)

# sns.countplot(x="sex", data=df, hue=df.income, ax=ax[1])
# ax[1].set_title('Title of the second chart')

# plt.show()
# st.pyplot(fig)


# In[ ]:




