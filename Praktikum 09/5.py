nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*70)
print('NIM'.ljust(20,' '),end=' ')
print('NAMA'.ljust(20,' '),end=' ')
print('N.MID'.ljust(10,' '),end=' ')
print('N.UAS'.rjust(10,' '))
print('-'*70)
def data():
    a=0
    b={}
    for n in nilai:
        b['nim']=n.get('nim')
        b['mid']=n.get('mid')
        b['nama']=n.get('nama')
        b['uas']=n.get('uas')
        print(b['nim'].ljust(20,' '),end=' ')
        print(b['nama'].ljust(15,' '),end=' ')
        print(str(b['mid']).rjust(10,' '),end=' ')
        print(str(b['uas']).rjust(15,' '))
    print('-'*70)
data()