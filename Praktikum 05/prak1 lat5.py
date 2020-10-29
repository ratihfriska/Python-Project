kode=input("Masukkan kode karyawan  ")
nama=input("Masukkan nama karyawan  ")
gol=input("Masukkan golongan       ")
status=input("Masukkan status (1: menikah, 2: belum menikah)    ")
if(status=='menikah'):
    anak=int(input("Masukkan jumlah anak    "))
if(status=='belum menikah'):
    anak=0
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
if(status=='menikah'):
    tunjistrisuami= (10/100)*gjpkk
    if(anak>0):
        tunjanak=((5/100)*gjpkk)*anak
potfix=pot*gjpkk
if(status=='belum menikah'):
    gjktr=gjpkk
if(status=='menikah'):
    gjktr=gjpkk+tunjistrisuami
    if(anak>0):
        gjktr=gjpkk+tunjistrisuami+tunjanak
gjbrsh=gjktr-potfix

print("==============================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Nama Karyawan             : ",kode)
print("Golongan                  : ",gol)
print("Status Menikah            : ",status)
print("Jumlah Anak               : ",anak)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Gaji Pokok                : Rp", int(gjpkk))
if(status=='menikah'):
    print("Tunjungan Istri/Suami","    : Rp",int(tunjistrisuami))
    if(anak>0):
        print("Tunjungan Anak,           : Rp",int(tunjanak))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ + ")
print("Gaji Kotor,               : Rp", int(gjktr))
print("Potongan (",pot*100,"%)","        : Rp",int(potfix))
print(".............................................-")
print("Gaji Bersih               : Rp" ,int(gjbrsh))