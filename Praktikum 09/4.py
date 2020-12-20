def randomString():
    import random
    n=int(input('Masukkan nilai n : '))
    a=input('Masukkan Kata : ')
    e=len(a)
    f=e**2
    if n>f :
        print('Nilai yang diinginkan terlalu banyak')
        exit()
    i=0
    b=[]
    for i in range (n):
        c=random.sample(a,e)
        b+=[''.join(c)]
    print(b)
randomString()