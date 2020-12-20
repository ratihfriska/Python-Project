nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
import math
print('='*100)
print('NIM'.ljust(20,' '),end=' ')
print('NAMA'.ljust(20,' '),end=' ')
print('N.MID'.ljust(10,' '),end=' ')
print('N.UAS'.rjust(10,' '),end=' ')
print('N.AKHIR'.rjust(15,' '),end=' ')
print('STATUS'.rjust(15,' '))
print('-'*100)
def data():
    a=0
    b={}
    for n in nilai:
        b['nim']=n.get('nim')
        b['mid']=n.get('mid')
        b['nama']=n.get('nama')
        b['uas']=n.get('uas')
        nilaiAkhir=round((b['mid']+2*b['uas'])/3)
        if nilaiAkhir < 60 :
            status='TIDAK LULUS'
        if nilaiAkhir >= 60 :
            status='LULUS'
        print(b['nim'].ljust(20,' '),end=' ')
        print(b['nama'].ljust(15,' '),end=' ')
        print(str(b['mid']).rjust(10,' '),end=' ')
        print(str(b['uas']).rjust(15,' '),end=' ')
        print(str(nilaiAkhir).rjust(15,' '),end=' ')
        print(status.rjust(15,' '))
    print('-'*100)
data()