import math
def formasi():
    a=1
    b=0
    n=int(input('Masukkan Nilai n yang diinginkan (n harus ganjil) : '))
    if n % 2 == 0:
        print('Error Bilangan Tidak Ganjil')
        exit()
    c=1
    d=math.ceil(n/2)
    b=('*'* c)
    print(b.center(20,' '))
    while True:
        if a < d:
            a+=1
            c+=2
            b=('*'* c)
            print(b.center(20,' '))
        if a >= d and a<=n :
            c-=2
            b=('*'* c)
            print(b.center(20,' '))
            a+=1
formasi()