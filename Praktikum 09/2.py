def formasi():
    a=0
    b=0
    n=int(input('Masukkan Nilai n yang diinginkan : '))
    c=1
    while a < n:
        b=('*'* c)
        print(b.center(20,' '))
        c+=2
        a+=1
formasi()