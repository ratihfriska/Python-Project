print('Buatlah list a = [1, 5, 6, 3, 6, 9, 11, 20, 12] dan b = [7, 4, 5, 6, 7, 1,12, 5, 9]')
a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
print(a)
print(b)

print('Sisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b')
a[3]=10
b[2]=15
print(a)
print(b)

print('Sisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b')
a[-1]=4
b[-1]=8
print(a)
print(b)

print('sorting secara ascending pada list a dan b')
a.sort()
print(a)
b.sort()
print(b)

print('Buatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)')
c=a[0:8]
d=b[2:10]
print(c)
print(d)

print('Buatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya.')
e=[]
n=0
for n in range (len(d)):
    indeks=c[n]+d[n]
    e+= [indeks]
e.append(c[-1])
print(e)

print('Ubahlah list e ke dalam tuple')
myTuple=tuple(e)
print(myTuple)

print('Carilah nilai min, maks, dan jumlahan seluruh elemen dari e')
print('nilai min : ',min(e))
print('nilai max : ',max(e))
print('jumlah seluruh elemen dari e adalah ',sum(e))

print('Buatlah	sebuah	string	myString = "python	adalah	bahasa	pemrograman	yang menyenangkan"')
myString= "python adalah bahasa pemrograman yang menyenangkan"

print('Dengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut')
hrfpnysn=set(myString)
hrfpnysn.remove(' ')
print('huruf penyusun : ', hrfpnysn)

print('Urutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list')
print('mengubah ke list: ')
f=list(hrfpnysn)
print(f)
print('mengurutkan secara alfabet : ')
f.sort()
print(f) 