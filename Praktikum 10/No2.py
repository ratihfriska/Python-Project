myFile=open('d:data2.txt','w')
myFile.write(input('Masukkan NIM : '))
myFile.write('|')
myFile.write((input('Masukkan Nama Mahasiswa : ')))
myFile.write('|')
myFile.write((input('Masukkan kota : ')))
a=input('y/n : ')
while True:
    if a=='y' :
        myFile.write('\n')
        myFile.write(input('Masukkan NIM : '))
        myFile.write('|')
        myFile.write((input('Masukkan Nama Mahasiswa : ')))
        myFile.write('|')
        myFile.write((input('Masukkan kota :')))
        a=input('y/n : ')
    if a=='n' :
        myFile.close()
        break