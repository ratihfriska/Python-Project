try:
    a=int(input('Berapa banyak bilangan yang diinginkan? '))
    b=0
    d=[]
    for b in range (a):
        c=int(input('input bilangan bulat : '))
        d+=[c]
    d.sort(reverse=True)
    print(d)
except ValueError:
    print('Bukan Bilangan Bulat')