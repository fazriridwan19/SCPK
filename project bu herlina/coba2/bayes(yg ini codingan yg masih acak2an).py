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

freq_d1 = len(df[df['Contraceptive Method Used']==1])
freq_d2 = len(df[df['Contraceptive Method Used']==2])
freq_d3 = len(df[df['Contraceptive Method Used']==3])

freq_c1_d1 = len(count_age[count_age['Contraceptive Method Used']==1])
freq_c1_d2 = len(count_age[count_age['Contraceptive Method Used']==2])
freq_c1_d3 = len(count_age[count_age['Contraceptive Method Used']==3])

freq_c2_d1 = len(count_edu[count_edu['Contraceptive Method Used']==1])
freq_c2_d2 = len(count_edu[count_edu['Contraceptive Method Used']==2])
freq_c2_d3 = len(count_edu[count_edu['Contraceptive Method Used']==3])

freq_c3_d1 = len(count_partner_edu[count_partner_edu['Contraceptive Method Used']==1])
freq_c3_d2 = len(count_partner_edu[count_partner_edu['Contraceptive Method Used']==2])
freq_c3_d3 = len(count_partner_edu[count_partner_edu['Contraceptive Method Used']==3])

freq_c4_d1 = len(count_num_child[count_num_child['Contraceptive Method Used']==1])
freq_c4_d2 = len(count_num_child[count_num_child['Contraceptive Method Used']==2])
freq_c4_d3 = len(count_num_child[count_num_child['Contraceptive Method Used']==3])

freq_c5_d1 = len(count_relig[count_relig['Contraceptive Method Used']==1])
freq_c5_d2 = len(count_relig[count_relig['Contraceptive Method Used']==2])
freq_c5_d3 = len(count_relig[count_relig['Contraceptive Method Used']==3])

freq_c6_d1 = len(count_current_work[count_current_work['Contraceptive Method Used']==1])
freq_c6_d2 = len(count_current_work[count_current_work['Contraceptive Method Used']==2])
freq_c6_d3 = len(count_current_work[count_current_work['Contraceptive Method Used']==3])

freq_c7_d1 = len(count_husb_occu[count_husb_occu['Contraceptive Method Used']==1])
freq_c7_d2 = len(count_husb_occu[count_husb_occu['Contraceptive Method Used']==2])
freq_c7_d3 = len(count_husb_occu[count_husb_occu['Contraceptive Method Used']==3])

freq_c8_d1 = len(count_standart_liv[count_standart_liv['Contraceptive Method Used']==1])
freq_c8_d2 = len(count_standart_liv[count_standart_liv['Contraceptive Method Used']==2])
freq_c8_d3 = len(count_standart_liv[count_standart_liv['Contraceptive Method Used']==3])

freq_c9_d1 = len(count_media_expo[count_media_expo['Contraceptive Method Used']==1])
freq_c9_d2 = len(count_media_expo[count_media_expo['Contraceptive Method Used']==2])
freq_c9_d3 = len(count_media_expo[count_media_expo['Contraceptive Method Used']==3])

p_c1_d1 = freq_c1_d1/freq_d1
p_c1_d2 = freq_c1_d2/freq_d2
p_c1_d3 = freq_c1_d3/freq_d3

p_c2_d1 = freq_c2_d1/freq_d1
p_c2_d2 = freq_c2_d2/freq_d2
p_c2_d3 = freq_c2_d3/freq_d3

p_c3_d1 = freq_c3_d1/freq_d1
p_c3_d2 = freq_c3_d2/freq_d2
p_c3_d3 = freq_c3_d3/freq_d3

p_c4_d1 = freq_c4_d1/freq_d1
p_c4_d2 = freq_c4_d2/freq_d2
p_c4_d3 = freq_c4_d3/freq_d3

p_c5_d1 = freq_c5_d1/freq_d1
p_c5_d2 = freq_c5_d2/freq_d2
p_c5_d3 = freq_c5_d3/freq_d3

p_c6_d1 = freq_c6_d1/freq_d1
p_c6_d2 = freq_c6_d2/freq_d2
p_c6_d3 = freq_c6_d3/freq_d3

p_c7_d1 = freq_c7_d1/freq_d1
p_c7_d2 = freq_c7_d2/freq_d2
p_c7_d3 = freq_c7_d3/freq_d3

p_c8_d1 = freq_c8_d1/freq_d1
p_c8_d2 = freq_c8_d2/freq_d2
p_c8_d3 = freq_c8_d3/freq_d3

p_c9_d1 = freq_c9_d1/freq_d1
p_c9_d2 = freq_c9_d2/freq_d2
p_c9_d3 = freq_c9_d3/freq_d3

p_d1 = freq_d1/df.size
p_d2 = freq_d2/df.size
p_d3 = freq_d3/df.size

p_test_d1 = p_c1_d1 * p_c2_d1 * p_c3_d1 * p_c4_d1 * p_c5_d1 * p_c6_d1 * p_c7_d1 * p_c8_d1 * p_c9_d1 * p_d1
p_test_d2 = p_c1_d2 * p_c2_d2 * p_c3_d2 * p_c4_d2 * p_c5_d2 * p_c6_d2 * p_c7_d2 * p_c8_d2 * p_c9_d2 * p_d2
p_test_d3 = p_c1_d3 * p_c2_d3 * p_c3_d3 * p_c4_d3 * p_c5_d3 * p_c6_d3 * p_c7_d3 * p_c8_d3 * p_c9_d3 * p_d3

result = np.array([p_test_d1, p_test_d2, p_test_d3])
print(f'Probabilitas wanita tersebut tidak menggunakan kontrasepsi : {result[0]}')
print(f'Probabilitas wanita tesebut menggunakan kontrasepsi jangka panjang : {result[1]}')
print(f'Probabilitas wanita tersebut menggunakan kontrasepsi jangka pendek : {result[2]}')

if result.max() == result[0]:
    print('Kemungkinan wanita ini tidak menggunakan kontrasepsi')
elif result.max() == result[1]:
    print('Kemungkinan wanita ini akan menggunakan kontrasepsi jangka panjang')
else:
    print('Kemungkinan wanita ini akan menggunakan kontrasepsi pendek')
        
