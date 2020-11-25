def ABC():
    try:
        z=input('Masukkan nama file : ')
        file=open(z,'a')
        while True:
            print('Data yang mau ditambahkan: ',end='')
            xxx=input()
            file.write(xxx)
            print('Mau lagi(y/n): ',end=' ')
            b=input()
            if b == 'y':
                continue
            elif b == 'n':
                break
            else:
                print('Input tidak valid')
                break
        file.close()
    except OSError:
        print('Input tidak valid atau file tidak ada')
    except ValueError:
        print('Input tidak valid')
ABC()