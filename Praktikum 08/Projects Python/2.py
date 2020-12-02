def dataStat():
    a=sum(x)/len(x)
    b=max(x)
    c=min(x)
    d=[a,b,c]
    return d
x=[9,12,13,17,2,7,8,9,5,11]
print('x = ', x)
d=dataStat()
print('list baru yang dihasilkan = ', d)