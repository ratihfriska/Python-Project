print('---------------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('---------------------------------')
def hitung():
    x=0
    sum=0
    while True:
        x+=1
        try:
            bil=int(input('Masukkan bilangan bulat: '))
            sum=sum+bil
            print('Mau lagi (y/n): ',end=' ')
            b=input()
            if b == 'y':
                continue
            if b == 'n':
                rata2=sum/x
                print('Rata ratanya adalah : ',rata2)
                break
            else:
                print('Input tidak valid')
                exit()
        except ValueError:
            print('Bukan bilangan bulat')
            x-=1
hitung()