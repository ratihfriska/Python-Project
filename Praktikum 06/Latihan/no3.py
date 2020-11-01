#nilai faktorial
def faktorial(n):
    hasil = 1
    for i in range (2, n + 1):
        hasil *= i
    return hasil
#nilai kombinasi
print("Menghitung Nilai Kombinasi  C(a,b) :")
a=int(input("a= "))
b=int(input("b= "))
hasil1=(faktorial(a)/(faktorial(b)*faktorial(a-b)))
print('C(',a,',',b,') = ',int(hasil1))
#nilai permutasi
print("Menghitung Nilai Permutasi  P(c,d) :")
c=int(input("c= "))
d=int(input("d= "))
hasil2=(faktorial(c)/faktorial(c-d))
print('P(',c,',','d) = ', int(hasil2))