try:
    buah = {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }
    print('nama buah yang dibeli : ',end=' ')
    buah1=input()
    c=buah[buah1]
    print('Berapa Kg               ', end=' ')
    kg=int(input())
    print('--------------------------------------')
    print('Total Harga              ',c*kg)
except KeyError:
    print('Buah tidak tersedia atau input tidak valid')
except ValueError:
    print('Masukkan bilangan bulat saja')