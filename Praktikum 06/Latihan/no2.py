def starFormation1(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('* ' , end='')
        print('')
n=4
starFormation1(n)
print("=========================================")
def starFormation2(n):
     for i in range(0, (n+1)):
        for j in range(0, (n)):
            print('* ' , end='')
        n-=1
        print('')
n=4
starFormation2(n)