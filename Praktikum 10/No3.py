myFile=open('d:data2.txt','r')
f=[]
for a in myFile:
    b=a.split('|')
    c=b[0]
    d=b[1]
    e=b[2]
    dataMhs={'nim':c,'nama':d,'alamat':e}
    f=dict(dataMhs)
    print(f)
myFile.close()