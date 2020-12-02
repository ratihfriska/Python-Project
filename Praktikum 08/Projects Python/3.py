a=int(input('Berapa banyak data yang diinginkan? '))
print('Nama Mahasiswa :')
b=0
dataMhs=[]
for b in range (a):
    d=input()
    c=len(d)
    e=d+'  ('+ str(c)+ ' karakter)'
    dataMhs.append(e)
dataMhs.sort()
print('-'*30)
for f in dataMhs:
    print(f)