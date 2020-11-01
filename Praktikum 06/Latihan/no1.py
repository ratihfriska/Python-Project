def isPythagoras(a,b,c):
    nilai = ((a**2 + b**2) == (c**2) )
    return nilai
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
isPythagoras(a,b,c)
print('a = ',a,',b= ',b, ',c = ', c, '----->', isPythagoras(a,b,c))