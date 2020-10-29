kode=input("Masukkan kode karyawan  ")
nama=input("Masukkan nama karyawan  ")
gol=input("Masukkan golongan       ")
if(gol=='A') or (gol=='a'):
    gjpkk=10000000
    pot=(2.5)/100
if(gol=='B') or (gol=='b'):
    gjpkk=8500000
    pot=(2.0)/100
if(gol=='C') or (gol=='c'):
    gjpkk=7000000
    pot=(1.5)/100
if(gol=='D')or(gol=='d'):
    gjpkk=5500000
    pot=(1.0)/100
potfix=pot*gjpkk
gjbrsh=gjpkk-potfix
print("==============================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Nama Karyawan        : ",kode)
print("Golongan             : ",gol)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
print("Gaji Pokok           : Rp", gjpkk)
print("Potongan (",pot*100,"%)","   : Rp",potfix)
print("....................................-")
print("Gaji Bersih          : Rp" ,gjbrsh)