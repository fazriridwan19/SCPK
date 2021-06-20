import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# pengambilan data
df = pd.read_csv('data_lulus_tepat_waktu.csv')
x = df.values
x = np.delete(x, 4, axis=1)
y = df['tepat'].values

# labeling data
lb = LabelBinarizer()
y = lb.fit_transform(y)
y = y.flatten()

# splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

# membuat model knn dan proses training pada data
K = 3
knn_cls = KNeighborsClassifier(n_neighbors=K)
knn_cls.fit(x_train, y_train)

# memrediksi data test berdasarkan hasil data training
y_pred = knn_cls.predict(x_test)
cls_report = classification_report(y_test, y_pred)
print(f'Classification report: \n{cls_report}')


x_test2 = [[2.30, 1.97, 1.8, 1.56]]
y_pred2 = knn_cls.predict(x_test2)
print(f'data yang akan di prediksi: {x_test2[0]}')
if y_pred2[0] == 1:
    print('hasil prediksi: tepat waktu')
else:
    print('hasil prediksi: tidak tepat waktu')