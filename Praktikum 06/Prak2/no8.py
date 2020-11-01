def luasSegitiga(a,t):
    luas = a * t /2
    return luas
alas = 10
alas2= 15
tinggi = 20
tinggi2= 45
print ('Luas Segitiga dg alas ', alas, 'dan tinggi  ', tinggi,' adalah  ',   luasSegitiga(alas,tinggi))
print ('Luas Segitiga dg alas ', alas2, 'dan tinggi  ', tinggi2,' adalah  ',   luasSegitiga(alas2,tinggi2))
luastotal=luasSegitiga(alas,tinggi)+luasSegitiga(alas2,tinggi2)
print('luas total = ',luastotal)