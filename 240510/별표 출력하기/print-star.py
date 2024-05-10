n=int(input())
for i in range (n):
    for i in range(n+1-(n-i)):
        print('*',end=" ")
    print('')

for i in range (n):
    for i in range(n-i):
        print('*',end=" ")
    print('')