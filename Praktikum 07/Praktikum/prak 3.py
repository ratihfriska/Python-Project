file=open("d:/data1.txt", "r")
sum = 0
print('Bilangan dalam file data.txt di D yang dijumlahkan adalah ')
for data in file :
    try:
        sum=sum+int(data)
        print(data)
    except ValueError:
        print('Bukan bilangan bulat\n')
print('Hasil penjumlahan semua bilangan yang ada di dalam file data.txt di D adalah ',sum)