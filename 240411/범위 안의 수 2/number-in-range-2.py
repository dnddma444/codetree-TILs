num=0
s=0
cnt=0

for i in range(10):
    num=int(input())
    if num>=0 and num<=200:
        s+=num
        cnt+=1

print(s,f"{s/cnt:.1f}")