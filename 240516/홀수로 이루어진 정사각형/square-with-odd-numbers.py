n=int(input())

for i in range (1,2*n+1,2):
    for j in range(1,2*n+1,2):
        print(9+j+i,end=' ')
    print()