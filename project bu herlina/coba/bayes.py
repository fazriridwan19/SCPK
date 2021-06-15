import pandas as pd
import numpy as np

data = pd.read_excel('decision.xlsx')
x_train = np.array(data[['wheater','parents', 'money','decision']])
dec = data['decision']
dec = np.array(dec.drop_duplicates())
x_test = np.array(['windy','yes','poor'])

print(f'x_train:\n{x_train}\n')
print(f'x_test:\n{x_test}\n')

sun_cin = 0
sun_ten = 0
sun_sta = 0

par_cin = 0
par_ten = 0
par_sta = 0

poor_cin = 0
poor_ten = 0
poor_sta = 0

count_cin = 0
count_ten = 0
count_sta = 0
i = 0
for row in x_train:
    if dec[0] in row:
        count_cin = count_cin + 1
    if dec[1] in row:
        count_ten = count_ten + 1
    if dec[2] in row:
        count_sta = count_sta + 1
        
    if x_test[0] in row and dec[0] in row:
        sun_cin = sun_cin + 1
    if x_test[0] in row and dec[1] in row:
        sun_ten = sun_ten + 1
    if x_test[0] in row and dec[2] in row:
        sun_sta = sun_sta + 1
    
    if x_test[1] in row and dec[0] in row:
        par_cin = par_cin + 1
    if x_test[1] in row and dec[1] in row:
        par_ten = par_ten + 1
    if x_test[1] in row and dec[2] in row:
        par_sta = par_sta + 1
        
    if x_test[2] in row and dec[0] in row:
        poor_cin = poor_cin + 1
    if x_test[2] in row and dec[1] in row:
        poor_ten = poor_ten + 1
    if x_test[2] in row and dec[2] in row:
        poor_sta = poor_sta + 1
        
p_sun_cin = sun_cin/count_cin
p_sun_ten = sun_ten/count_ten
p_sun_sta = sun_sta/count_sta

p_par_cin = par_cin/count_cin
p_par_ten = par_ten/count_ten
p_par_sta = par_sta/count_sta

p_poor_cin = poor_cin/count_cin
p_poor_ten = poor_ten/count_ten
p_poor_sta = poor_sta/count_sta

p_cin = count_cin/len(x_train)
p_ten = count_ten/len(x_train)
p_sta = count_sta/len(x_train)

p_x_cin = p_sun_cin * p_par_cin * p_poor_cin * p_cin
p_x_ten = p_sun_ten * p_par_ten * p_poor_ten * p_ten
p_x_sta = p_sun_sta * p_par_sta * p_poor_sta * p_sta

print(f'probability for cinema : {p_x_cin}')
print(f'probability for tennis : {p_x_ten}')
print(f'probability for stay in : {p_x_sta}')