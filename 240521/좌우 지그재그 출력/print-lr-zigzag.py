n=int(input())
cnt=0
for i in range (1,n+1):
    if i%2==0:
        for j in range (1,n+1):
            print(i*n-j+1,end=' ')
        print()
    else :
        for j in range (1,n+1):
            print(i*n+j-n,end=' ')

        print()