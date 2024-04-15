n=int(input())
num=1
for i in range (1,10):
    num*=i
    if num>=n:
        break
print(i)