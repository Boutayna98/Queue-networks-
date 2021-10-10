#!/usr/bin/env python
# coding: utf-8

# # 1.Importation des bibliothèques
#  
#  
# &nbsp; 
# **ciw bibliothèque de SED des files d'attentes** 
# 
# &nbsp;
# **pandas pour  manipuler le listing** 
# 
# &nbsp;
# **matplotlib pour représentation graphiques**
# 
# &nbsp;
# **numpy pour les calcules numériques**
# 
# &nbsp;
# **math réalisation des opérations Arithmétiques** 
# 
# &nbsp;
# **seaborn Bibliothèque de la Data_Visualisation**  
# 

# In[8]:



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


# # 2.Création du réseaux des files d'attentes 
# &nbsp;
# **Classe 0 désigne les clients de type A**
# 
# &nbsp;
# **Classe 1 désigne les clients de type B**
# 
# &nbsp;
# **Chaque guichet a un seul employé**
# 
# &nbsp;
# **La matrice de routage est aussi mentionnée**
# 
# &nbsp;
# **Ici on a pas mentionné la capacité c'est par défaut infinie en cas de besoin ci dessous la syntaxe munie d'un exemple** 
# 
# &nbsp;
# queue_capacities=[5, float('inf'), float('inf'), 10]**
# 
# &nbsp;
# ***Il convient de noter qu'il existe toutes les autres lois dans la bibliothèques Ciw :**
# 

# In[9]:


N = ciw.create_network(
    #Classe 0 désigne les clients de type A 
     #Classe 1 désigne les clients de type B
     arrival_distributions={'Class 0': [ciw.dists.Exponential(8)],
                            'Class 1': [ciw.dists.Exponential(17)]},
     service_distributions={'Class 0': [ciw.dists.Exponential(20)],
                            'Class 1': [ciw.dists.Exponential(30)]},
    routing={'Class 0': [[1.0]],
             'Class 1': [[1.0]]},
    #Vecteur des probailités de changements
    class_change_matrices={'Node 1': [[0.5, 0.5],
                                     [0.75, 0.25]]},
    #Chaque guichet possède un seul employé
    number_of_servers=[1])


# # 3.Lancement de la simulation 
# **Horizon de la simulation est fixé a 10000 unités** 
# 
# &nbsp;
# **Vue que l'exécution prends beaucoup de temps on a décidé de :**
# 
# 
# &nbsp;
# $\color{red}{\text{On changera cet horizon demandée par 500 unités}}$

# In[10]:


ciw.seed(1)
Q = ciw.Simulation(N)
#Horizon de simulations
#Q.simulate_until_max_time(10000.0)
Q.simulate_until_max_time(500.0)


# # 4.Collecter la Data communément appelé "Listing"
# 

# In[11]:


DATA= Q.get_all_records()


# In[12]:


DATA


# # 5.Restituer la donnée aquise 
# ***Comme vous remarquez en haut le listing fourni en une liste de tuples ce qui n'est pas réutilisable par la suite*** 
# 
# 
# &nbsp;
# ***La bibliothèque pandas nous permettra d'organiser les données dans un tableau format CSV qu'on va convertir en format xls a l'aide Power Query***

# In[13]:


df = pd.DataFrame(DATA, columns =['id_number',"customer_class","node",
                                  "arrival_date","waiting_time","service_start_date",
                                  "service_time","service_end_date","time_blocked",
                                  "exit_date","destination","queue_size_at_arrival",
                                  "queue_size_at_departure"])


# In[14]:


df


#  # 6.Afficher le Dataframe 

# In[15]:


print(df)


# # 7.Exporter les données

# In[16]:


df.to_csv ('DATA.csv', index = False , header=True)
df
df.to_csv('DATA.csv')


# # 8.Aficher le Dataframe 

# In[17]:



df=df.rename(columns={"Unnamed: 1":"time"})


# In[18]:


df


# # 9.Nombre  total des clients réparties en deux à l'issue de la simulation 

# In[19]:



Counter([client.customer_class for client in DATA])


# In[20]:


print("On a 5623 clients de type A \n On a 6376 clients de types B ")


# # 10.Etude de la stabilité du système 

# In[21]:


#taux d'ocupation noté gho
print("le taux d'ocuppation de la file du guichet 1 est : ",8/20)


# In[22]:


print("le taux d'ocuppation de la file du guichet 2 est : ",17/30)


# __On conclue donc que le réseaux est stable puisque les deux taux d'occupation sont inférieurs à 1__ 

# In[26]:


system_times=[client.service_end_date-client.arrival_date for client in DATA]
moyenne_system_times=sum(system_times)/len(system_times)


# # 12.Représentation du pourcentage d'activité des serveurs 

# In[27]:


plt.hist(system_times);
plt.show()

print ("Pourcentage d'activité des serveurs :  "+str(Q.transitive_nodes[0].server_utilisation))


# # 13 Calcul de la durée Moyenne de séjour d'un client dans le système 

# ###                                                        Méthode : 1

# In[28]:


df_system_times=df["service_end_date"]-df["arrival_date"]


# In[29]:


df_system_times


# In[30]:


y=df_system_times.mean()


# In[31]:


print("Le temps moyen de séjour d un client est :",y)


# ### Méthode : 2 

# In[32]:


x=(df["service_time"]+df["waiting_time"]).mean()


# In[33]:


print("Le temps moyen de séjour d un client est :",x)


# ### Comparaison 

# In[34]:


print("la différence entre les résultats des deux méthode :")
print(x-y)
print("Puisque la différence est nulle on conclue que les deux méthodes sont equivalentes ")


# # 14. Le nombre moyen de clients dans chaque catégorie 

# In[36]:


N_A=(0.4/0.6)
print("le nombre moyen de client dans la file 1 est :",N_A )


# In[37]:


N_B=(0.56/0.44)
print("le nombre moyen de client dans la file 1 est :",N_B )

