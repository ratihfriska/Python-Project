try:
    buah = {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }
    print('nama buah yang dibeli : ',end=' ')
    buah1=input()
    d=buah[buah1]
    print('Berapa Kg               ', end=' ')
    kg=int(input())
    x=d*kg
    print('Beli Buah yang lain? (y/n) : ',end=' ')
    a=input()
    while True:
        if a=='y':
            print('nama buah yang dibeli : ',end=' ')
            buah1=input()
            c=buah[buah1]
            print('Berapa Kg               ', end=' ')
            kg1=int(input())
            print('Beli Buah yang lain? (y/n) :')
            a=input()
            d+=c
            x1=c*kg1
            x+=x1
            if a=='y':
                continue
            if a=='n':
                break
        if a=='n':
            break
        else:
            print('input tidak valid')
            exit()
    print('--------------------------------------')
    print('Total Harga              ',x)
except KeyError:
    print('Buah tidak tersedia atau input tidak valid')
except ValueError:
    print('Masukkan bilangan bulat saja')