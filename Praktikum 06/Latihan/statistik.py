# membuat fungsi rata-rata
def sum(*myData):
    sum=0
    i = 0
    for data in myData:
        sum+=data
        i += 1
    print('Jumlah dari',myData,': ', sum)
def average(*myData):
    sum=0
    i = 0
    for data in myData:
        sum+=data
        i += 1
    rata2 = sum/i
    print('Rata-rata dari',myData,': ', rata2)
def max(*myData):
    max=0
    for data in myData:
        if data>max:
            max=data
    print('Nilai maksimum dari',myData,': ', max)
def min(*myData):
    min=99
    for data in myData:
        if data < min:
            min = data
    print('Nilai minimum dari',myData,': ', min)
sum()
average()
max()
min()