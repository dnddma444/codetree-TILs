n=int(input())
num=0
cnt=0
s=0

for i in range (n):
    num=int(input())
    cnt+=1
    s+=num

print(s,f"{s/cnt:.1f}")