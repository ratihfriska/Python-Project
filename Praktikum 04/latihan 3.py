import math

jarak = int(input("jarak tempuh = "))

liter = jarak/12
print("bensin yang diperlukan", liter ,"liter")
print("karena bensin di awal full, maka")
banyakisi = (liter-50)/50
print("banyak pengisian=", math.ceil(banyakisi) , ("kali"))
