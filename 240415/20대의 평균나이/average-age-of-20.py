cnt=0
s=0

while True:
    n=int(input())
    if n>=30 or n<=19:
        print(f'{s/cnt:.1f}')
        break

    else:
        cnt+=1
        s+=n