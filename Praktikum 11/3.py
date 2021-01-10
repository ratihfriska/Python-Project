from datetime import *
def dateDiff():
    mydata = open('d:mydata.txt', 'r')
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    for a in mydata:
        b = a.split('|')
        data1.append(b[0])
        data2.append(b[1])
        data3.append(b[2])
        data4.append(b[3])
        data5.append(b[4].strip())
    kode = str(input('Masukkan kode member : '))
    if kode in data1:
        sama = True
        a = data1.index(kode)
        skrg = datetime.now()
        b = data5[a]
        c = datetime.strptime(b, '%Y-%m-%d')
        hitung = c - skrg
        kembali = datetime.date(skrg)
        maks = datetime.date(c)
        if sama == True:
            hitung = datetime.date(skrg) - maks
            hitung = int(hitung.days)
            bayardenda = 0
            if hitung > 0:
                bayardenda = 2000 *(hitung)
                hitung = abs(hitung)
            elif hitung <= 0:
                hitung = 0
            print('Data Peminjaman Buku  ')
            print('Kode Member                    : ',data1[a],'\nNama Member                    : ',data2[a], '\nJudul Buku                     : ',data3[a])
            print('Tanggal Mulai Peminjaman       : ',data4[a], '\nTanggal Maks Peminjaman        : ',data5[a])
            print('Tanggal Pengembalian           : ',kembali, '\nTerlambat                      : ', hitung,'Hari')
            print('Denda                          :  Rp.',bayardenda)
        else:
            print('data tidak ditemukan')
            mydata.close()
            exit()
    else:
        print('data tidak ditemukan')
        mydata.close()
        exit()
dateDiff()