jumlah = 0
sum = 0
i=0
if (i == 0):
    i+=1
    print(i)
    sum += 1
    jumlah+=i
    while (i >= 1) and (i <99) :
        i+=2
        print(i)
        sum += 1
        jumlah += i
print("Jumlah perulangan    :  ", str(sum))
print("Jumlah Seluruh Bilangan  :   ", str(jumlah))