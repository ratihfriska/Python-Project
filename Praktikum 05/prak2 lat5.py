from random import randint
bil=randint(0,100)
print("Hai.. nama saya Ms. Ratih Cangtip, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
while True:
    tbkn=int(input("Tebakan Anda  : "))
    if(tbkn<0) or (tbkn>100):
        print("error!!!")
        exit()
    if (tbkn>=0) and (tbkn<=100):
        if(tbkn>bil):
            print("Hehehe... Bilangan tebakan anda terlalu besar")
        if(tbkn<bil):
            print("Hehehe... Bilangan tebakan anda terlalu kecil")
        if(tbkn==bil):
            print("Yeeee... Bilangan tebakan anda BENAR :-)")
            break