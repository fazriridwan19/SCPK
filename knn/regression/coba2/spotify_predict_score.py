# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:27:16 2021

@author: fazri
"""
import math
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ambil data
df = pd.read_csv('top10s.csv')
df_droped = df.drop(['Unnamed: 0', 'title', 'artist', 'top genre', 'year'], axis=1)
x = df_droped.values
x = np.delete(x, 9, axis=1)
y = df_droped['pop'].values
x_new = np.array([[174, 80, 30, -5, 13, 70, 120, 2, 16]])


# splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=10)

# preprocessing
# scalling features dengan standar score
ss = StandardScaler()
x_train_scaled = ss.fit_transform(x_train)
x_test_scaled = ss.transform(x_test)
x_new_scaled = ss.transform(x_new)

# training model knn
K = 3
model = KNeighborsRegressor(n_neighbors=K)
model.fit(x_train_scaled, y_train)
y_pred = model.predict(x_test_scaled)
y_pred_new = model.predict(x_new_scaled)

# evaluasi model knn
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
print(f'prediksi x new: {y_pred_new[0]}')

