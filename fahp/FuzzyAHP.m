function [bobotAntarKriteria, relasiAntarKriteria] = FuzzyAHP(relasiAntarKriteria, TFN)
fuzzyRelasi = {};
[jumlahData, jumlahKriteria] = size(relasiAntarKriteria);

%* Lakukan konversi masing-masing relasi antar kriteria menjadi TFN (Triangular Fuzzy Number) (poin 6a - 6b)
%6a. Lakukan perhitungan pada matriks relasi antar kriteria
%Masukkan nilai pada bagian segitiga bawah sesuai dengan nilai sesuai pada poin 3.
    for i=1:jumlahData
        for j=i+1:jumlahData
            relasiAntarKriteria(j,i) = 1/relasiAntarKriteria(i,j);
        end
    end
    
%6b. Lakukan perhitungan pada matriks relasi antar kriteria
%Jika nilai matriks relasi antar kriteria lebih dari 1,
%maka nilai TFN yang digunakan adalah nilai kriteria padakelompok pertama
%Jika nilai matriks relasi antar kriteria kurang dari 1,
%maka nilai TFN yang digunakan adalah nilai kriteria padakelompok kedua
    for i=1:jumlahData
        for j=1:jumlahKriteria
            kriteria = relasiAntarKriteria(i,j);
            if kriteria >= 1
                fuzzyRelasi{i,j} = TFN{kriteria, 1};
            else
                fuzzyRelasi{i,j} = TFN{round(kriteria^-1), 2};
            end
        end
    end
%6c. Hitung jumlah dari masing-masing TFN yang dipakai dalam matriks relasi antar kriteria
%Kemudian dari nilai tersebut, jumlahkan nilai pada masing-masing kolom kriteria
    for i=1:jumlahData
        barisRelasi = [fuzzyRelasi{i,:}];
        jumlahRelasiPerBaris{1,i} = sum(reshape(barisRelasi, 3, [])');
    end
relasiPerData = [jumlahRelasiPerBaris{1,:}];
jumlahRelasiPerKolom = sum(reshape(relasiPerData,3,[])');
%6d. Lakukan perhitungan pada masing-masing nilai relasi pada masing-masing kolom
%Lakukan pembagian dengan jumlah relasi pada masing-masing kolom
%Kemudian catat jumlah dari pembagian tersebut untuk setiap kolomnya
    for i=1:jumlahData
        relasiPerData = [jumlahRelasiPerBaris{1,i}];
        for j=1:3
            nilaiRelasiPerKolom = jumlahRelasiPerKolom(1,j);
            jumlahPerKolom(1,j) = (relasiPerData(1,j))*(1/nilaiRelasiPerKolom);
        end
        jumlahRelasiPerBaris{1,i} = jumlahPerKolom;    
    end

derajatKemungkinan = zeros(jumlahData*(jumlahData-1), 3);
idxBaris = 1;

%6e. Lakukan perhitungan pada masing-masing data dengan indeks baris dan kolom tidak sama
for i=1:jumlahData
    for j=1:jumlahData
        if i ~= j
            %6f. Masukkan nilai awal derajat kemungkinan, M1, dan M2 sesuai rumus yang telah dijelaskan sebelumnya
            derajatKemungkinan(idxBaris, [1 2]) = [i j];
            M1 = jumlahRelasiPerBaris{1,i};
            M2 = jumlahRelasiPerBaris{1,j};
            
            %6g. Hitung nilai derajat kemungkinan menggunakan rumus yang telah dijelaskan sebelumnya
            if M1(1,2) >= M2(1,2)
                derajatKemungkinan(idxBaris, 3) = 1;
            elseif M2(1,1) >= M1(1, 3)
                derajatKemungkinan(idxBaris, 3) = 0;
            else
                derajatKemungkinan(idxBaris, 3) = (M2(1,1)-M1(1,3))/((M1(1,2)-M1(1,3))-(M2(1,2)-M2(1,1)));
            end
            idxBaris = idxBaris+1;
        end
    end
end
%6h. Hitung nilai bobot menggunakan nilai derajat kemungkinan minimal pada masing-masing kriteria
bobotAntarKriteria = zeros(1,jumlahData);
for i=1:jumlahData
    bobotAntarKriteria(1,i) = min(derajatKemungkinan([find(derajatKemungkinan(:,1) == i)], [3]));
end
%6i. Lakukan normalisasi terhadap nilai bobot yang telah dihitung
%yaitu dengan cara membagi masing-masing nilai bobot dengan total semua bobot
bobotAntarKriteria = bobotAntarKriteria/sum(bobotAntarKriteria);
end