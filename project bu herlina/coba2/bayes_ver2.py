# Age - age of the woman
# Education - level of education woman has received (1=low, 4=high)
# Partner Education - level of education partner has received (1=low, 4=high)
# Number of Children - number of kids mothered by woman
# Religion=Islam - woman that identify as Muslim (0=No, 1=Yes)
# Currently Working - woman is currently employed (0=Yes, 1=No)
# Husbands Occupation - Not specified (categorical 1-4)
# Standard of Living - based on the standard of living index (1=low, 4=high)
# Media exposure - quality of media exposure (0=Good, 1=Not good)
# Contraceptive Method Used - 1=No-use, 2=Long-term, 3=Short-term

import pandas as pd
import numpy as np

df = pd.read_csv('1987_Indonesia_Contraception_Prevalence_Study.csv')

data_test = [43,3,4,2,1,1,2,3,0]
print(data_test)

count_age = df[df['Age']==data_test[0]]
count_edu = df[df['Education']==data_test[1]]
count_partner_edu = df[df['Partner Education ']==data_test[2]]
count_num_child = df[df['Number of Children']==data_test[3]]
count_relig = df[df['Religion = Islam']==data_test[4]]
count_current_work = df[df['Currently working']==data_test[5]]
count_husb_occu = df[df['Husband Occupation ']==data_test[6]]
count_standart_liv = df[df['Standard of Living']==data_test[7]]
count_media_expo = df[df['Media Exposure']==data_test[8]]

class_dec = np.array(df['Contraceptive Method Used'].drop_duplicates())
sizeof_class = class_dec.size
sizeof_columns = df.shape[1]-1
i = 0

freq_d = np.zeros((sizeof_class))

while i < sizeof_class:
    freq_d[i] = len(df[df['Contraceptive Method Used']==class_dec[i]])
    i = i + 1

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

p_c_d = np.zeros((sizeof_columns, sizeof_class))
i = 0
while i < sizeof_columns:
    j = 0
    while j < sizeof_class:
        p_c_d[i][j] = freq_c_d[i][j]/freq_d[j]
        j = j + 1
    i = i + 1

p_d = np.zeros((sizeof_class))
i = 0
while i < sizeof_class:
    p_d[i] = freq_d[i]/df.size
    i = i + 1

def perkalian(p_c_d, i, j):
    global sizeof_columns

    if i == sizeof_columns:
        return 1
    else:
       return p_c_d[i][j] * perkalian(p_c_d, i+1, j)
         
p_test_d = np.zeros((sizeof_class))
i = 0
while i < sizeof_class:
    p_test_d[i] = perkalian(p_c_d, 0, i) * p_d[i]
    i = i + 1




































# p_test_d[0] = p_c_d[0][0] * p_c_d[1][0] * p_c_d[2][0] * p_c_d[3][0] * p_c_d[4][0] * p_c_d[5][0] * p_c_d[6][0] * p_c_d[7][0] * p_c_d[8][0]
# p_test_d[1] = p_c_d[0][1] * p_c_d[1][1] * p_c_d[2][1] * p_c_d[3][1] * p_c_d[4][1] * p_c_d[5][1] * p_c_d[6][1] * p_c_d[7][1] * p_c_d[8][1]
# p_test_d[2] = p_c_d[0][2] * p_c_d[1][2] * p_c_d[2][2] * p_c_d[3][2] * p_c_d[4][2] * p_c_d[5][2] * p_c_d[6][2] * p_c_d[7][2] * p_c_d[8][2]
# print(p_test_d[0])
# print(p_test_d[1])
# print(p_test_d[2])