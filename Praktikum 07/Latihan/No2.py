def ABC():
    try:
        while True:
            xxx='XXXX\n'
            file.write(xxx)
            print('Data yang mau ditambahkan: ',xxx)
            print('Mau lagi(y/n): ',end=' ')
            b=input()
            if b == 'y':
                continue
            if b == 'n':
                break
    except ValueError():
        print('Input tidak valid')
namafile=input('Masukkan nama file : ')
file=open(namafile,'a')
ABC()
file.close()