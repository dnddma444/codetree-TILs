a=input().split()
b=input().split()

aA,aS=int(a[0]),a[1]
bA,bS=int(b[0]),b[1]

if (aS=='M'and aA>=19) or (bS=='M'and bA>=19):
    print("1")
else : print('0')