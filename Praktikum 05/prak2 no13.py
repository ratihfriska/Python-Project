hitung = 0
from random import randint
while True:
    bil = randint(0,10)
    print(bil)
    hitung += 1
    if bil == 5:
        break
print("Jumlah perulangan :  ",hitung)