try:
    x=['bayam', 'kangkung', 'wortel', 'selada']
    print('Diketahui data sayur adalah sebagai berikut',x)
    print('MENU :','\nA. Tambah data sayur','\nB. Hapus data sayur','\nC. Tampilkan data sayur')
    while True:
        print('Pilihan Anda (A/B/C) : ',end=' ')
        z=input()
        if z=='A' or z=='a':
            print('Tambah data sayur : ',end=' ')
            y=input()
            x.append(y)
        elif z=='B' or z=='b':
            print('Hapus data sayur : ', end=' ')
            t=input()
            x.remove(t)
        elif z=='C' or z=='c':
            v=set(x)
            s=list(v)
            print('Menampilkan data sayur : ',)
            for f in s:
                print(f)
        else:
            print('input tidak valid')
            break
        print('Ingin memilih lagi? (y/n) : ', end=' ')
        u=input()
        if u=='Y' or u=='y':
            continue
        if u=='n' or u=='N':
            break
        else:
            print('input tidak valid')
            break
except ValueError:
    print('data tidak ditemukan')