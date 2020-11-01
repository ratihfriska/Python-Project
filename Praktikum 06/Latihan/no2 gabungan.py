def starFormation1(n):
    for i in range(0, n-3):
        for j in range(0, i + 1):
            print('* ' , end='')
        print('')
    for i in range(0, n):
        for j in range(0, (n-4)):
            print('* ' , end='')
        n-=1
        print('')
n=7
starFormation1(n)