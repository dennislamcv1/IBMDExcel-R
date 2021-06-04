#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns


# In[2]:


st.title("Bike-Sharing Demand Prediction App")


# In[3]:


df = pd.read_csv("seoul_bike_sharing_clean.csv", parse_dates=["DATE"])

#df.head()


# In[4]:


# fig = plt.figure(figsize=(16,5))
# sns.lineplot(x="DATE",y="TEMPERATURE", data=df)
# plt.show()
# st.pyplot(fig)


# In[5]:


# fig = plt.figure(figsize=(50,10))
# sns.scatterplot(x=df.DATE,y=df.RENTED_BIKE_COUNT,data=df, estimator=None)
# plt.title("Scatterplot", fontsize=20)
# plt.xticks(rotation=90, fontsize=10)
# plt.xlabel("Dates", fontsize=20)
# plt.ylabel("Bike Counts", fontsize=20)
# plt.show()


# In[6]:


# fig = plt.figure(figsize=(16,5))

# sns.regplot(x="HUMIDITY", y="RENTED_BIKE_COUNT", data=df)
# plt.xlabel("Humidity", fontsize=20)
# plt.ylabel("Bike Counts", fontsize=20)
# plt.show()


# In[7]:


df2 = pd.read_csv("selected_cities.csv")
#df2.head()


# In[8]:


df3 = pd.read_csv("model.csv")
#df3[:5]


# In[9]:


st.header("Bike Sharing data")
st.write(df.head())


# In[10]:


st.header("Selected Cities Data")
st.write(df2.head())


# In[11]:


city = ['All','New York', 'Paris', 'Suzhou', 'London']

st.selectbox("City:", options=city)


# In[12]:


st.map(df2)


# In[13]:


st.write("**Select a button**")

page_names = ['Basic max bike prediction','A static temperature trend line','An interactive bike-sharing demand prediction trend line','A static humidity and bike-sharing demand prediction correlation plot']

page = st.radio("Selections", page_names)

if  page == 'Basic max bike prediction':
    st.subheader('Basic max bike prediction')
    st.dataframe(df3[:5])
elif page == 'A static temperature trend line':
    st.subheader('A static temperature trend line')
    
    fig = plt.figure(figsize=(16,5))
    sns.lineplot(x="DATE",y="TEMPERATURE", data=df)
    plt.xlabel("Dates")
    plt.ylabel("Temperature")
    st.pyplot(fig)    
elif page == 'An interactive bike-sharing demand prediction trend line':
    st.subheader('An interactive bike-sharing demand prediction trend line')
    
    fig = plt.figure(figsize=(50,10))
    sns.scatterplot(x=df.DATE,y=df.RENTED_BIKE_COUNT,data=df, estimator=None)
    plt.title("Scatterplot", fontsize=20)
    plt.xticks(rotation=90, fontsize=10)
    plt.xlabel("Dates", fontsize=20)
    plt.ylabel("Bike Counts", fontsize=20)
    st.pyplot(fig)
else:
    st.subheader('A static humidity and bike-sharing demand prediction correlation plot')
    
    fig = plt.figure(figsize=(16,5))
    sns.regplot(x="HUMIDITY", y="RENTED_BIKE_COUNT", data=df)
    plt.xlabel("Humidity", fontsize=20)
    plt.ylabel("Bike Counts", fontsize=20)
    st.pyplot(fig)


# In[ ]:





# In[ ]:





# In[ ]:




