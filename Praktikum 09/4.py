def randomString():
    try:
        import random
        n=int(input('Masukkan nilai n : '))
        a=input('Masukkan Kata : ')
        e=len(a)
        f=e**2
        if n>f :
            print('Nilai yang diinginkan terlalu banyak')
            exit()
        b=[]
        for i in range (n):
            c=random.sample(a,e)
            if c in b:
                b.remove(c)
                i-=1
            b+=[''.join(c)]
        print(b)
    except ValueError:
        print('n harus angka')
randomString()