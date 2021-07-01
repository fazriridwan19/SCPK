# 1. Age - age of the woman
#   if age < 26 then 'young', category = 1
#   if age < 41 then 'adult', category = 2
#   else 'old', category = 3
# 2. Education - level of education woman has received (1=low, 4=high)
# 3. Partner Education - level of education partner has received (1=low, 4=high)
# 4. Number of Children - number of kids mothered by woman
#   if num < 4 then 'low', category = 1
#   if num < 10 then 'medium', category = 2
#   else then 'high', category = 3
# 5. Religion=Islam - woman that identify as Muslim (0=No, 1=Yes)
# 6. Currently Working - woman is currently employed (0=Yes, 1=No)
# 7. Husbands Occupation - Not specified (categorical 1-4)
# 8. Standard of Living - based on the standard of living index (1=low, 4=high)
# 9. Media exposure - quality of media exposure (0=Good, 1=Not good)
# 10. Contraceptive Method Used - 1=No-use, 2=Long-term, 3=Short-term

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('1987_Indonesia_Contraception_Prevalence_Study.csv')

# menentukan kategori decision yang ada pada data frame
class_dec = np.array(df['Contraceptive Method Used'].drop_duplicates())

# menentukan jumlah klasifikasi decision dan jumlah kategori/kolom
sizeof_class = class_dec.size
sizeof_columns = df.shape[1]-1
sizeof_line = df.shape[0]

# labeling data
age = df['Age'].values
num_child = df['Number of Children'].values
i = 0
while i < sizeof_line:
    # labeling pada kolom age
    if age[i] < 26:
        age[i] = 1
    elif age[i] < 41:
        age[i] = 2
    else:
        age[i] = 3
    
    #labeling pada kolom number of children
    if num_child[i] < 4:
        num_child[i] = 1
    elif num_child[i] < 10:
        num_child[i] = 2
    else:
        num_child[i] = 3
    i = i + 1
df['Age'] = age
df['Number of Children'] = num_child

# ---------------------------membagi dataset---------------------------------------------
x = df.drop(['Contraceptive Method Used'], axis=1)
x = x.values
y = df['Contraceptive Method Used'].values
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=1234)
# --------------------------------------------------------------------------------------

#data_test = x_test[15]
#print(data_test)

# fungsi perkalian
def perkalian(p_c_d, i, j):
    global sizeof_columns

    if i == sizeof_columns:
        return 1
    else:
       return p_c_d[i][j] * perkalian(p_c_d, i+1, j)
def train_bayes(df, data_test):
    # ambil data
    count_age = df[df['Age']==data_test[0]]
    count_edu = df[df['Education']==data_test[1]]
    count_partner_edu = df[df['Partner Education ']==data_test[2]]
    count_num_child = df[df['Number of Children']==data_test[3]]
    count_relig = df[df['Religion = Islam']==data_test[4]]
    count_current_work = df[df['Currently working']==data_test[5]]
    count_husb_occu = df[df['Husband Occupation ']==data_test[6]]
    count_standart_liv = df[df['Standard of Living']==data_test[7]]
    count_media_expo = df[df['Media Exposure']==data_test[8]]
     
    # menghitung banyaknya kemunculan untuk setiap decision/class
    i = 0
    freq_d = np.zeros((sizeof_class))
    while i < sizeof_class:
        freq_d[i] = len(df[df['Contraceptive Method Used']==class_dec[i]])
        i = i + 1
    
    # menghitung banyaknya kemunculan untuk setiap kombinasi kategori dan decision
    j = 0
    freq_c_d = np.zeros((sizeof_columns, sizeof_class))
    while j < sizeof_class:
        freq_c_d[0][j] = len(count_age[count_age['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[1][j] = len(count_edu[count_edu['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[2][j] = len(count_partner_edu[count_partner_edu['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[3][j] = len(count_num_child[count_num_child['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[4][j] = len(count_relig[count_relig['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[5][j] = len(count_current_work[count_current_work['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[6][j] = len(count_husb_occu[count_husb_occu['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[7][j] = len(count_standart_liv[count_standart_liv['Contraceptive Method Used']==class_dec[j]])
        freq_c_d[8][j] = len(count_media_expo[count_media_expo['Contraceptive Method Used']==class_dec[j]])
        j = j + 1
    
    # menghitung probabilitas kemunculan untuk setiap kombinasi kategori dan decision/class 
    p_c_d = np.zeros((sizeof_columns, sizeof_class))
    i = 0
    while i < sizeof_columns:
        j = 0
        while j < sizeof_class:
            p_c_d[i][j] = freq_c_d[i][j]/freq_d[j]
            j = j + 1
        i = i + 1
    
    # mnghitung probabilitas  kemunculan setiap decision yang ada pada data frame
    p_d = np.zeros((sizeof_class))
    i = 0
    while i < sizeof_class:
        p_d[i] = freq_d[i]/sizeof_line
        i = i + 1
    
    # menghitung probabilitas dari decision saat diketahui kondisi data_test         
    p_test_d = np.zeros((sizeof_class))
    i = 0
    while i < sizeof_class:
        p_test_d[i] = perkalian(p_c_d, 0, i) * p_d[i]
        i = i + 1
    
    #print(f'freq-c-d : \n{freq_c_d}\n')
    #print(f'freq-d:\n{freq_d}\n')
    #print(f'prob(c|d):\n{p_c_d}\n')
    #print(f'prob(d):\n{p_d}\n')
    #print(f'prob(test|d):\n{p_test_d}\n')
    if max(p_test_d) == p_test_d[0]:
        return 1
    elif max(p_test_d) == p_test_d[1]:
        return 2
    else:
        return 3

'''
test di 20% data asli

y_pred = np.zeros((x_test.shape[0]))
for i in range(x_test.shape[0]):
    y_pred[i] = train_bayes(df, x_test[i])
    
acc_score = accuracy_score(y_test, y_pred)
print(f'accuracy score:{acc_score}')
'''

'''
test di 20 data asli
'''
test = pd.read_excel('train.xlsx')
x_test2 = test.drop(['Contraceptive Method Used'], axis=1)
x_test2 = x_test2.values
y_test2 = test['Contraceptive Method Used'].values
y_pred = np.zeros((x_test2.shape[0]))
for i in range(x_test2.shape[0]):
    y_pred[i] = train_bayes(df, x_test2[i])
acc_score = accuracy_score(y_test2, y_pred)
print(f'accuracy score:{acc_score}')

'''
pred = train_bayes(df, [3, 3, 4, 1, 1, 1, 2, 3, 0])
if pred == 1:
    print('cmu : no-use')
elif pred == 2:
    print('cmu : long-term')
else:
    print('cmu : short-term')
'''

































# p_test_d[0] = p_c_d[0][0] * p_c_d[1][0] * p_c_d[2][0] * p_c_d[3][0] * p_c_d[4][0] * p_c_d[5][0] * p_c_d[6][0] * p_c_d[7][0] * p_c_d[8][0]
# p_test_d[1] = p_c_d[0][1] * p_c_d[1][1] * p_c_d[2][1] * p_c_d[3][1] * p_c_d[4][1] * p_c_d[5][1] * p_c_d[6][1] * p_c_d[7][1] * p_c_d[8][1]
# p_test_d[2] = p_c_d[0][2] * p_c_d[1][2] * p_c_d[2][2] * p_c_d[3][2] * p_c_d[4][2] * p_c_d[5][2] * p_c_d[6][2] * p_c_d[7][2] * p_c_d[8][2]
# print(p_test_d[0])
# print(p_test_d[1])
# print(p_test_d[2])