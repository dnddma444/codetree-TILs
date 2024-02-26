a=input().split()
b=input().split()
am,ae=int(a[0]),int(a[1])
bm,be=int(b[0]),int(b[1])

if am>bm:
    print("A")
elif am<bm:
    print("B")

if am==bm:
    if ae>be:
        print("A")
    else:print("B")