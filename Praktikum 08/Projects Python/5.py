def kuadrat():
    a=len(bil)
    n=0
    e=[]
    for n in range (a):
        total=bil[n]*bil[n]
        e+=[total]
    print('Hasil kuadrat : ',e)
bil = [1,2,3,4,5,6,7,8,9,10]
print('bil : ', bil)
kuadrat()