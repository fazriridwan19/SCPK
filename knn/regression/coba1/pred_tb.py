#!/usr/bin/env python
# coding: utf-8

# In[1]:


# membuat dataset
import pandas as pd
sensus = {
    'tinggi': [158, 170, 183, 191, 155, 163, 180, 158, 170],
    'jk': ['pria', 'pria', 'pria', 'pria', 'wanita', 'wanita', 'wanita', 'wanita', 'wanita'],
    'berat': [64, 86, 84, 80, 49, 59, 67, 54, 67]
}

sensus_df = pd.DataFrame(sensus)
sensus_df


# In[2]:


# mengelompokkan data
import numpy as np
x_train = sensus_df.drop(['berat'], axis=1)
x_train = x_train.values
y_train = np.array(sensus_df['berat'])

print(f'x train:\n{x_train}\n')
print(f'y train:\n{y_train}')


# In[3]:


x_train_tranpose = np.transpose(x_train)
print(f'x train:\n{x_train}\n')
print(f'x train tranpose: \n{x_train_tranpose}')


# In[4]:


# labeling pada data
from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()
jk_binarized = lb.fit_transform(x_train_tranpose[1])


print(f'x train tranpose: \n{x_train_tranpose[1]}\n')
print(f'jk binarized: \n{jk_binarized}')


# In[5]:


jk_binarized = jk_binarized.flatten()
jk_binarized


# In[23]:


x_train_tranpose[1] = jk_binarized
x_train = x_train_tranpose.transpose()

print(f'x_train_tranpose:\n{x_train_tranpose}\n')
print(f'x_train:\n{x_train}')


# In[7]:


# training model
from sklearn.neighbors import KNeighborsRegressor

K=3
model = KNeighborsRegressor(n_neighbors=K)
model.fit(x_train, y_train)


# In[8]:


x_new = [[155, 1]]
x_new


# In[9]:


# prediksi model
y_pred = model.predict(x_new)
y_pred


# In[10]:


# evaluasi knn regression model
x_test = np.array([[168, 0], [180, 0], [160, 1], [169, 1]])
y_test = np.array([65, 96, 52, 67])

print(f'x_test:\n{x_test}\n')
print(f'y_test:\n{y_test}')


# In[11]:


y_pred = model.predict(x_test)
y_pred


# In[12]:


# metric score R_squared
from sklearn.metrics import r2_score
r_squared = r2_score(y_test, y_pred)
r_squared


# In[13]:


# Mean Absolute Error
# MAE = 1/n*sum from i=1 to n (|yi - y^i|)
# semakin kecil nilai MAE semakin baik
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
mae


# In[14]:


# Mean Squared Error
# MSE = 1/n*sum from i=1 to n (yi - y^i)^2
# semakin kecil nilai MSE semakin baik
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
mse


# In[16]:


# permasalahan scalling pada features
from scipy.spatial.distance import euclidean

# tinggi dalam milimeter
x_train = np.array([[1700, 0], [1600, 1]])
x_new = np.array([[1640, 0]])

[euclidean(x_new, d) for d in x_train]


# In[18]:


# tinggi dalam meter
x_train = np.array([[1.7, 0], [1.6, 1]])
x_new = np.array([[1.64, 0]])

[euclidean(x_new, d) for d in x_train]


# In[20]:


# mengatasi ketidak konsistenan pada masalah diatas
# menggunakan nilai Z atau standar score

# tinggi dalam satuan mili meter
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()

x_train = np.array([[1700, 0], [1600, 1]])
x_train_scaled = ss.fit_transform(x_train)

print(f'x_train_scaled:\n{x_train_scaled}\n')

x_new = x_new = np.array([[1640, 0]])
x_new_scaled = ss.transform(x_new)

print(f'x_new_scaled:\n{x_new_scaled}\n')

jarak = [euclidean(x_new_scaled, d) for d in x_train_scaled]
print(f'Jarak euclidean: {jarak}')


# In[21]:


# tinggi dalam satuan meter
x_train = np.array([[1.7, 0], [1.6, 1]])
x_train_scaled = ss.fit_transform(x_train)
print(f'x_train_scaled:\n{x_train_scaled}\n')

x_new = np.array([[1.64, 0]])
x_new_scaled = ss.transform(x_new)
print(f'x_new_scaled:\n{x_new_scaled}\n')

jarak = [euclidean(x_new_scaled, d) for d in x_train_scaled]
print(f'Jarak euclidean: {jarak}')


# In[25]:


# perbaikan dalam program dengan memberi features scalling
x_train = np.array([[158, 0], [170, 0], [183, 0], [191, 0], [155, 1], [163, 1], [180, 1], [158, 1], [170, 1]])
y_train = np.array([64, 86, 84, 80, 49, 59, 67, 54, 67])
x_test = np.array([[168, 0], [180, 0], [160, 1], [169, 1]])
y_test = np.array([65, 96, 52, 67])

print(f'x train:\n{x_train}\n')
print(f'y train:\n{y_train}\n')
print(f'x_test:\n{x_test}\n')
print(f'y_test:\n{y_test}')


# In[26]:


# features scalling
x_train_scaled = ss.fit_transform(x_train)
x_test_scaled = ss.transform(x_test)

print(f'x train scaled:\n{x_train_scaled}\n')
print(f'x_test scaled:\n{x_test_scaled}\n')


# In[28]:


# training dan evaluasi model
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f'MAE: \n{mae}\n')
print(f'MSE: \n{mse}\n')


# In[ ]:




