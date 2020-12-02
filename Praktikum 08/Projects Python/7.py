def buahMahal():
    buah = {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }
    d=list(buah.values())
    d.sort(reverse=True)
    max=d[0]
    for buah, d in buah.items():
        if d == max:
            print(buah,max)
buahMahal()