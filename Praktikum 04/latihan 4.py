#jarak
jarak1 = int(input("jarak1="))
jarak2 = int(input("jarak2="))

#kecepatan
kecepatan1 = int(input("kecepatan1="))
kecepatan2 = int(input("kecepatan2="))

#waktu perjalanan
berangkatjam = int(input("Jam berangkat (jam)="))
berangkatmenit =int(input("menit berangkat(menit)="))
istirahatjam =int(input("istirahat(jam)= "))
istirahatmenit=int(input("istirahat(menit)="))

import math
waktuperjalananjam =round(jarak1/kecepatan1)+ round(jarak2/kecepatan2)

#waktu sampai
print("waktu sampai ke kota C =",(berangkatjam + berangkatmenit + istirahatjam + istirahatmenit/100 + waktuperjalananjam))
