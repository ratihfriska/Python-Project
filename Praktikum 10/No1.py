myFile=open('d:data1.txt','r')
b=0
c=0
for a in myFile:
    if a==1:
        c+=1
    if int(a) % 2==0:
        b+=1
    if int(a) % 2==1:
        c+=1
print('Jumlah bilangan genap ada : ',b)
print('Jumlah bilangan ganjil ada : ',c)
myFile.close()