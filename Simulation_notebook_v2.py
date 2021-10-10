#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ciw 
import pandas as pd 
from pandas import DataFrame
import matplotlib as plt 
import numpy as np #Calcules numériques  
import matplotlib.pyplot as plt#Représentation Graphiques
get_ipython().run_line_magic('matplotlib', 'inline')
import math #Réalisation des opération mathématiques 
import matplotlib.pyplot as plt 
import seaborn as sns #Bibliothèque de la Data_Visualisation  
from collections import Counter


# In[9]:


df=pd.read_csv(r'C:\Users\BOULHANNA\Desktop\INSEA S4\s4\SIMULATION\simulation_projet\output\DATA.csv')


# In[10]:


df


# In[11]:


df.set_index('time')


# In[12]:


client_A=df[df["customer_class"]==0]


# In[13]:


client_A


# In[18]:


temp_de_sejour_A=(client_A["service_time"]+client_A["waiting_time"]).mean()


# In[19]:


temp_de_sejour_A


# In[20]:


client_B=df[df["customer_class"]==1]


# In[21]:


client_B


# In[22]:


temp_de_sejour_B=(client_B["service_time"]+client_B["waiting_time"]).mean()


# In[23]:


temp_de_sejour_B


# In[26]:


Exemple_4_unit_time=df[:5]


# In[27]:


Exemple_4_unit_time


# In[28]:


Exemple_4_unit_time.set_index("time")


# In[46]:


# x axis values
x =Exemple_4_unit_time["time"] 
# corresponding y axis values
y = Exemple_4_unit_time["customer_class"]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('temps')
# naming the y axis
plt.ylabel('type du client entrant danns le système')
  
# giving a title to my graph
plt.title('Evolution des clients dans le système pendant 4 unités de temps')
  
# function to show the plot
plt.show()


# In[45]:



import matplotlib.pyplot as plt
  

    
# x axis values
x =Exemple_4_unit_time["time"] 
# corresponding y axis values
y = Exemple_4_unit_time["customer_class"]
  
# plotting points as a scatter plot
plt.scatter(x, y, label= "Client : 0=A & 1=B", color= "green", 
            marker= "*", s=200)
  
# x-axis label
plt.xlabel('temps')
# frequency label
plt.ylabel('Classe du client entrant dans le système')
# plot title
plt.title('Evolution des clients dans le système pendant 4 unités de temps ')
# showing legend
plt.legend()
  
# function to show the plot
plt.show()

