try:
    kata=input('Masukkan Kata : ')
    n=int(input('Masukkan nilai n : '))
    hasil=" "
    for a in kata:
        if a.isupper():
            kode_c=ord(a)
            nilai_c=ord(a)-ord("A")
            kode_baru=(nilai_c - n)%26
            nilaifix=kode_baru+ord("A")
            katabaru=chr(nilaifix)
            hasil+=katabaru
        if a.islower():
            kode_c=ord(a)
            nilai_c=ord(a)-ord("a")
            kode_baru=(nilai_c - n)%26
            nilaifix=kode_baru+ord("a")
            katabaru=chr(nilaifix)
            hasil+=katabaru
    print('hasil',hasil)
except ValueError:
    print('Masukkan n berupa angka!')