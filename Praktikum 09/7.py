mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*80)
print(('NIM').ljust(10,' '),end=' ')
print(('NAMA MAHASISWA').ljust(15,' '),end=' ')
print(('TGL LAHIR').center(20,' '),end=' ')
print(('TEMPAT LAHIR').ljust(10,' '))
print('-'*80)
for a in mhs:
       b=a.split(':')
       c=b[0]
       x=b[1]
       e=b[2]
       f=b[3]     
       print((c.ljust(10,' ')),((x).ljust(20,' ')),(e.ljust(15,' ')),f.ljust(10,' '))
                           

print('-'*80)