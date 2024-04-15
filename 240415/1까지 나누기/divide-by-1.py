n=int(input())
cnt=1
num=n
for i in range (1,n):
    if num//i>1:
        num//=i
        cnt+=1
    else:
        break

print(cnt)