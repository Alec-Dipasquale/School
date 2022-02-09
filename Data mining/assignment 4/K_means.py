#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

DFS = pd.read_csv("./heart.csv", sep=",")


Scale= StandardScaler(with_mean=0, with_std=1)
DF = Scale.fit_transform(DFS)
from sklearn.cluster import KMeans
KMC = KMeans(n_clusters = 2)
KMC.fit(DF)
center_age = [KMC.cluster_centers_[0][0], KMC.cluster_centers_[1][0]]
center_thalachh = [KMC.cluster_centers_[0][5],KMC.cluster_centers_[1][5]]

plt.figure(figsize = (20,10))
plt.subplot(1,2,1)
sns.scatterplot(x="age", y="thalachh", data=DFS, hue = KMC.labels_, s=55)
plt.title("Maximum Heart Rate")
plt.xlabel("Age")
plt.ylabel("Max Heart Rate")

plt.figure(figsize = (20,10))
plt.subplot(1,2,1)
sns.scatterplot(x="age", y="chol", data=DFS, hue = KMC.labels_, s=55)
plt.title("Cholestrol")
plt.xlabel("Age")
plt.ylabel("Cholestrol in Mg")

plt.figure(figsize = (20,10))
plt.subplot(1,2,1)
sns.scatterplot(x="age", y="trtbps", data=DFS, hue = KMC.labels_, s=55)
plt.title("Resting Blood Pressure")
plt.xlabel("Age")
plt.ylabel("Resting Blood Pressure")


# In[ ]:





# In[ ]:




