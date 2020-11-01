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
average(5, 10, 4, 9, 30, 16, 2, 11)
sum(5, 10, 4, 9, 30, 16, 2, 11)
max(5, 10, 4, 9, 30, 16, 2, 11)
min(5, 10, 4, 9, 30, 16, 2, 11)
print('======================================================')
average(81, 98, 12, 83, 45, 77, 69, 30, 56)
sum(81, 98, 12, 83, 45, 77, 69, 30, 56)
max(81, 98, 12, 83, 45, 77, 69, 30, 56)
min(81, 98, 12, 83, 45, 77, 69, 30, 56)