arr=input().split()
a,b,c=int(arr[0]),int(arr[1]),int(arr[2])
sat=True

for i in range (a,b+1):
    if i%c!=0:
        sat=True
    elif i%c==0:
        sat=False
        break

if sat==True:
    print('YES')
else:
    print('NO')