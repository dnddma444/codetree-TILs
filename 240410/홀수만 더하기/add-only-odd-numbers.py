n=int(input())
num=0
cnt=0
for i in range (n):
    num=int(input())
    if num%2==1 and num%3==0:
        cnt+=num

print(cnt)