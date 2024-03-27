n=input().split()

a=int(n[1])
b=int(n[0])

while a<=b:
    if b%2==0 :
        print(b,end=' ')
    b-=1