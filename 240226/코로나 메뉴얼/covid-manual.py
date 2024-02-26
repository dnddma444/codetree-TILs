a=input().split()
b=input().split()
c=input().split()

ac,at=a[0],int(a[1])
bc,bt=b[0],int(b[1])
cc,ct=c[0],int(c[1])

if (ac=='Y'and bc=='Y') or (cc=='Y'and bc=='Y') or (cc=='Y'and ac=='Y'):
    if (at>=37 and bt>=37) or (at>=37 and ct>=37) or (bt>=37 and ct>=37):
        print('E')
    else: print("N")