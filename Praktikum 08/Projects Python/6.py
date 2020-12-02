def sortStringByChar():
    myData.sort(key=len)
    print('Data Setelah diurutkan berdasarkan jumlah karakter : ',myData)
myData=['Cilok','Seblak','Sop','Sate','Thaitea']
print('data mula mula : ', myData)
sortStringByChar()