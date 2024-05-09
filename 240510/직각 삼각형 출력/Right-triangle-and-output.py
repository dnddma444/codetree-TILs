n= int(input())

for i in range (1,n+1):
    for i in range (n-(n-i)):
        print('*',end='')
    for i in range (n-(n-i)):
        print('*',end='')
    print('')