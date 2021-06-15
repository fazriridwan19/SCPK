import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelBinarizer

df = pd.read_csv('data_lulus_tepat_waktu.csv')
x = df.values
x = np.delete(x, 4, axis=1)
y = df['tepat'].values

lb = LabelBinarizer()
y = lb.fit_transform(y)
y = y.flatten()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

nb_clf = GaussianNB()
nb_clf.fit(x_train, y_train)

#x_test2 = np.array([[4, 3, 3.2, 3.1]])

y_pred = nb_clf.predict(x_test)
#result = nb_clf.predict_proba(x_test2)
#print(f'kemungkinan tidak lulus tepat waktu : {result[0][0]}')
#print(f'kemungkinan lulus tepat waktu : {result[0][1]}')
print(round(accuracy_score(y_test, y_pred), 3))