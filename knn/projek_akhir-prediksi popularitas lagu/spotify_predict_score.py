import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ambil data
df = pd.read_csv('top10s.csv')
x = df.drop(['Unnamed: 0', 'title', 'artist', 'top genre', 'year','pop'], axis=1)
x = x.values
y = df['pop'].values

y_baru = []

i = 0
while(i < y.shape[0]):
    if y[i] < 50:
        y_baru.append(1)
    elif y[i] < 71:
        y_baru.append(2)
    else:
        y_baru.append(3)
    i = i + 1

def get_pred(x_train, y_train, x_test):
    # preprocessing
    # scalling features dengan standar score
    model_pp = StandardScaler()
    x_train = model_pp.fit_transform(x)
    x_test = model_pp.transform(x_test)
    
    # training model knn
    K = 5
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    
    return y_pred
def do_input():
    global x, y_baru
    bpm = int(input('Beat Per Minute (Tempo dari lagu): '))
    nrgy = int(input('Energy (Makin besar nilainya makin energic lagunya): '))
    dnce = int(input('Danceability (Kemampuan lagu untuk membuat pendengrnya bergoyang): '))
    dB = int(input('Loudness (Kebisingan lagu): '))
    live = int(input('Liveness (Semakin tinggi, semakin besar kemungkinan lagu tersebut direkam secara langsung) : '))
    val = int(input('Valence (Semakin tinggi nilainya, semakin positif mood untuk lagu tersebut): '))
    dur = int(input('Duration (durasi lagu-dalam detik-): '))
    acous = int(input('Acousticness (Tingkat beat akustik pada lagu): '))
    spch = int(input('Speechiness (Banyak kata yang diucapkan): '))
    
    data_test = [[bpm, nrgy, dnce, dB, live, val, dur, acous, spch]]
    popularity = get_pred(x, y_baru, data_test)
    if popularity[0] == 1:
        print('\nPopularity of the song is bad \n')
    elif popularity[0] == 2:
        print('\nPopularity of the song is normal \n')
    else:
        print('\nPopularity of the song is good\n')       
def get_acc():
    global x, y_baru
    x_train, x_test, y_train, y_test = train_test_split(x, y_baru, test_size=0.2, random_state=10)
    y_pred = get_pred(x, y_baru, x_test)
    acc = accuracy_score(y_test, y_pred)
    return acc
def show_menu():
    print('[1] Prediksi popularitas lagu')
    print('[2] Akurasi model')
    print('[3] Exit')
    ans = int(input('Pilih : '))
    
    if ans == 1:
        do_input()
        return 1
    elif ans == 2:
        print(f'Akurasi model: {get_acc()}\n')
        return 1
    else:
        return 0

stop = 1
while stop == 1:
    stop = show_menu()
