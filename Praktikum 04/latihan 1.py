import math 
#jam rental
rental1 = int(input("jam pinjam(jam)= "))
rental2 = int(input("jam pinjam(menit)= "))
kembali1 = int(input("jam kembali(jam)= "))
kembali2 = int(input("jam kembali(menit)= "))
            
#sewa
pertama = 200000
kedua = 10000
menit = 10000/60

#perhitungan waktu
waktupinjamjam = kembali1 - rental1
waktupinjammenit = (kembali2/60) - (rental2/60)
waktupinjam = math.floor(waktupinjamjam+waktupinjammenit)

#perhitungan sewa
print("biaya sewa= Rp. ",(waktupinjam - 12)*kedua + pertama )
