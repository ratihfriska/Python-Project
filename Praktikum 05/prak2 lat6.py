from random import randint
bil=randint(0,100)
hitung=0
print("Hai.. nama saya Ms. Ratih Cangtip, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
while True:
    tbkn=int(input("Tebakan Anda  : "))
    if(tbkn<0) or (tbkn>100):
        print("error!!!")
        exit()
    if (tbkn>=0) and (tbkn<=100):
        if(tbkn>bil):
            print("Hehehe... Bilangan tebakan anda terlalu besar")
            hitung+=2
        if(tbkn<bil):
            print("Hehehe... Bilangan tebakan anda terlalu kecil")
            hitung+=2
        if(tbkn==bil):
            print("Yeeee... Bilangan tebakan anda BENAR :-)")
            break
score= 100-hitung
if(score<0):
    scorefix=0
if(score>0):
    scorefix=score
print("Score Anda:  ", scorefix)