arr=input().split()

a=int(arr[0])
b=int(arr[1])

for i in range (a,b):
    if i%2==0:
        print(i,end=' ')
        i+=3

    elif i%2==1:
        print(i,end=' ')
        i*=2