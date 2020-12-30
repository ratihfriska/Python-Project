a=open('d:data3.txt','r')
for b in a:
    c=b.split('|')
    print((int(c[0]))+(int(c[1])))
a.close()