#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
from ydata_profiling import ProfileReport
#Étape 1 : Exploration des données avec Pandas


# In[24]:


#1.Téléchargez l'ensemble de données fourni
#2.Utilisez pandas pour lire le fichier dans un Dataframe pandas.
Edat = pd.read_csv("/Users/mac/Desktop/GoMyCode/EDUCATION_ATTAINMENT.csv")


# In[25]:


Edat.head()


# In[26]:


#3.Afficher des informations générales sur l'ensemble de données.
Edat.info()


# In[27]:


#4.Exécutez une analyse descriptive sur l'ensemble de données à l'aide de la fonction
Edat.describe()


# In[30]:


#Étape 2 : Exploration des données avec ydata-profiling
#1.Utilisez ydata-profiling pour générer un rapport de l'ensemble de données fourni.

Profile = ProfileReport(Edat, title = "Report Edat")


# In[32]:


#2.Recherchez les valeurs manquantes dans l'ensemble de données.
#Vous pouvez utiliser le rapport généré par ydata pour identifier les valeurs manquantes.
Profile.to_file('Mon Rapport.html')


# In[33]:


#3.Examinez les corrélations entre les différentes colonnes de l’ensemble de données.
#Vous pouvez utiliser le rapport généré par ydata pour identifier les corrélations.
#Reponse :Tout les variables pourcentage de reussite par tranche age sont fortement correles avec la variable annee, sauf pour la variable country.


# In[1]:


#4 Identifiez tous les autres modèles ou informations intéressants dans l'ensemble de données que vous pouvez découvrir grâce au rapport de profilage ydata.
#Reponse: La sortie nous donne aussi des informations sur les donnees manquantes, la dimension de la base(nombre d'observation et de variables),
#le pourcentage de ces donnees manquantes et les nombres de doublons, les types de variables(Numeric et text).


# In[ ]:


#4. Etape 3: Summary
# Ce rapport nous fait une statistique descriptive de notre jeu de donnees. des informations sur les donnees manquantes( le nombre et le pourcentage),
#mais aussi sur les doublons et la correlation entre les variables tranches d'ages et les annees.

