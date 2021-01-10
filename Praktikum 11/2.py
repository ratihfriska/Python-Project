from datetime import *
def pinjam():
    kode=(input('Masukkan Kode Member   : '))
    nama=((input('Masukkan Nama Member  : ')))
    judul=((input('Masukkan Judul Buku  : ')))
    mydata=open('d:mydata.txt','w')
    tglpinjam=datetime.date(datetime.now())
    tglkembali= tglpinjam + timedelta(days=7)
    mydata.write(kode + '|' + nama + '|' + judul + '|' + str(tglpinjam) + '|' + str(tglkembali)+'\n')
    while True:
        lagi=input('Tambah data lagi? (Y/N) : ')
        if lagi=='Y' or lagi=='y' :
            kode=(input('Masukkan Kode Member   : '))
            nama=((input('Masukkan Nama Member  : ')))
            judul=((input('Masukkan Judul Buku  : ')))
            mydata=open('d:mydata.txt','a+')
            tglpinjam=datetime.date(datetime.now())
            tglkembali= tglpinjam + timedelta(days=7)
            mydata.write(kode + '|' + nama + '|' + judul + '|' + str(tglpinjam) + '|' + str(tglkembali)+'\n')
        if lagi=='N' or lagi=='n':
            mydata=open('d:mydata.txt','r')
            print(mydata.read())
            mydata.close()
            break
pinjam()