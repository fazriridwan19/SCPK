rt = {'RT 1','RT 2','RT 3','RT 4','RT 5','RT 6','RT 7','RT 8','RT 9','RT 10'};
data = [
    50 10 5
    60 9 10
    20 2 5
    10 4 8
    90 3 6
    100 4 2
    40 5 4
    25 6 1
    70 3 2
    11 2 3
];
maksPositif = 100;
maksMeninggal = 10;
maksOdp = 10;

data(:,1) = data(:,1)/maksPositif;
data(:,2) = data(:,2)/maksMeninggal;
data(:,3) = data(:,3)/maksOdp;

relasiAntarKriteria = [
    1 2 4
    0 1 2
    0 0 1
];

TFN = {
    [-100/3 0 100/3] [3/100 0 -3/100]
    [0 100/3 200/3] [3/200 3/100 0]
    [100/3 200/3 300/3] [3/300 3/200 3/100]
    [200/3 300/3 400/3] [3/400 3/300 3/200]
};

[RasioKonsistensi] = HitungKonsistensiAHP(relasiAntarKriteria);

if RasioKonsistensi < 0.10
    % metode fuzzy ahp
    [bobotAntarKriteria, relasiAntarKriteria] = FuzzyAHP(relasiAntarKriteria, TFN);
    
    %Hitung nilai skor akhit
    ahp = data * bobotAntarKriteria';
    
    disp('Hasil perhitungan dengan metode Fuzzy AHP');
    disp('RT           , Skor akhir, kesimpulan');
end

    for i=1:size(ahp,1)
        if ahp(i) < 0.5
            status = 'Tidak LockDown';
        else
            status = 'LockDown';
        end
        disp([char(rt(i)), blanks(13 - cellfun('length', rt(i))), ', ', ...
            num2str(ahp(i)), blanks(10 - length(num2str(ahp(i)))), ', ', ...
            char(status)]);
    end
