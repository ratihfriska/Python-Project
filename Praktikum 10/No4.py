myFile=open('d:data2.txt','r')
f=input('Masukkan NIM :')
x=0
n=0
for a in myFile:
    b=a.split('|')
    c=b[0]
    d=b[1]
    e=b[2]
    dataMhs={'nim':c,'nama':d,'alamat':e}
    if f==dataMhs['nim']:
        print('Data Mahasiswa:')
        print('NIM : ', dataMhs['nim'])
        print('Nama :', dataMhs['nama'])
        print('Alamat : ', dataMhs['alamat'])
        myFile.close()
        break
if f !=dataMhs['nim']:
    print('Data tidak ditemukan')
    myFile.close()