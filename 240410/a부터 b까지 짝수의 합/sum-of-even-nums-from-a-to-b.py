arr=input().split()

a=int(arr[0])
b=int(arr[1])
cnt=0

for i in range (a,b+1):
    if i%2==0:
        cnt+=i

print(cnt)