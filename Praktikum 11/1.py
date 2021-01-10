from datetime import *
import math
def diffDate(x):
    now=datetime.now()
    y=datetime.date(datetime.now())
    print('Tanggal hari ini : ',y)
    hitung=datetime.strptime(x, '%Y-%m-%d')
    selisih=now-hitung
    selisih1=abs(selisih.days)
    return selisih1
x=input('Masukkan tanggal yang diinginkan : ')
print(diffDate(x))