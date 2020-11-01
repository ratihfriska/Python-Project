from operation import *
a = 2
b = 4
c = 6
d = 7
e = 9
f = 10              
g = 5
h = 12
i = 34
print(a, '+', b, '*', c, '-', b, '=' , kurang(jumlah(kali(b,c),a),b))
print('(',b, '+', d, ')*(', c, '-', e, ') = ',kali((jumlah(b, d)),kurang(c,e)))
print('(',f, '+', a, ')/(', d, '+', g, ')/(', h, '-', i, ')=', bagi(bagi(jumlah(f,a),jumlah(d,g)),kurang(h,i)))