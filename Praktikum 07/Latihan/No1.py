try:
    file=input('Masukkan nama file: ')
    file1=open(file,"r")
    print('Isi file', file, 'adalah ')
    print(file1.read())
except FileNotFoundError:
    print('File tidak ditemukan')